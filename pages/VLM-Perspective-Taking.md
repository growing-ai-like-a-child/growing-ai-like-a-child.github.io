---
layout: page
title: Vision Language Models See What You Want but not What You See
subtitle: 
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="https://arxiv.org/abs/2410.00324" target="_blank">[paper]</a>
</div>
</center>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Abstract</h3>
<ul>
    Knowing others' intentions and taking others' perspectives are two core components of human intelligence that are considered to be instantiations of theory-of-mind. Infiltrating machines with these abilities is an important step towards building human-level artificial intelligence. Here, to investigate intentionality understanding and level-2 perspective-taking in Vision Language Models (VLMs), we constructed the IntentBench and PerspectBench, which together contains over 300 cognitive experiments grounded in real-world scenarios and classic cognitive tasks. We found VLMs achieving high performance on intentionality understanding but low performance on level-2 perspective-taking. This suggests a potential dissociation between simulation-based and theory-based theory-of-mind abilities in VLMs, highlighting the concern that they are not capable of using model-based reasoning to infer others' mental states.
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Key Findings</h3>
<ul>
    <li>VLMs demonstrate a clear dissociation between intentionality understanding and perspective-taking abilities</li>
    <li>All models perform above chance on intentionality understanding, with some achieving near-human accuracy</li>
    <li>No models exceed chance performance on perspective-taking tasks</li>
    <li>Intentionality understanding improves with model scale, while perspective-taking does not</li>
    <li>These abilities show no correlation in VLMs, suggesting they rely on different cognitive mechanisms</li>
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Introduction</h3>
<ul>
    Intentionality is the capacity of the mind to be directed toward, represent, or stand for objects, properties, or states of affairs for further executable actions. Understanding intentionality requires the ability to comprehend the mental content for action in another mind, which has been seen as a key distinction between humans and machines.
    
    Theory-of-mind (ToM) allows one to infer the mental content of others. Recent studies have shown that large language models (LLMs) and vision language models (VLMs) exhibit ToM abilities, raising questions about the nature of ToM and its implementation in artificial intelligence.
    
    This study examines the extent to which different ToM abilities require model-based reasoning by assessing VLMs' ability to perform intentionality understanding and level-2 perspective-taking.
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Methods</h3>
<ul>
    <h4>Datasets</h4>
    <ul>
        <li><strong>PerspectBench:</strong> 32 multi-image and 209 single-image format experiments based on classic cognitive tasks, particularly adaptations of the Three Mountain Task</li>
        <li><strong>IntentBench:</strong> 100 single-image format experiments based on real-world ambiguous social scenarios</li>
    </ul>
    
    <h4>Cognitive Experiments</h4>
    <ul>
        <li><strong>Level-2 Perspective-taking:</strong> Adapted from Piaget's Three Mountain Task, using groups of 3-4 elastic cans organized into different spatial patterns with a doll placed at different angles to test if models can take the perspective of another</li>
        <li><strong>Intentionality Understanding:</strong> Includes tests of action understanding using cartoon stimuli and real-world ambiguous scenarios</li>
    </ul>
    
    <h4>Models Evaluated</h4>
    <ul>
        <li><strong>Open-source VLMs with Multi-Image Reasoning:</strong> CogVLM Series, Qwen series, Blip2, LLaVA-Next</li>
        <li><strong>Closed-source VLMs with Multi-Image Reasoning:</strong> GPT series (GPT-4v, GPT-4-turbo, GPT-4o-mini), Gemini Series, Claude Series</li>
        <li><strong>Open-source VLMs with Single-Image Reasoning:</strong> InstructBlip Series, LLaVA Series</li>
    </ul>
    
    <h4>Human Baseline</h4>
    <ul>
        <li>22 college students proficient in English</li>
        <li>Questions required at least 80% of participants to answer correctly</li>
    </ul>
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Results</h3>
<ul>
    <h4>Overall Performance</h4>
    <ul>
        <li>Clear dissociation between model performance in intentionality understanding and perspective-taking</li>
        <li>All models performed above chance (approx. 25%) on intentionality understanding</li>
        <li>No model exceeded chance performance (approx. 29%) on perspective-taking</li>
        <li>Statistical analysis: paired samples t-test showed highly significant difference (t = 17.651, p = 2.62 × 10<sup>-19</sup>)</li>
    </ul>
    
    <h4>Relationship Between Model Performance and Model Size</h4>
    <ul>
        <li>Distinct trends in how abilities evolve as VLMs scale in size</li>
        <li>Intentionality understanding improves with model size (y = 0.0599x + 0.3925, r<sup>2</sup> = 0.2797)</li>
        <li>Perspective-taking performance remains stagnant or even declines slightly (y = -0.0057x + 0.1437, r<sup>2</sup> = 0.0176)</li>
    </ul>
    
    <h4>Intercorrelation Between Abilities</h4>
    <ul>
        <li>No significant correlation between intentionality understanding and perspective-taking</li>
        <li>Pearson correlation: 0.0252 (p = 0.882)</li>
        <li>Spearman correlation: 0.0115 (p = 0.946)</li>
    </ul>
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Discussion</h3>
<ul>
    VLMs appear proficient in intentionality understanding while performing significantly worse in perspective-taking. This suggests that intentionality understanding may not require explicit perspective-taking but can rely on contextual cues and associative learning.
    
    The relationship between model performance and size indicates a fundamental difference in the scalability of these abilities. Intentionality understanding improves with model size, suggesting that attention-based architectures are well-suited for this ability. In contrast, perspective-taking shows no improvement with scaling, suggesting it may require cognitive mechanisms not captured by existing architectures.
    
    Level-2 perspective-taking requires model-based reasoning—the ability to construct an internal model of the world. Our findings suggest this hallmark ability of human intelligence might remain absent in VLMs and may be fundamentally unacquirable within their current architectural framework.
    
    VLMs' performance on perspective-taking tasks mirrors children's egocentrism—consistently reporting what they see from their own perspective rather than considering others' perspectives. This suggests VLMs are egocentric rather than simply unable to process visual information.
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Conclusion</h3>
<ul>
    This study represents the first attempt to evaluate VLMs' performance in intentionality understanding and perspective-taking. The findings suggest that while current VLMs can infer intentions behind actions, they struggle with level-2 perspective-taking.
    
    This supports the hypothesis that intentionality understanding may not require mental simulation but could rely on knowledge-based reasoning. It also raises concerns that VLMs lack internal models for reasoning or cannot leverage them effectively for perspective-taking.
    
    These findings are crucial for understanding the nature of ToM abilities and their artificial implementations. Further research into the underlying mechanisms of this dissociation may provide insights into the limitations of current AI models and inform the development of better architectures for social reasoning.
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Figures</h3>
<ul>
    <h4>Figure 1: Example Experiments and Model Performances on PerspectBench</h4>
    <p><img src="/assets/images/case_6.pdf" alt="Example Experiments and Model Performances on PerspectBench" width="90%"></p>
    
    <h4>Figure 2: Example Experiments and Model Performances on IntentBench</h4>
    <p><img src="/assets/images/case_2.pdf" alt="Example Experiments and Model Performances on IntentBench" width="90%"></p>
    
    <h4>Figure 3: VLMs' Performance on IntentBench and PerspectBench As Compared to Human Baseline</h4>
    <p><img src="/assets/images/all_results.pdf" alt="VLMs' Performance on IntentBench and PerspectBench As Compared to Human Baseline" width="90%"></p>
    
    <h4>Figure 4: VLMs perform significantly better in intentionality understanding compared to perspective-taking</h4>
    <p><img src="/assets/images/violin_2.pdf" alt="VLMs perform significantly better in intentionality understanding compared to perspective-taking" width="60%"></p>
    
    <h4>Figure 5: Differential performance changes in intentionality understanding and perspective-taking in VLMs as their model sizes increase</h4>
    <p><img src="/assets/images/model_size_3.pdf" alt="Differential performance changes in intentionality understanding and perspective-taking in VLMs as their model sizes increase" width="90%"></p>
    
    <h4>Additional Examples of Vision Language Models Assessed with IntentBench</h4>
    <p><img src="/assets/images/case_1.pdf" alt="Additional Examples of Vision Language Models Assessed with IntentBench: Correct" width="80%"></p>
    <p><img src="/assets/images/case_5.pdf" alt="Additional Examples of Vision Language Models Assessed with IntentBench: Wrong" width="80%"></p>
</ul>
</div>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Authors</h3>
<ul>
    Qingying Gao<sup>1,*</sup>, Yijiang Li<sup>2</sup>, Haiyun Lyu<sup>3</sup>, Haoran Sun<sup>1</sup>, Dezhi Luo<sup>4,*</sup>, Hokin Deng<sup>5,*</sup>
    <br>
    <sup>1</sup>Johns Hopkins University, <sup>2</sup>University of California, San Diego, <sup>3</sup>University of North Carolina at Chapel Hill, <sup>4</sup>University of Michigan, <sup>5</sup>Carnegie Mellon University
    <br>
    <sup>*</sup> qgao14@jh.edu, ihzedoul@umich.edu, hokind@andrew.cmu.edu
</ul>
</div> 