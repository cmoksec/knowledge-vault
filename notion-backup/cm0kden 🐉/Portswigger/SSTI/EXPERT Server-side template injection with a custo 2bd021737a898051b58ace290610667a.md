# EXPERT: Server-side template injection with a custom exploit

![Снимок экрана 2025-12-02 в 14.05.59.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.05.59.png)

After trying to upload a php shell via avatar upload:

![Снимок экрана 2025-12-02 в 13.50.12.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.50.12.png)

Set preferred config from user.username to just user:

![Снимок экрана 2025-12-02 в 13.55.24.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.55.24.png)

Twig error:

![Снимок экрана 2025-12-02 в 13.55.58.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.55.58.png)

`blog-post-author-display` is being eval’ed:

```jsx
user.setAvatar('/home/carlos/User.php','image/jpg')
```

![Снимок экрана 2025-12-02 в 14.03.04.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.03.04.png)

The class has a deletion method:

![Снимок экрана 2025-12-02 в 14.03.49.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.03.49.png)

Link SSH key as an avatar:

![Снимок экрана 2025-12-02 в 14.05.32.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.05.32.png)

![Снимок экрана 2025-12-02 в 14.06.17.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.06.17.png)

And trigger deletion (template is evaluated on comments section, so you will need to reload post page)

![Снимок экрана 2025-12-02 в 14.06.47.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.06.47.png)

![Снимок экрана 2025-12-02 в 14.07.07.png](EXPERT%20Server-side%20template%20injection%20with%20a%20custo/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.07.07.png)