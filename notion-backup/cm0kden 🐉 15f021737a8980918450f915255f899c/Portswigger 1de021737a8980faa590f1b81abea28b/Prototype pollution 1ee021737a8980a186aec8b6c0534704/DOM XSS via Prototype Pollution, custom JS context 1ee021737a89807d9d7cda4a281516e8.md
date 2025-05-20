# DOM XSS via Prototype Pollution, custom JS context

During a webapp testing, an interesting sink was found:

![image.png](DOM%20XSS%20via%20Prototype%20Pollution,%20custom%20JS%20context%201ee021737a89807d9d7cda4a281516e8/image.png)

It was evaluating a macros, we also were able to pollute it using prototype pollution. But standard `alert(1)` payload was not executing because of Syntax error in JS. That’s because before it, a statement `a+1` is done. So, to accommodate, a payload must result in a valid arithmetic expression. To do so, we can apply `-` or `/` to make a NaN-resulting valid JS code: `alert(1)-1` or `alert(1)/1` 

![image.png](DOM%20XSS%20via%20Prototype%20Pollution,%20custom%20JS%20context%201ee021737a89807d9d7cda4a281516e8/image%201.png)