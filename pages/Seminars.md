---
layout: page
title: GrowAI Seminars
subtitle: 
---
<link rel="stylesheet" href="/assets/css/seminars.css">

<center>
<div class="assets">
<a href="mailto:growing.ai.like.a.child@gmail.com" target="_blank">[Contact Us]</a>
<a href="https://github.com/growing-ai-like-a-child" target="_blank">[Github]</a>
</div>
</center>

<div id="intro">
  <div id="intro-text">
    <h1>GrowAI Seminars</h1>
    <p>
      GrowAI Seminars is an online series organized by the <a href="https://growing-ai-like-a-child.github.io/">Growing AI Like a Child</a> team. We invite researchers from AI, developmental psychology, cognitive science, and related fields to share insights and work toward understanding how artificial intelligence systems can develop more human-like capabilities through developmental trajectories similar to those of children.
    </p>
    <p>
      <a href="mailto:growing.ai.like.a.child@gmail.com">Contact us</a> if you're interested in giving a talk or have suggestions for speakers.
    </p>
  </div>
  <div id="intro-image">
    <img src="/assets/images/logo.png" alt="GrowAI Logo">
  </div>
</div>

<div class="image-quote-container">
  <img src="/assets/images/child-development.jpg" alt="Child Development">
  <blockquote>
    "The goal is to make machines that learn and think like people" - Lake et al.
  </blockquote>
</div>

<div id="filters" class="button-group">
  <button class="button is-checked" data-filter="upcoming">Upcoming Seminars</button>
  <button class="button" data-filter="past">Past Seminars</button>
</div>

<div class="seminar-grid">
  {% for seminar in site.data.seminars %}
    <div class="seminar-card {{ seminar.type }}">
      <div class="seminar-title">{{ seminar.title }}</div>
      <div class="seminar-date">{{ seminar.date }} | {{ seminar.time }}</div>
      <div class="seminar-speaker">
        <a href="{{ seminar.url }}">{{ seminar.speaker }} ({{ seminar.affiliation }})</a>
      </div>
      <div class="speaker-image">
        <img src="{{ seminar.image }}" alt="{{ seminar.speaker }}">
      </div>
      <div class="seminar-abstract">
        {{ seminar.abstract }}
      </div>
      <div class="seminar-link">
        <a href="{{ seminar.link }}">{{ seminar.link_text }}</a>
      </div>
    </div>
  {% endfor %}
</div>

<script src="/assets/js/seminars.js"></script> 