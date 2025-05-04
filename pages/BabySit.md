---
layout: page
title: BabySit
subtitle: Corrective Feedback Accelerates Neural Word Acquisition
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="https://arxiv.org/abs/2405.13828" target="_blank">📃 Paper </a>
<a href="https://github.com/sled-group/TnD" target="_blank">💻 Code </a>
</div>
</center>

<div style="text-align: center;">
  <div class="pub-badge" style="display: inline-block; background-color: #4A154B; color: white; padding: 6px 15px; border-radius: 25px; font-size: 12pt; margin: 15px auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-weight: bold;">Accepted at NAACL 2025</div>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 20pt'>
<h3>Abstract</h3>
<p>
Humans are efficient language learners and inherently social creatures. Our language development is largely shaped by our social interactions, for example, the demonstration and feedback from caregivers. Contrary to human language learning, recent advancements in large language models have primarily adopted a non-interactive training paradigm, and refined pre-trained models through feedback afterward.
</p>
<p>
In this work, we explore how corrective feedback from interactions influences neural language acquisition from scratch through systematically controlled experiments, assessing whether it contributes to word learning efficiency in language models. We introduce a trial-and-demonstration (TnD) learning framework that incorporates three distinct components: student trials, teacher demonstrations, and a reward conditioned on language competence at various developmental stages.
</p>
<p>
Our experiments reveal that the TnD approach accelerates word acquisition for student models of equal and smaller numbers of parameters, and we highlight the significance of both trials and demonstrations. We further show that the teacher's choices of words influence students' word-specific learning efficiency, and a practice-makes-perfect effect is evident by a strong correlation between the frequency of words in trials and their respective learning curves. Our findings suggest that interactive language learning, with teacher demonstrations and active trials, can facilitate efficient word learning in language models.
</p>

<h3>Introduction</h3>
<p>
Humans are social beings and we learn language from interactions. Long before children's linguistic skills are mature, they could engage in early forms of conversational exchange with others. A critical component of social interactions that language grounds to is the <i>feedback</i> provided by the caregivers. This includes the communicative feedback that highlights the success and failure of communication, and the corrective feedback that is more direct and emphasizes the responses from caregivers, which offer corrections to possible errors in children's speech.
</p>
<p>
Unlike human learners who acquire language skills through feedback during interactions, most language models differ in terms of their inductive biases and data sources. These models typically learn from massive text corpora using cross-entropy loss for self-supervised learning.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/BabySit/framework.png" alt="Trial-and-Demonstration (TnD) framework illustration" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">The Trial-and-Demonstration (TnD) learning framework incorporates three components: (a) A teacher model pre-trained with causal language modeling (CLM), (b) A student model that learns via alternating between CLM and reinforcement learning (RL), and (c) A reward conditioned on the neural age of the student model.</figcaption>
</figure>

<h3>Trial-and-Demonstration (TnD) Learning Framework</h3>
<p>
We introduce Trial-and-Demonstration (TnD), an interactive learning framework that incorporates corrective feedback with three components: student model <i>trials</i>, teacher model <i>demonstrations</i>, and a <i>reward</i> conditioned on the training trajectory of the model.
</p>
<p>
In this framework, the student model engages in production-based learning: to produce an initial utterance, followed by the teacher model generating its version of the text as a demonstration. For the student model to recognize the teacher's response as preferable and to facilitate learning, these language outputs are evaluated by a reward function, which is based on the competence of the student's language use that is expected for its developmental stage (i.e., training steps).
</p>

<h3>Components of the TnD Framework</h3>

<h4>The Student Model and Trials</h4>
<p>
We employ randomly initialized GPT-2 as the student model for our investigation into language acquisition, leveraging its causal language modeling (CLM) objective and inherent generative capabilities for production-based learning. To encourage the student model to attempt text production, it is essential to provide an appropriate context. In each trial, we prompt the student with the first 5 tokens from a natural sentence, asking it to generate the continuation as a <i>trial</i>.
</p>

<h4>The Teacher Model and Demonstrations</h4>
<p>
We utilize pre-trained language models as proxies for human language teachers. Employing language models as "caregivers" for language models offers two advantages: it eliminates the need for recruiting human participants across thousands of iterations, and we can consistently control the behavior of the teacher model across experiments.
</p>
<p>
The process of developing a teacher model is identical to the typical language model pre-training. We adopted the same GPT-2 architecture and pre-trained the model with the CLM objective. To generate a natural language <i>demonstration</i> for the student's <i>trial</i>, we prompt the pre-trained teacher model with the same 5 tokens used for the student model, thereby obtaining the teacher's completion of the sentence.
</p>

<h4>The Reward and Reward Model</h4>
<p>
Defining an effective reward in our context is challenging due to the absence of communication games and the lack of access to large-scale human preference annotations. Heuristic reward metrics do not consider the developmental trajectory of language models, which is critical for simulating language acquisition.
</p>
<p>
We treat the number of training steps as the neural model's "age". A language model that generates fluent text at 500 steps, which typically emerges around 5,000 steps, should be rewarded for its accelerated learning. Conversely, if the language production quality in the student remains the same at 50,000 steps, it should be penalized.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/BabySit/surprisal-main.png" alt="Learning curves for different models" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Learning curves of word acquisition for different models. The TnD approach accelerates word learning compared to other baselines, highlighting the importance of both trials and demonstrations in the learning process.</figcaption>
</figure>

<h3>Key Findings</h3>

<h4>Corrective Feedback Accelerates Neural Word Acquisition</h4>
<p>
Our experiments reveal that the TnD learning framework significantly accelerates word acquisition in training, outperforming other baselines. This acceleration is attributed to the critical roles of both trials and demonstrations in the learning process. With only teacher demonstrations, the student model acquires words faster than with the plain CLM baseline alone, though not as rapidly as when active trials are incorporated in the TnD framework.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/BabySit/vocab.png" alt="Effective vocabulary size growth" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">Growth of effective vocabulary size over training steps. The TnD model picks up a larger effective vocabulary much faster than other approaches.</figcaption>
</figure>

<h4>Corrective Feedback Helps Knowledge Distillation for Smaller Student Models</h4>
<p>
We investigated whether our approach could distill linguistic knowledge to smaller student models. We found that such efficient language learning can still be observed, even when the setting is translated to smaller models. Each TnD model outperforms the CLM baseline of the same size and even surpasses CLM baselines of large capacity in early steps.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/BabySit/smaller-models.png" alt="Performance on smaller models" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">TnD accelerates word acquisition for smaller student models. Each smaller TnD model outperforms its CLM counterpart of the same size.</figcaption>
</figure>

<h4>Teacher's Word Preferences in Demonstrations Affect Students</h4>
<p>
Our findings indicate that the teacher model's word choices significantly influence the efficiency of word acquisition by the student model. The absence of words from teacher demonstrations leads to slower learning speed for student models, as evidenced by a higher neural age of acquisition (nAoA), although the student models are ultimately able to learn these words from the corpus and their trials.
</p>

<h4>Practice Makes Perfect in Trials</h4>
<p>
We observe that the learning curves for certain words exhibit a pronounced correlation with the frequency of these words in trials. Our analysis reveals that the cumulative frequency of words encountered in trials plays a significant role in the acquisition of functional words and predicates. However, this significant contribution does not extend to nouns, indicating a potential impact of active trials on different parts of speech within the learning process.
</p>

<figure style="text-align: center; margin: 25px 0;">
    <img src="/img/BabySit/trial.png" alt="Word frequency in trials" style="max-width: 90%; height: auto;">
    <figcaption style="margin-top: 10px; font-style: italic;">The relationship between word frequency in trials and learning curves for selected words. There's a strong correlation between how often certain words appear in trials and how quickly they are learned.</figcaption>
</figure>

<h3>Conclusion</h3>
<p>
This research introduces a trial-and-demonstration (TnD) learning framework to examine the effectiveness of corrective feedback in neural word acquisition through systematically controlled experiments, assessing how the interplay between student trials and teacher demonstrations contributes to learning efficiency in neural language models.
</p>
<p>
We find that (1) TnD learning accelerates neural word acquisition across student models of different sizes; (2) the teacher's choices of words influence students' word-specific learning efficiency; and (3) a practice-makes-perfect effect is evident by a strong correlation between the frequency of words in trials and their respective learning curves. Our findings confirm the crucial role of interaction in efficient word learning with language models.
</p>
</div>
