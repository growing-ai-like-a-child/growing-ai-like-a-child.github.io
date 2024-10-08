---
layout: page
title: Vision Language Models Know Law of Conservation without Understanding More-or-Less
subtitle:  
---
[//]: # (<h3 style='margin-bottom: 10pt;'>Topics</h3>)
<center>
<div class="assets">
<a href="https://arxiv.org/abs/2410.00332" target="_blank">[paper]</a>
</div>
</center>

<div class='description' style='font-size: 11pt;margin-bottom: 10pt'>
<h3>Abstract</h3>
<ul>
    Conservation is a critical milestone of cognitive development considered to be supported by both the understanding of quantitative concepts and the reversibility of mental operations. To assess whether this critical component of human intelligence has emerged in Vision Language Models, we leverage the ConserveBench from CogDevelop2K, a data-intensive cognitive experiment benchmark for assaying the developmental trajectory of machine intelligence. The battery includes over 350 questions across four dimensions of physical quantities: volume, solid quantity, length, and number. The former two involve only transformational tasks, whereas the latter two also involve non-transformational tasks assessing the understanding of quantitative concepts alone. Surprisingly, we find that while VLMs are generally capable of conserving, they tend to fail at non-transformational tasks which success is typically considered to be entailed by the ability to conserve. This implies that the law of conservation, at least in concrete domains, may exist without corresponding conceptual understanding of quantity.
</ul>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">VLMs behaviors on Number, Length, Solid Quanity, and Liquid Volume experiments on ConserveBench</p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/conserve_case_1.jpg">
</figure>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">Sets of 3, 5, 7 coins in both reality and virtual display were tested. The same number of coins are placed on two lines with different distance between the coins. VLMs can not count the correct number of coins in this situation. In virtual setting, VLMs have no problems with 3 circles but has problem choosing the correct answer. When the number of circles is 5 or 7, VLM can not count the correct number of circles.</p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/conserve_case_2.jpg">
</figure>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">VLMs performance on Length experiments on ConserveBench. As shown in B), VLM can not verify the length of two lines placed as diagonal and vertical. D) shows that VLM has difficulty verifying the length of lines placed in perpendicular relation. A) and C) show that VLMs have the ability to verify parallel lines in a virtual setting.</p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/case_4.jpg">
</figure>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">VLMs performance on Number experiments on ConserveBench. Sets of 3 to 13 trapezoids in both reality and virtual display are tested. The same number of trapezoids has been placed on two lines with different distance between the trapezoids. VLMs can correctly count the number of 3 trapezoids. Yet for 4 to 13, VLMs count the number of trapezoids wrong. </p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/case_3.jpg">
</figure>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">VLMs performance on Number experiments on ConserveBench with modified way of asking question. Sets of 3 to 13 trapezoids in both reality and virtual display are tested. </p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/conserve_case_5.jpg">
</figure>
<hr class="small" style="border-width: 0; height: 0px; background-color: white; padding-top: 20px; padding-bottom: 20px;">

<p style="font-family: 'Times New Roman', Times, serif; font-size: 14pt; line-height: 1.2;">We observe that GPT-4o achieve very high performance on law of conservation tasks whereas fail badly on quantity understanding, Number and Length, tasks.</p>
<figure>
    <img src="/img/CogDevelop2K/System2ReasoningatScale_Conservation/conservation.jpg">
</figure>

</div>
