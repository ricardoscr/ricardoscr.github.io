---
layout: archive
permalink: /en/
title: All Posts
tagline: A List of Posts
tags: [blog]
author_profile: true
---

All english posts.

<ul class="post-list">
  {% assign pages_list = "R" %}  
  {% for post in pages_list %}
    {% if post.title != null %}
    {% if group == null or group == post.group %}
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}<span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%B %d, %Y" }}</time></span></a></li>
    {% endif %}
    {% endif %}
  {% endfor %}
  {% assign pages_list = nil %}
  {% assign group = nil %}
</ul>
