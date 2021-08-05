#!/usr/bin/env python

from manimlib.imports import *

from manimlib.mobject.geometry import TipableVMobject;

from circuitanimlib.circuit import *

# To watch one of these scenes, run the following:
# python -m manim example.py DrawCircuit -pl
#
# Use the flag -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)



#Resistor
#Capacitor
#Battery
#Diode
#Bjt
#Mosfet (WIP)




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

