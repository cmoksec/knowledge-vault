# Web cache deception

Created: May 19, 2025 2:50 PM

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%201.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%202.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%203.png)

The key to perform cache deception attack is to trick a caching agent to store a non-cacheable resource with sensitive data as it would be some static file or other cacheable resource.

Cache deception is most often occurs when a cache agent and origin server treat URLs differently — e.g. while origin servers treats `/myaccount;abc.js` as `/myaccount` , cache agent applies a rule for caching static scripts and stores a page with confidential data thinking it’s a script.

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%204.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%205.png)

## Mapping discrepancies

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%206.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%207.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%208.png)

[Basic Web cache deception attack](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/Basic%20Web%20cache%20deception%20attack%201f9021737a8980ed83ebe31bd883185a.md)

---

## Delimiter discrepancies

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%209.png)

[Exploiting delimiters for Web cache deception](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/Exploiting%20delimiters%20for%20Web%20cache%20deception%201f9021737a89801a97fde6fffd2827a8.md)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2010.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2011.png)

---

## Normalization discrepancies

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2012.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2013.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2014.png)

[Using origin server normalization to do web cache deception](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/Using%20origin%20server%20normalization%20to%20do%20web%20cache%20%201f9021737a89800a8dbfec2380826404.md)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2015.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2016.png)

[Using caching agent normalization to do web cache deception](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/Using%20caching%20agent%20normalization%20to%20do%20web%20cache%20%201f9021737a8980c9ad54dc863e432a3d.md)

---

## File name cache discrepancies

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2017.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2018.png)

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2019.png)

---

## Prevention

![image.png](Web%20cache%20deception%201f8021737a898021a623c141ff688e3f/image%2020.png)

---

## Web cache deception delimiters wordlist

```jsx
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?
@
[
\
]
^
_
`
{
|
}
~
%21
%22
%23
%24
%25
%26
%27
%28
%29
%2A
%2B
%2C
%2D
%2E
%2F
%3A
%3B
%3C
%3D
%3E
%3F
%40
%5B
%5C
%5D
%5E
%5F
%60
%7B
%7C
%7D
%7E
```