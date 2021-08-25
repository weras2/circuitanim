#!/usr/bin/env python

from manimlib.imports import *

#from manimlib.mobject.geometry import *;

from circuitanimlib.circuit import *

from circuitanimlib.logic import *

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


#Capacitor
#Diode
#Inductor
#Resistor

#Battery
#VoltageSource
#CurrentSource

#Bjt
#Mosfet





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




class Transistors(Scene):
    def construct(self):
        tran1 = Mosfet()
        tran2 = Mosfet(is_nmos=False)

        tran1.shift(LEFT*2)
        tran2.shift(RIGHT*2)

        self.play(ShowCreation(tran1),ShowCreation(tran2))


class Create(Scene):
    def construct(self):

        obj = CurrentSource(is_dependent=True)

        self.play(ShowCreation(obj))

class Logic(Scene):

    def construct(self):

        pad = 0.5;
        obj = AND()
        obj1 = NAND()
        obj2 = OR()
        obj3 = NOR()
        obj4 = XOR()
        obj5 = XNOR()
        obj6 = Buffer()
        obj7 = NOT()

        obj.shift(2*(pad+LOGIC_WIDTH)*LEFT + 2*(pad+LOGIC_HEIGHT)*UP)
        obj1.shift(2*(pad+LOGIC_WIDTH)*LEFT + (pad+LOGIC_HEIGHT)*UP)

        obj2.shift((LOGIC_WIDTH)*LEFT + 2*(pad+LOGIC_HEIGHT)*UP)
        obj3.shift((LOGIC_WIDTH)*LEFT + (pad+LOGIC_HEIGHT)*UP)

        obj4.shift((LOGIC_WIDTH)*RIGHT + 2*(pad+LOGIC_HEIGHT)*UP)
        obj5.shift((LOGIC_WIDTH)*RIGHT + (pad+LOGIC_HEIGHT)*UP)

        obj6.shift(2*(pad+LOGIC_WIDTH)*RIGHT + 2*(pad+LOGIC_HEIGHT)*UP)
        obj7.shift(2*(pad+LOGIC_WIDTH)*RIGHT + (pad+LOGIC_HEIGHT)*UP)     




        self.play(ShowCreation(obj),
            ShowCreation(obj1),
            ShowCreation(obj2),
            ShowCreation(obj3),
            ShowCreation(obj4),
            ShowCreation(obj5),
            ShowCreation(obj6),
            ShowCreation(obj7))



class Testing(Scene):

    def construct(self):

        obj = Inductor()
        obj.scale(4)
        self.play(ShowCreation(obj))


class LCircuit(Scene):

    def construct(self):

        obj1 = NOT()

        
        obj2 = Buffer()

        obj2.shift(1.5*LOGIC_WIDTH*RIGHT + LOGIC_HEIGHT*DOWN)

        circ = Circuit()

        circ.connect(obj1.get_output(),obj2.get_inputA())

        circ.render()

        self.play(ShowCreation(obj1),ShowCreation(circ),ShowCreation(obj2))
