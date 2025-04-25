---
layout: page
title: OctoBERT
subtitle: World-to-Words: Grounded Open Vocabulary Acquisition through Fast Mapping in Vision-Language Models
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="http://arxiv.org/abs/2306.08685" target="_blank">[paper]</a>
</div>
</center>


<center>
    <div class="assets">
        <b><u>Martin Ziqiao Ma</u></b>*, Jiayi Pan*, Joyce Chai
    </div>
    <div class="assets">
        [ACL 2023 (Outstanding Paper Award)] 
        <a href="http://arxiv.org/abs/2306.08685" target="_blank">[paper]</a> 
        <a href="https://github.com/sled-group/world-to-words" target="_blank">[github]</a> 
        <a href="https://huggingface.co/sled-umich/OctoBERT-Trajectories" target="_blank">[huggingface]</a> 
    </div>
</center>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Abstract</h3>
<p>
The ability to connect language units to their referents in the physical world, referred to as <i>grounding</i>, is crucial to learning and understanding grounded meanings of words. 
While humans demonstrate fast mapping in new word learning, it remains unclear whether modern vision-language models can truly represent language with their grounded meanings, and how grounding may further bootstrap new word learning.
To this end, we introduce Grounded Open Vocabulary Acquisition (<code>GOVA</code>) to examine grounding and bootstrapping in open-world language learning.
As an initial attempt, we propose object-oriented BERT (<code>OctoBERT</code>), a novel visually-grounded language model by pre-training on image-text pairs highlighting grounding as an objective. 
Through extensive experiments and analysis, we demonstrate that <code>OctoBERT</code> is a more coherent and fast grounded word learner, and that the grounding ability acquired during pre-training helps the model to learn unseen words more rapidly and robustly.
</p>

<h3>Introduction</h3>
<p>
Language is learned through sensorimotor experience in the physical world.
The ability to connect language units to their referents in the physical world, <i>i.e.</i> <i>(referential) grounding</i>, plays an important role in learning and understanding grounded meanings of words. 
As shown in Figure 1, a human reader would easily ground noun phrases to the corresponding entities captured in the image.
Even when the term "<code>incinerator</code>" is new to human learners, they can still locate the object of interest through the language and visual context, and acquire its meaning.
In fact, this ability to bootstrap new word learning with only minimal information, known as <i>fast mapping</i>, is demonstrated abundantly in cognitive literature on human language acquisition.
</p>

<figure>
    <img src="/img/OctoBERT/formulation.pdf" alt="Word mapping example showing grounding of the term incinerator">
    <figcaption>Figure 1: Even when the term "<code>incinerator</code>" (highlighted yellow) is new to human learners, they can still locate the most likely referent (indicated by the yellow bounding box) in the perceived world by grounding.</figcaption>
</figure>

<p>
Recently, there has been a substantial effort on pre-training vision-language models (VLMs). 
Despite the exciting performance of these models on a variety of downstream vision and language tasks, it remains unclear whether these models can truly understand or produce language with their grounded meanings in the perceived world, and how grounding may further bootstrap new word learning.
These questions are of interest from both a scientific and an engineering point of view.
</p>

<h3>Grounded Open Vocabulary Acquisition (<code>GOVA</code>)</h3>
<p>
We introduce Grounded Open Vocabulary Acquisition (<code>GOVA</code>), a scalable formulation to examine grounding and bootstrapping in open-world language learning.
In this formulation, language learning is a combination of learning to predict a word in a linguistic context as well as learning to ground the word in the physical world.
</p>

<figure>
    <img src="/img/OctoBERT/refcloze.pdf" alt="Word grounding task example">
    <figcaption>Figure 2: An instance of the word grounding task. Models are tasked to predict the missing word "<code>boat</code>" and localize the corresponding smaller yellow boat in the image coherently.</figcaption>
</figure>

<p>
Under this formulation, we explore the framework in which the model first acquires the grounding ability during pre-training, and then transfers this ability to learn unseen words without grounding supervision.
</p>

<figure>
    <img src="/img/OctoBERT/few-shot.pdf" alt="Few-shot new word learning framework">
    <figcaption>Figure 3: An illustration of the few-shot new word learning paradigm. The model first pre-trains on a grounding dataset with a set of base words (V_seen), and then attempts to acquire a set of unseen words (V_unseen) in a small number of raw text-image pairs.</figcaption>
</figure>

<h3>Object-Oriented BERT (<code>OctoBERT</code>)</h3>
<p>
As an initial step, we developed object-oriented BERT (<code>OctoBERT</code>), a novel visually grounded language model motivated by recent advances in detection transformers (DETR).
Compared to many existing VLMs, <code>OctoBERT</code> performs language modeling upon explicit object representations.
The model first acquires the ability to ground during pre-training, and then transfers this intrinsic ability to learn unseen words when grounded supervision is no longer available.
</p>

<figure>
    <img src="/img/OctoBERT/model.pdf" alt="OctoBERT model architecture">
    <figcaption>Figure 4: An overview of <code>OctoBERT</code>, a visually grounded language model pre-trained with three objectives: masked language modeling (MLM), object localization (OL), and grounding through word-region alignment (WRA).</figcaption>
</figure>

<h3>Key Findings</h3>
<p>
Our empirical results show that learning to map words to their referents plays a significant role in grounded word acquisition. By pre-training with fine-grained word-object mappings, <code>OctoBERT</code> demonstrates stronger performance in learning grounded meanings of words, both seen and unseen, yet with orders of magnitude fewer data compared to other competitive VLM baselines.
</p>

<figure>
    <img src="/img/OctoBERT/grounding.pdf" alt="Word-agnostic grounding example">
    <figcaption>Figure 5: Although the word "<code>elephant</code>" is unseen to <code>OctoBERT</code>, the model is still able to localize the object in the image referred to by the <code>MASK</code>.</figcaption>
</figure>

<p>
The pre-trained model can further provide a foundation for efficient learning of new grounded words with a few examples. We further present an in-depth analysis to understand potential predictors of VLMs in word learning, which demonstrates intriguing behaviors in comparison to human language learning.
</p>

<figure>
    <img src="/img/OctoBERT/multiclass.pdf" alt="Graph showing performance on multi-class incremental learning">
    <figcaption>Figure 6: The log G-PPL (All-Protocol) of seen and unseen words in multi-class incremental learning, each unseen word with a sample size ranging from 8 to 32.</figcaption>
</figure>

<h3>Conclusion</h3>
<p>
The connection between language and their referents captures the grounded meaning of words, and an explicit treatment is key to empowering efficient open-world language learning abilities in humans and AI agents. This work introduces Grounded Open Vocabulary Acquisition (<code>GOVA</code>), a scalable formulation to examine grounding and fast mapping in open-world grounded language learning. Our findings pave the way for future research in grounded language learning in the open world.
</p>
</div>
