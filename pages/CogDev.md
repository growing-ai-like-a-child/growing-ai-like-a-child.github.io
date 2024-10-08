---
layout: page
title: CogDevelop2K
subtitle: Reversed Cognitive Development in Multi-modal Large Language Models
---

[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)

<center>
<div class="assets">
<a href="https://openreview.net/forum?id=fDNBPqgr4K" target="_blank">[paper]</a>
</div>
</center>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Abstract</h3>
<ul>
Are Multi-modal Large Language Models (MLLMs) stochastic parrots? Do they genuinely understand and are capable of performing the tasks they excel at? This paper aims to explore the fundamental basis of MLLMs, i.e. core cognitive abilities that human intelligence builds upon to perceive, comprehend, and reason. To this end, we propose CogDevelop2K, a comprehensive benchmark that spans 12 sub-concepts from fundamental knowledge like object permanence and boundary to advanced reasoning like intentionality understanding, structured via the developmental trajectory of a human mind. We evaluate 46 MLLMs on our benchmarks. Comprehensively, we further evaluate the influence of evaluation strategies and prompting techniques. Surprisingly, we observe a reversed cognitive developmental trajectory compared to humans.
</ul>

<figure>
    <img src="/material_1.jpg">
</figure>

<hr class="small" style="border-width: 0; height: 0px; background-color: lightgray; padding-top: 20px; padding-bottom: 20px;">
<h3>Cognitive Experiment Example</h3>
<ul>
A video-image interleaved example of multi-frame questions. To correctly infer the answer, model needs to understand the question by mapping each image (co-reference) to its option letter, to understand correlation between frames (temporal understanding) and to infer the possible trajectory of the bottle (reasoning).
</ul>

<figure>
    <img src="/img/CogDevelop2K/multi-interleave.png">
</figure>

<hr class="small" style="border-width: 0; height: 0px; background-color: lightgray; padding-top: 20px; padding-bottom: 20px;">
<h3>We built a comprehensive and exhaustive sets of cognitive exeperiments acoss three Piagetian developmental stages</h3>
<figure>
    <img src="/img/CogDevelop2K/case_pic.jpg">
</figure>

<hr class="small" style="border-width: 0; height: 0px; background-color: lightgray; padding-top: 20px; padding-bottom: 20px;">
<h3>We observe diverse performances across Multimodal Large Language Models </h3>
<figure>
    <img src="/img/CogDevelop2K/all-in-one-plot.png">
</figure>

</div>
