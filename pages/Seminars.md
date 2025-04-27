---
layout: page
title: GrowAI Seminars
subtitle: 
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="mailto:growing.ai.like.a.child@gmail.com" target="_blank">[Contact Us]</a>
<a href="https://github.com/growing-ai-like-a-child" target="_blank">[Github]</a>
</div>
</center>

<style>
#intro {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
  gap: 30px;
}

#intro-text {
  flex: 2;
}

#intro-image {
  flex: 1;
  text-align: center;
}

#intro-image img {
  max-width: 250px;
  border-radius: 8px;
}

.image-quote-container {
  text-align: center;
  margin: 40px 0;
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 10px;
}

.image-quote-container img {
  max-width: 300px;
  height: auto;
  border-radius: 8px;
}

.image-quote-container blockquote {
  margin-top: 20px;
  font-size: 1.5rem;
  font-style: italic;
  color: #555;
}

.button-group {
  margin: 30px 0;
  text-align: center;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 5px;
  margin: 0 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #e0e0e0;
}

.button.is-checked {
  background-color: #0366d6;
  color: white;
}

.seminar-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 40px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.seminar-card {
  width: 220px;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: #ffffff;
  display: none; /* Initially hidden, shown by JS */
}

.seminar-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

.seminar-title {
  font-size: 16px;
  font-weight: bold;
  margin-top: 15px;
  text-align: left;
}

.seminar-date {
  margin: 8px 0;
  font-size: 14px;
  text-align: left;
}

.seminar-speaker {
  margin: 15px 0;
  font-size: 14px;
  text-align: center;
}

.speaker-image {
  margin-top: 15px;
  text-align: center;
}

.speaker-image img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ddd;
}

.seminar-abstract {
  margin: 8px 0;
  font-size: 14px;
  line-height: 1.5;
  text-align: left;
  font-style: italic;
  max-height: 150px;
  overflow-y: auto;
}

.seminar-link {
  font-size: 14px;
  text-align: center;
  margin-top: 12px;
}

/* Category classes for filtering */
.upcoming {
  display: block;
}

.past {
  display: none;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .seminar-grid {
    gap: 15px;
  }
  
  .seminar-card {
    width: calc(50% - 15px);
    max-width: 220px;
  }
}

@media (max-width: 576px) {
  .seminar-card {
    width: 100%;
    max-width: 300px;
  }
}
</style>

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
  <img src="/assets/images/child-development.jpg" alt="Child Development" style="width: 300px; height: auto; border-radius: 8px; padding-top: 30px;">
  <blockquote style="margin-top: 20px; font-size: 1.5rem; font-style: italic; color: #555; padding-bottom: 20px;">
    "The goal is to make machines that learn and think like people" - Lake et al.
  </blockquote>
</div>

<div id="filters" class="button-group">
  <button class="button is-checked" data-filter="upcoming">Upcoming Seminars</button>
  <button class="button" data-filter="past">Past Seminars</button>
</div>

<div class="seminar-grid">
  <!-- Upcoming Seminar 1 -->
  <div class="seminar-card upcoming">
    <div class="seminar-title">Vision Language Models See What You Want but not What You See</div>
    <div class="seminar-date">May 15, 2024 | 2:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/qingying-gao">Qingying Gao (Johns Hopkins University)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/qingying_gao.jpg" alt="Qingying Gao" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      Knowing others' intentions and taking others' perspectives are two core components of human intelligence that are considered to be instantiations of theory-of-mind. In this talk, I will discuss our recent work investigating intentionality understanding and level-2 perspective-taking in Vision Language Models (VLMs).
    </div>
    <div class="seminar-link">
      <a href="https://zoom.us/link">Zoom Link</a>
    </div>
  </div>

  <!-- Upcoming Seminar 2 -->
  <div class="seminar-card upcoming">
    <div class="seminar-title">Developmental Trajectories in Large Language Models</div>
    <div class="seminar-date">June 5, 2024 | 3:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/hokin-deng">Hokin Deng (Carnegie Mellon University)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/hokin_deng.jpg" alt="Hokin Deng" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      This talk explores how large language models acquire capabilities in a sequence that mimics human cognitive development. Drawing parallels between the training progression of LLMs and the stages of child development.
    </div>
    <div class="seminar-link">
      <a href="https://zoom.us/link">Zoom Link</a>
    </div>
  </div>

  <!-- Upcoming Seminar 3 -->
  <div class="seminar-card upcoming">
    <div class="seminar-title">Cognitive Foundations of Learning in AI Systems</div>
    <div class="seminar-date">June 20, 2024 | 1:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/haoran-sun">Haoran Sun (Johns Hopkins University)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/haoran_sun.jpg" alt="Haoran Sun" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      This seminar examines how insights from cognitive development can inform better learning algorithms. We'll explore how fundamental cognitive capabilities like object permanence and causal reasoning might be incorporated into AI learning systems.
    </div>
    <div class="seminar-link">
      <a href="https://zoom.us/link">Zoom Link</a>
    </div>
  </div>

  <!-- Upcoming Seminar 4 -->
  <div class="seminar-card upcoming">
    <div class="seminar-title">Building Intrinsic Motivation in Reinforcement Learning</div>
    <div class="seminar-date">July 10, 2024 | 11:00 AM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/yijiang-li">Yijiang Li (UC San Diego)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/yijiang_li.jpg" alt="Yijiang Li" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      How do we build AI systems that explore and learn from their environment without explicit rewards? This talk examines approaches to intrinsic motivation inspired by developmental psychology and their implementation in RL agents.
    </div>
    <div class="seminar-link">
      <a href="https://zoom.us/link">Zoom Link</a>
    </div>
  </div>

  <!-- Past Seminar 1 -->
  <div class="seminar-card past">
    <div class="seminar-title">Infant-Inspired Learning in Computer Vision Models</div>
    <div class="seminar-date">March 10, 2024 | 1:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/haiyun-lyu">Haiyun Lyu (UNC Chapel Hill)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/haiyun_lyu.jpg" alt="Haiyun Lyu" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      In this talk, I discussed how principles from infant visual development can inform the architecture and training of computer vision models. By incorporating constraints and learning mechanisms observed in human infants.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>

  <!-- Past Seminar 2 -->
  <div class="seminar-card past">
    <div class="seminar-title">Embodied Cognition and AI</div>
    <div class="seminar-date">February 15, 2024 | 11:00 AM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/dezhi-luo">Dezhi Luo (University of Michigan)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/dezhi_luo.jpg" alt="Dezhi Luo" onerror="this.src='/assets/images/members/placeholder.jpg'">
    </div>
    <div class="seminar-abstract">
      This talk explored the role of embodiment in cognitive development and its implications for AI. Drawing from studies on how children learn through physical interaction with their environment.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>
  
  <!-- Past Seminar 3 -->
  <div class="seminar-card past">
    <div class="seminar-title">Theory of Mind in Multimodal Learning</div>
    <div class="seminar-date">January 25, 2024 | 2:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/jane-doe">Jane Doe (Stanford University)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/placeholder.jpg" alt="Jane Doe">
    </div>
    <div class="seminar-abstract">
      This seminar explored how theory of mind can be implemented in multimodal AI systems. We discussed computational approaches to modeling beliefs, intentions, and perspectives in language and vision models.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>
  
  <!-- Past Seminar 4 -->
  <div class="seminar-card past">
    <div class="seminar-title">Language Acquisition in Children and AI</div>
    <div class="seminar-date">December 10, 2023 | 10:00 AM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/john-smith">John Smith (MIT)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/placeholder.jpg" alt="John Smith">
    </div>
    <div class="seminar-abstract">
      This talk compared language acquisition processes in children with current approaches to training large language models. We examined key differences and opportunities for more human-like language learning in AI systems.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Get filter buttons
  const upcomingButton = document.querySelector('[data-filter="upcoming"]');
  const pastButton = document.querySelector('[data-filter="past"]');
  
  // Get all seminar cards
  const seminarCards = document.querySelectorAll('.seminar-card');
  const upcomingCards = document.querySelectorAll('.seminar-card.upcoming');
  const pastCards = document.querySelectorAll('.seminar-card.past');
  
  // Add click handlers for filter buttons
  upcomingButton.addEventListener('click', function() {
    upcomingButton.classList.add('is-checked');
    pastButton.classList.remove('is-checked');
    
    // Show upcoming, hide past
    upcomingCards.forEach(card => card.style.display = 'block');
    pastCards.forEach(card => card.style.display = 'none');
  });
  
  pastButton.addEventListener('click', function() {
    pastButton.classList.add('is-checked');
    upcomingButton.classList.remove('is-checked');
    
    // Show past, hide upcoming
    pastCards.forEach(card => card.style.display = 'block');
    upcomingCards.forEach(card => card.style.display = 'none');
  });
  
  // Initialize with upcoming seminars visible
  upcomingCards.forEach(card => card.style.display = 'block');
  pastCards.forEach(card => card.style.display = 'none');
});
</script> 