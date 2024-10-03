---
layout: page
title: Papers
subtitle: 
---
 


<h3 style='margin-bottom: 10pt;'>Accepted Papers</h3>
<hr>
<p style='font-size: 11pt;'>
The list of accepted papers will appear here.
</p>

[//]: # ( <div class="card mb-3">)

[//]: # (  <div class="card-header font-weight-bold">)

[//]: # (  Reinforcement Learning of Diverse Skills using Mixture of Deep Experts)

[//]: # (  </div>)

[//]: # (  <div class="card-body">)

[//]: # (    <p class="card-text">)

[//]: # (    	<div class="row">)

[//]: # (    		<div class="col-9">)

[//]: # (    			<b>Authors:</b> Onur Celik · Aleksandar Taranovic · Gerhard Neumann)

[//]: # (    		</div>)

[//]: # (    		<div class="col-3">)

[//]: # (    			<div class="right">)

[//]: # (    				<a class="btn btn-primary" href="https://openreview.net/forum?id=zN0XIPH1WG" target="_blank" role="button">Paper Link</a>)

[//]: # (				</div>)

[//]: # (    		</div>)

[//]: # (    	</div>)

[//]: # (    </p>)

[//]: # (      <button type="button" class="collapsible">Abstract</button>)

[//]: # (		<div class="content">)

[//]: # (	      <p style='margin-top: 5pt;'>	)

[//]: # (            Agents that can acquire diverse skills to solve the same task have a benefit over other agents if e.g. unexpected environmental changes occur. However, Reinforcement Learning &#40;RL&#41; policies mainly rely on Gaussian parameterization, preventing them from learning multi-modal, diverse skills. In this work, we propose a novel RL approach for training policies that exhibit diverse behavior. To this end, we propose a highly non-linear Mixture of Experts &#40;MoE&#41; as the policy representation, where each expert formalizes a skill as a contextual motion primitive. The context defines the task, which can be for instance the goal reaching position of the agent, or changing physical parameters like friction. Given a context, our trained policy first selects an expert out of the repertoire of skills and subsequently adapts the parameters of the contextual motion primitive. To incentivize our policy to learn diverse skills, we leverage a maximum entropy objective combined with a per-expert context distribution that we optimize alongside each expert. The per-expert context distribution allows each expert to focus on a context sub-space and boost learning speed. However, these distributions need to be able to represent multi-modality and hard discontinuities in the environment's context probability space. We solve these requirements by leveraging energy-based models to represent the per-expert context distributions and show how we can efficiently train them using the standard policy gradient objective.)

[//]: # (				</p>)

[//]: # (		</div>)

[//]: # (  </div>)

[//]: # (</div>)



