---
layout: page
title: Docs
menubar_toc: true
toc_title: Custom Title
show_sidebar: false
hide_hero: true
---

## Introduction

Welcome to circuitanim, an extension to 3b1b's manim python library. Much like manim simplifies animating mathematical obects, circuitanim simplifies animating circuits. As seen below, with only a few lines of code, you can render a complete circuit scene.

<!-- blank line -->
<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="graphics/videos/DrawCircuit_poster.jpg">
    <source src="graphics/videos/DrawCircuit.mp4" type="video/mp4">
    <!--<source src="path/to/video.ogg" type="video/ogg">
    <source src="path/to/video.webm" type="video/webm"> -->
  </video> 
</figure>
<!-- blank line -->


<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>
<link rel="stylesheet" href="graphics/prettify.css" />

<pre class ="prettyprint lang-py">
class DrawCircuit(Scene):
  def construct(self):
    res = Resistor()
    cap = Capacitor()
    batt = Battery()

    batt.rotate(PI/2)
    cap.rotate(-PI/2)
    cap.shift(RIGHT*3)
    res.shift(2*LEFT + UP*3)
    batt.shift(3*LEFT)


    circ = Circuit()
    circ.connect(batt.get_right(),res.get_left())
    circ.connect(res.get_right(),cap.get_left(),pin_top=True)
    circ.connect_right_to_left(cap.get_right(),batt.get_left())
    circ.render()
    
    self.play(ShowCreation(batt),ShowCreation(res),ShowCreation(cap),ShowCreation(circ),run_time=3)
</pre>



## Set Up

For up-to-date installation, see the github readme which can be found [here](https://github.com/weras2/circuitanim).  



## Basic Electrical Components 

### Capacitor

### Diode 

### Inductor 

### Resistor






## Power Sources 

### Battery 




### Current Source

### Voltage Source



## Transistors 

{% include notification.html 
message=" Note: Transistors have more than two terminals so avoid the use of get_left() and get_right(). Instead, use methods specific to the transistor type"  %}



### BJTs 
<pre class ="prettyprint lang-py">
class Bjt(CircuitComponent)
</pre>

<code class = "prettyprint lang-py">get_base()</code> Returns coordinates of base terminal
<code class = "prettyprint lang-py">get_collector()</code> Returns coordinates of collector terminal
<code class = "prettyprint lang-py">get_emitter()</code> Returns coordinates of emitter terminal


### Mosfets
