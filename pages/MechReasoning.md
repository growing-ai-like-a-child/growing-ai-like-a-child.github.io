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

<h3>Understanding of Mechanical System Stability</h3>
<ul>
VLMs performance in intuitively evaluating system stability is not ideal, however here we observe some interesting phenomena. Models excel at identifying objects in images, and they not only understand what the objects are, the models also successfully recognize their mechanical states as well. Also, the models could effectively connect mechanical descriptions with the corresponding mechanical scenarios. In Experiments 2B and 2F, the models could recognize the two chairs and the two bottles, and their mechanical situations; however, the models still failed to provide the correct answers in the experiments. For instance, in Experiment 2B, the model explains, "the stool on the right is more likely to tip over when an active child sits on it because its legs are splayed at an angle, making the base wider and potentially more stable under normal circumstances but also adding a tipping hazard due to the non-vertical configuration of the legs". The model correctly notices that it’s the angle of the leg that matters for the stability of the system. However, it reasons completely the opposite way to correct answers. When the leg’s angle wider, it’s actually more stable. It’s a very intuitive physical problem for humans but the models fail, even though they still demonstrate step-by-step reasoning abilities in this case. In Experiment 2F, the model is correct that the bottle on the bottom "has a larger area of contact with the surface, creating more friction, which helps prevent rolling". However, the model fails to realize one bottle is standing, and one bottle is rolling, and sliding friction and rolling friction are completely different. In contrast, humans can easily solve these problems intuitively.
</ul>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_MechReason/Case_1.jpg">
</figure>

</div>
