---
layout: page
title: Probing Mechanical Reasoning in Large Vision Language Models
subtitle: 
---

[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)

<center>
<div class="assets">
<a href="https://arxiv.org/abs/2410.00318" target="_blank">[paper]</a>
</div>
</center>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Abstract</h3>
<ul>
    Mechanical reasoning is a fundamental ability that sets human intelligence apart from other animal intelligence. Mechanical reasoning allows us to design tools, build bridges and canals, and construct houses which set the foundation of human civilization. Embedding machines with such ability is an important step towards building human-level artificial intelligence. Recently, Li et al. built CogDevelop2K, a data-intensive cognitive experiment benchmark for assaying the developmental trajectory of machine intelligence (Li et al., 2024). Here, to investigate mechanical reasoning in Vision Language Models, we leverage the MechBench of CogDevelop2K, which contains approximately 150 cognitive experiments, to test understanding of mechanical system stability, gears and pulley systems, seesaw-like systems and leverage principle, inertia and motion, and other fluid-related systems in Large Vision Language Models. We observe diverse yet consistent behaviors over these aspects in VLMs.
</ul>

<h3>VLMs Partially Understand Mechanical System Stability</h3>
<!--
<p>
VLMs performance in intuitively evaluating system stability is not ideal, however here we observe some interesting phenomena. Models excel at identifying objects in images, and they not only understand what the objects are, the models also successfully recognize their mechanical states as well. Also, the models could effectively connect mechanical descriptions with the corresponding mechanical scenarios. In Experiments 2B and 2F, the models could recognize the two chairs and the two bottles, and their mechanical situations; however, the models still failed to provide the correct answers in the experiments. For instance, in Experiment 2B, the model explains, "the stool on the right is more likely to tip over when an active child sits on it because its legs are splayed at an angle, making the base wider and potentially more stable under normal circumstances but also adding a tipping hazard due to the non-vertical configuration of the legs". The model correctly notices that it’s the angle of the leg that matters for the stability of the system. However, it reasons completely the opposite way to correct answers. When the leg’s angle wider, it’s actually more stable. It’s a very intuitive physical problem for humans but the models fail, even though they still demonstrate step-by-step reasoning abilities in this case. In Experiment 2F, the model is correct that the bottle on the bottom "has a larger area of contact with the surface, creating more friction, which helps prevent rolling". However, the model fails to realize one bottle is standing, and one bottle is rolling, and sliding friction and rolling friction are completely different. In contrast, humans can easily solve these problems intuitively.
</p>
-->
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_1.jpg">
</figure>

<h3>VLMs Don't Understand Pulley Systems</h3>
<!--
<p>We find that current VLMs struggle to handle pulley systems. There are generally three failures in VLMs' reasoning about pulley systems: first, VLMs are not able to identify which are the movable pulleys in the system, and second, VLMs exhibit relatively low accuracy in determining whether an object is rising or falling through pulley systems.</p>

<p>VLMs perform poorly in recognizing movable pulley systems. In one experiment, the image includes a standard single movable pulley system and a standard single fixed pulley system. The question "Which system requires less effort?" essentially asks whether the model can correctly select the movable pulley. Clearly, the model failed in its selection, as it straightforwardly provided an incorrect answer in its explanation. VLMs also struggle in predicting whether a suspended weight is being lifted or lowered through a pulley system. Multiple experiments either directly or indirectly reflect this issue, with one experiment being the most direct and concise. In this case, the weight is directly attached to the movable pulley, and by pulling the other end of the rope, the pulley and the weight are lifted. However, the model's response was the exact opposite of the correct answer. In its explanation, the model seemed to imply that the pulley was not fixed (though it did not explicitly state that it was a movable pulley), and the physics it provided was entirely incorrect. Therefore, we can hypothesize that the model's poor performance in predicting the weight's movement may be due to its limited ability to recognize movable pulleys. However, the specific reasons require further experiments to be analyzed in detail.</p>
<p>The above issues confirm that VLMs still have limitations in recognizing pulley systems. For individuals with some mechanical experience, identifying simple pulley systems through basic diagrams is not difficult.</p>
-->
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_2.jpg">
</figure>

<h3>VLMs Understand Gear Systems</h3>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_3.jpg">
</figure>

<h3>Understanding of Seesaw-like systems and Leverage Principle</h3>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_4.jpg">
</figure>

<h3>Reasoning about Inertia and Motion</h3>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_5.jpg">
</figure>
</div>

<h3>Reasoning about Fluids System</h3>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_5.jpg">
</figure>
</div>
