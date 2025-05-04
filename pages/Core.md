---
layout: page
title: Core Knowledge Deficits in MLLMs
subtitle: Investigating the Foundations of Multimodal Intelligence
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="https://arxiv.org/abs/2410.10855" target="_blank">📃 Paper 📃 </a>
<a href="" target="_blank">💾 Data (Coming Soon) 💾</a>
<a href="" target="_blank">📠 Code (Coming Soon) 📠</a>
</div>
</center>

<div class="pub-badge" style="display: inline-block; background-color: #4A154B; color: white; padding: 4px 10px; border-radius: 20px; font-size: 11pt; margin-bottom: 10px;">Accepted at ICML 2025</div>

<div class='description' style='font-size: 11pt;margin-bottom: 20pt'>
<h3>Abstract</h3>
<p>
While Multi-modal Large Language Models (MLLMs) demonstrate impressive abilities over high-level perception and reasoning, their robustness in the wild still lags behind humans and exhibits diminished efficacy on simple tasks that are intuitive for humans. We examine the hypothesis that these deficiencies stem from the absence of core knowledge—rudimentary cognitive abilities innate to humans from early childhood.
</p>
<p>
To probe core knowledge representation in MLLMs, we draw from developmental cognitive sciences and develop a large-scale benchmark, the <b>CoreCognition dataset</b>, encompassing 12 core cognitive concepts. We evaluate 219 models with 10 different prompts, leading to a total of 2409 data points for analysis. Our findings reveal core knowledge deficits in early-developed core abilities while models demonstrate human-comparable performance in high-level cognition. Moreover, we find that low-level abilities show little to no scaling, in stark contrast to high-level abilities. Finally, we introduce an evaluation technique "Concept Hacking," through which we demonstrate that MLLMs do not genuinely advance toward core knowledge but instead rely on illusory understanding and shortcut learning as they scale.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/final_1_2.png" alt="Data statistics and cognitive development map" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Left: Data statistics of CoreCognition dataset. Right: Map of core cognitive abilities organized by developmental stage, with dependency relationships indicated by arrows.</figcaption>
</figure>

<h3>Core Cognitive Abilities</h3>
<p>
Our study examines 12 core cognitive abilities organized across three developmental stages based on Piaget's theory of cognitive development:
</p>

<h4>Sensorimotor Stage</h4>
<ul>
    <li><b>Boundary:</b> The transition from existence to non-existence of objects</li>
    <li><b>Continuity:</b> Physical properties of objects tend to exist in the same way</li>
    <li><b>Permanence:</b> Things continue to exist when they are not in sight</li>
    <li><b>Spatiality:</b> The <i>a priori</i> understanding of the Euclidean properties of our world</li>
    <li><b>Perceptual Constancy:</b> Changes in appearances don't mean changes in physical properties</li>
</ul>

<h4>Concrete Operational Stage</h4>
<ul>
    <li><b>Intuitive Physics:</b> Intuitions about the laws of how things interact in the physical world</li>
    <li><b>Perspective Taking:</b> To see what others see</li>
    <li><b>Hierarchy:</b> Understanding of inclusion and exclusion of objects and categories</li>
    <li><b>Conservation:</b> Invariances of properties despite transformations</li>
</ul>

<h4>Formal Operational Stage</h4>
<ul>
    <li><b>Tool Use:</b> The capacity to manipulate specific objects to achieve goals</li>
    <li><b>Intentionality:</b> To see what others want</li>
    <li><b>Mechanical Reasoning:</b> Inferring actions from system states and vice versa</li>
</ul>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/final_2.jpg" alt="Examples from CoreCognition dataset" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Examples of tasks from the CoreCognition dataset, illustrating how each cognitive ability is assessed.</figcaption>
</figure>

<h3>Key Findings</h3>

<h4>MLLMs Show Reversed Cognitive Development</h4>
<p>
We found that MLLMs perform significantly better on tasks associated with later stages of cognitive development (Formal Operational), while their performance was comparatively worse on tasks that typically emerge earlier in human cognition (Sensorimotor). This suggests a rather unusual "reversed cognitive developmental trajectory" in these models.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/Graph2.png" alt="Performance across developmental stages" style="max-width: 70%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">MLLMs demonstrate better performance on higher-level abilities (Formal Operational) than on lower-level abilities (Sensorimotor), which is contrary to human cognitive development.</figcaption>
</figure>

<h4>Core Knowledge Deficits Don't Improve with Scale</h4>
<p>
Our scaling analysis revealed that while high-level abilities improve with larger model sizes, low-level abilities show minimal or no improvement. Some abilities, like perspective-taking, even deteriorate with increased scale. This indicates that simply increasing model parameters won't address core knowledge deficits.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/scalling.png" alt="Relationship between model performance and size" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Scaling laws do not apply uniformly across all cognitive abilities. While high-level abilities improve with model size, low-level abilities show little to no improvement.</figcaption>
</figure>

<h4>Concept Hacking: Models Rely on Shortcuts, Not Core Knowledge</h4>
<p>
To probe whether models genuinely understand core concepts or merely exploit statistical correlations, we developed "Concept Hacking" - a method that manipulates task-relevant details to invert the ground truth while preserving irrelevant conditions. Our analysis revealed that models either rely on shortcuts from their training data or possess illusory understandings that are opposite to reality, rather than developing true core knowledge.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/final_3.png" alt="Examples of Concept Hacking" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Examples of Concept Hacking methodology. Left: A model relying on shortcuts would succeed in the standard task but fail the manipulated one. Right: A model with an illusory understanding would fail the standard task but succeed in the manipulated version.</figcaption>
</figure>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/Core/parrot.png" alt="Concept Hacking results" style="max-width: 70%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Accuracy of MLLMs on Control vs. Manipulation tasks in Concept Hacking. As models scale, they increasingly rely on either shortcuts or illusory understandings rather than developing true core knowledge like humans (who would progress along the diagonal).</figcaption>
</figure>

<h3>Implications</h3>
<p>
Our findings suggest that current MLLMs exhibit fundamental core knowledge deficits—they lack a basic understanding of key domains such as objects, actions, numbers, space, and social relations, which humans possess from infancy. While these models can perform impressively on high-level tasks, they achieve this through shortcuts and statistical correlations rather than through a genuine understanding of how the world works.
</p>
<p>
This has important implications for the development of robust AI systems. Without core knowledge to ground their reasoning, MLLMs may continue to struggle with generalization and robustness in real-world scenarios. Our results suggest that addressing these deficits may require architectural innovations beyond simply scaling up current models.
</p>
</div>
