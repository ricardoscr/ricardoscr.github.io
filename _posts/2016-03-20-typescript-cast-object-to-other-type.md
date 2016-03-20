---
layout: post
# type: <nothing> | quote | status | video | photo
title: 'Typescript: cast an object to other type. How?'
category: Typescript
tags: [typescript, casting]
lang: 'en_US'
# description: Test dependencies are very common. Here they go.
# headline: Awesome snippet, let's begin testing ASAP!
comments: true
# modified: 2015-12-13
share: true
mathjax: false
# tags:
#  - alternate
#  - way
imagefeature: picture-38.jpg
#image:
#  feature: picture-38.jpg
#  credit: example.com
#  creditlink: "http://example.com/blog/stuff/"
# link: http://some-link-for-a-link-post
# featured: true
published: true
---

Typescript: cast an object to other type. How?

Use `<>`:

```typescript

var objectA: TypeA;
var objectX: TypeX;

objectA = <TypeA> objectX;

```