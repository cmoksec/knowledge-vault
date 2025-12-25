# Server-side template injection in an unknown language with a documented exploit

Sus input

![Снимок экрана 2025-10-28 в 15.04.57.png](Server-side%20template%20injection%20in%20an%20unknown%20langu/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.04.57.png)

Use polyglot, see leaked details.

![Снимок экрана 2025-10-28 в 15.07.16.png](Server-side%20template%20injection%20in%20an%20unknown%20langu/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.07.16.png)

Template engine is handlebars

```jsx
/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/parser.js:267
            throw new Error(str);
            ^

Error: Parse error on line 1:
<%'${{/#{@}}%>{{
----^
Expecting 'EOF', got 'OPEN_ENDBLOCK'
    at Parser.parseError (/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/parser.js:267:19)
    at Parser.parse (/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/parser.js:336:30)
    at HandlebarsEnvironment.parse (/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/base.js:46:43)
    at compileInput (/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/compiler.js:515:19)
    at ret (/opt/node-v19.8.1-linux-x64/lib/node_modules/handlebars/dist/cjs/handlebars/compiler/compiler.js:524:18)
    at [eval]:5:13
    at Script.runInThisContext (node:vm:128:12)
    at Object.runInThisContext (node:vm:306:38)
    at node:internal/process/execution:83:21
    at [eval]-wrapper:6:24

Node.js v19.8.1
```

Search on hacktricks

![Снимок экрана 2025-10-28 в 15.15.15.png](Server-side%20template%20injection%20in%20an%20unknown%20langu/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.15.15.png)

Use URLEncoded payload, change command

![Снимок экрана 2025-10-28 в 15.15.52.png](Server-side%20template%20injection%20in%20an%20unknown%20langu/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.15.52.png)