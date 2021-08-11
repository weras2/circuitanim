---
layout: page
title: Docs
menubar_toc: true
toc_title: Docs Table of Contents
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
from manimlib.imports import *
from circuitanimlib.circuit import *
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

For up-to-date installation, see the Github readme which can be found [here](https://github.com/weras2/circuitanim).  

## Driver Class

### Circuit
<pre class ="prettyprint lang-py">
class Circuit(VMobject)
</pre>
The circuit class is what glues together all of the electrical components in a scene. 

#### Methods
- <code class = "prettyprint lang-py">connect(point1,point2,pin_top=False)</code> Method for connecting electrical components, preferably from left to right. The function takes in two terminal coordinates to connect. The terminal coordinates can be found using methods specific to the electrical component. The optional parameter <code class = "prettyprint lang-py">pin_top=False</code> just specifies whether the anchor point of the 90 degree bend should lie in the horizontal axis of the first point (<code class = "prettyprint lang-py">False</code>) or second point(<code class = "prettyprint lang-py">True</code>). <br/>
- <code class = "prettyprint lang-py">connect_right_to_left(point1,point2)</code> Method for connecting electrical components, specifically designed for when the first terminal (point) lies to the right of the second terminal. <br/>
- <code class = "prettyprint lang-py">render()</code> Adds all points onto the Mobject for rendering.

## Basic Electrical Components 

### Capacitor

### Diode 

### Inductor 

### Resistor


## Logic Gates

<div class="columns">
    <div class="column is-4">
        {% include index.md ratio="is-16by9" link="graphics\logic\and.jpg" alt="Example image" %}
    </div>
    <div class="column is-8">
        <p>This is a page with the image-modal included. The page needs to be a .html page instead of markdown.</p>
        <p>You can click on the image to see a larger version in a modal.</p>
        <p>The below snippet shows an example of how to include the image modal.</p>
    </div>
</div>



## Power Sources 

### Battery 

### Current Source

### Voltage Source



## Transistors 
{% include notification.html 
message=" Note: Transistors have more than two terminals so avoid the use of get_left() and get_right(). Instead, use methods specific to the transistor type"%}



### BJTs 
<pre class ="prettyprint lang-py">
class Bjt(CircuitComponent)
</pre>

By default, the bjt is rendered as npn. If you would like to render a pnp bjt, then in the constructor just pass in the optional parameter <code class = "prettyprint lang-py">is_pnp</code> and set it to <code class = "prettyprint lang-py">False</code> like so <code class = "prettyprint lang-py">Bjt(is_pnp=False)</code>. 

#### Methods
- <code class = "prettyprint lang-py">get_base()</code> Returns coordinates of the base terminal <br/>
- <code class = "prettyprint lang-py">get_collector()</code> Returns coordinates of the collector terminal <br/>
- <code class = "prettyprint lang-py">get_emitter()</code> Returns coordinates of the emitter terminal <br/>


### Mosfets

By default, the mosfet is rendered as nmos. If you would like to render it as pmos,  then in the constructor just pass in the optional parameter <code class = "prettyprint lang-py">is_nmos</code> and set it to <code class = "prettyprint lang-py">False</code> like so <code class = "prettyprint lang-py">Mosfet(is_nmos=False)</code>.

#### Methods
- <code class = "prettyprint lang-py">get_drain()</code> Returns coordinates of the drain terminal <br/>
- <code class = "prettyprint lang-py">get_gate()</code> Returns coordinates of the gate terminal <br/>
- <code class = "prettyprint lang-py">get_source()</code> Returns coordinates of the source terminal <br/>
