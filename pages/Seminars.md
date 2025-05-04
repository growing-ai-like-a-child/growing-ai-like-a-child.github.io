---
layout: page
title: GrowAI Seminars
subtitle: 
---

[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<!-- <a href="mailto:growing.ai.like.a.child@gmail.com" target="_blank">[Contact Us]</a>
<a href="https://github.com/growing-ai-like-a-child" target="_blank">[Github]</a> -->
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

/* Featured seminar styling */
.featured-seminar {
  width: 100%;
  max-width: 900px;
  margin: 0 auto 40px auto;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(3, 102, 214, 0.2);
  background-color: #f5f9ff;
  border: 2px solid #0366d6;
  position: relative;
  overflow: hidden;
}

.featured-seminar::before {
  content: "FEATURED SEMINAR";
  position: absolute;
  top: 10px;
  right: -35px;
  background-color: #0366d6;
  color: white;
  padding: 5px 40px;
  font-size: 12px;
  font-weight: bold;
  transform: rotate(45deg);
}

.featured-content {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
}

.featured-image {
  flex: 1;
  min-width: 200px;
  text-align: center;
}

.featured-image img {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #0366d6;
}

.featured-details {
  flex: 2;
  min-width: 300px;
}

.featured-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 15px;
  color: #0366d6;
}

.featured-date {
  font-size: 18px;
  margin-bottom: 15px;
  font-weight: bold;
}

.featured-speakers {
  margin-bottom: 15px;
  font-size: 16px;
}

.featured-abstract {
  margin-bottom: 20px;
  font-size: 16px;
  line-height: 1.6;
}

.featured-materials {
  background-color: white;
  padding: 15px;
  border-radius: 8px;
  margin-top: 20px;
}

.featured-materials h3 {
  margin-top: 0;
  font-size: 18px;
  color: #0366d6;
}

.featured-materials ul {
  padding-left: 20px;
}

.featured-materials li {
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  .featured-content {
    flex-direction: column;
  }
  
  .featured-image {
    margin: 0 auto;
  }
}
</style>

<div id="intro">
  <div id="intro-text">
    <!-- <h1>GrowAI Seminars</h1> -->
    <p>
      GrowAI Seminars is an online series organized by the <a href="https://growing-ai-like-a-child.github.io/">Growing AI Like a Child</a> team. We invite researchers from AI, developmental psychology, cognitive science, and related fields to share insights and work toward understanding how artificial intelligence systems can develop more human-like capabilities through developmental trajectories similar to those of children.
    </p>
    <p>
      Join our <a href="https://join.slack.com/t/growingailikeachild/shared_invite/zt-309yqd0sl-W8xzOkdBPha1Jh5rnee78A">Slack</a> if you're interested in giving a talk or listening to upcoming talks.
    </p>
  </div>
  <div id="intro-image">
    <img src="/img/images/logo.jpeg" alt="GrowAI Logo">
  </div>
</div>

<div id="filters" class="button-group">
  <button class="button is-checked" data-filter="upcoming">Upcoming Seminars</button>
  <button class="button" data-filter="past">Past Seminars</button>
</div>

<!-- Featured Seminar -->
<div class="featured-seminar upcoming">
  <div class="featured-content">
    <div class="featured-image">
      <img src="/img/members/freda.jpg" alt="Freda Shi">
    </div>
    <div class="featured-details">
      <div class="featured-title">Grounding in AI: From Lexicons to Complex Meanings</div>
      <div class="featured-date">Date & Time: TBD</div>
      <div class="featured-speakers">
        <strong>Speaker:</strong> Freda Shi (University of Waterloo)<br>
        <strong>Host:</strong> Ziqiao Ma
      </div>
      <div class="featured-abstract">
        This comprehensive tutorial explores the concept of grounding in AI, defined as processing primary data with supervision from another source where the two sources have positive mutual information. The talk will connect existing work across visual, acoustic, factual, and cross-lingual grounding.
      </div>
    </div>
  </div>
</div>

<!--
<div class="seminar-grid">
  
  <div class="seminar-card past">
    <div class="seminar-title">Infant-Inspired Learning in Computer Vision Models</div>
    <div class="seminar-date">March 10, 2024 | 1:00 PM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/haiyun-lyu">Haiyun Lyu (UNC Chapel Hill)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/haiyun_lyu.jpg" alt="Haiyun Lyu">
    </div>
    <div class="seminar-abstract">
      In this talk, I discussed how principles from infant visual development can inform the architecture and training of computer vision models. By incorporating constraints and learning mechanisms observed in human infants.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>

  <div class="seminar-card past">
    <div class="seminar-title">Embodied Cognition and AI</div>
    <div class="seminar-date">February 15, 2024 | 11:00 AM ET</div>
    <div class="seminar-speaker">
      <a href="https://example.com/dezhi-luo">Dezhi Luo (University of Michigan)</a>
    </div>
    <div class="speaker-image">
      <img src="/assets/images/members/dezhi_luo.jpg" alt="Dezhi Luo">
    </div>
    <div class="seminar-abstract">
      This talk explored the role of embodiment in cognitive development and its implications for AI. Drawing from studies on how children learn through physical interaction with their environment.
    </div>
    <div class="seminar-link">
      <a href="https://youtube.com/recording">Recording</a>
    </div>
  </div>
  
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
-->

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Get filter buttons
  const upcomingButton = document.querySelector('[data-filter="upcoming"]');
  const pastButton = document.querySelector('[data-filter="past"]');
  
  // Get all seminar cards
  const seminarCards = document.querySelectorAll('.seminar-card');
  const upcomingCards = document.querySelectorAll('.seminar-card.upcoming');
  const pastCards = document.querySelectorAll('.seminar-card.past');
  
  // Get featured seminar
  const featuredSeminar = document.querySelector('.featured-seminar');
  
  // Add click handlers for filter buttons
  upcomingButton.addEventListener('click', function() {
    upcomingButton.classList.add('is-checked');
    pastButton.classList.remove('is-checked');
    
    // Show upcoming, hide past
    upcomingCards.forEach(card => card.style.display = 'block');
    pastCards.forEach(card => card.style.display = 'none');
    
    // Show featured seminar
    if (featuredSeminar) {
      featuredSeminar.style.display = 'block';
    }
  });
  
  pastButton.addEventListener('click', function() {
    pastButton.classList.add('is-checked');
    upcomingButton.classList.remove('is-checked');
    
    // Show past, hide upcoming
    pastCards.forEach(card => card.style.display = 'block');
    upcomingCards.forEach(card => card.style.display = 'none');
    
    // Hide featured seminar
    if (featuredSeminar) {
      featuredSeminar.style.display = 'none';
    }
  });
  
  // Initialize with upcoming seminars visible
  upcomingCards.forEach(card => card.style.display = 'block');
  pastCards.forEach(card => card.style.display = 'none');
  if (featuredSeminar) {
    featuredSeminar.style.display = 'block';
  }
});
</script> 