import warnings
import numpy as np

from manimlib.constants import *
from manimlib.mobject.geometry import Line
from manimlib.mobject.types.vectorized_mobject import VMobject


class WeirdShape(VMobject):
    def __init__(self, points, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(points)

class Circuit(VMobject):

    def __init__(self,**kwargs):
        self.ps = []
        self.bs = []
        VMobject.__init__(self,**kwargs)


    def connect(self,point1,point2,pin_top=False):
        if(pin_top):
            self.ps.append([point1,(point2[0],point1[1],0),point2])
        else:
            self.ps.append([point1,(point1[0],point2[1],0),point2])

    def connect_right_to_left(self,point1,point2):
        target_point = (point2[0],point1[1]-1.5,0)

        self.connect(point1,target_point)
        self.connect(target_point,point2)

    def render(self):
        for p in self.ps:
            self.append_points(WeirdShape(p).get_points());


class CircuitComponent(VMobject):


    def get_left(self):
        return self.get_points()[0];

    def get_right(self): 
        return self.get_points()[len(self.get_points()) - 1];



class Resistor(CircuitComponent):
    CONFIG = {
        "color" : WHITE,
        "points": [(-0.5,0,0),(-0.3125,0,0),(-0.25,-0.25,0),(-0.125,0.25,0),(0,-0.25,0),(0.125,0.25,0),(0.25,-0.25,0),(0.3125,0,0),(0.5,0,0)]
    }
    def __init__(self, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(self.CONFIG["points"])   

class Capacitor(CircuitComponent):
    CONFIG = {
        "color" : WHITE

    }
    pos_side = 0;
    neg_side = 0;

    def generate_points(self):
        neg = Line((-0.5,0,0),(-0.125,0,0))
        neg_side = (-0.5,0,0);
        wall1 = Line((-0.125,0.5,0),(-0.125,-0.5,0))
        wall2 = Line((0.125,0.5,0),(0.125,-0.5,0))
        pos = Line((0.125,0,0),(0.5,0,0))
        pos_side = (0.5,0,0)
        self.append_points(neg.get_points())
        self.append_points(wall1.get_points())
        self.append_points(wall2.get_points())
        self.append_points(pos.get_points())  


class Battery(CircuitComponent):
    CONFIG = {
        "color" : WHITE
    }

    def generate_points(self):
        neg = Line((-0.5,0,0),(-0.125,0,0))
        wall1 = Line((-0.125,0.25,0),(-0.125,-0.25,0))
        wall2 = Line((0.125,0.5,0),(0.125,-0.5,0))
        pos = Line((0.125,0,0),(0.5,0,0))
        self.append_points(neg.get_points())
        self.append_points(wall1.get_points())
        self.append_points(wall2.get_points())
        self.append_points(pos.get_points())    

class Inductor(CircuitComponent):
    def generate_points(self):
        line1 = Line((-1,0,0),(-0.75,0,0))
        arc1 = Arc(TAU/2, -TAU/2,radius=0.25)
        arc1.shift(0.5*LEFT)
        arc2 = Arc(TAU/2, -TAU/2,radius=0.25)
        arc3 = Arc(TAU/2, -TAU/2,radius=0.25)
        arc3.shift(0.5*RIGHT)
        line2 = Line((0.75,0,0),(1,0,0))

        self.append_points(line1.get_points())
        self.append_points(arc1.get_points())
        self.append_points(arc2.get_points())
        self.append_points(arc3.get_points())
        self.append_points(line2.get_points())


class Diode(CircuitComponent):

    def generate_points(self):
        line1 = Line((-0.5,0,0),(0,0,0))
        arrTip = ArrowTip(start_angle=0)
        line2 = Line((0.5,0,0),(1,0,0))
        self.append_points(line1.get_points())
        self.append_points(arrTip.get_points())
        self.append_points(line2.get_points())


class Bjt(CircuitComponent):
    CONFIG = {
    "is_npn" : True
    }

    base_loc = 0;
    collector_loc = 0;
    emitter_loc = 0;


    def generate_points(self):

        #TODO add pnp
        base = Line((-0.5,0,0),(0,0,0));
        wall = Line((0,0.5,0),(0,-0.5,0))
        collector = Line((0,0.125,0),(0.5,0.5,0))
        #diode = ArrowTip(start_angle=-0.643501109)
        emitter = Vector(direction = (0.5,-0.375,0));
        emitter.shift(0.125*DOWN)

        self.append_points(base.get_points())
        self.append_points(wall.get_points())
        self.append_points(collector.get_points())
        self.append_points(emitter.get_points())
        self.append_points(emitter.get_tip().get_points())



#WIP
class Mosfet(CircuitComponent):
    def generate_points(self):
        gate = Line((-0.5,0,0),(-0.125,0,0))
        wall1 = Line((-0.125,0.4,0),(-0.125,-0.4,0))
        wall2 = Line((0.125,0.5,0),(0.125,-0.5,0))
        body = Vector(direction=(-0.325,0,0))
        body.shift(RIGHT*0.5)
        top_line = Line((0.125,0.4,0),(0.5,0.4,0))
        bot_line = Line((0.125,-0.4,0),(0.5,-0.4,0))
        drain = Line((0.5,0.4,0),(0.5,0.75,0))
        source = Line((0.5,0,0),(0.5,-0.75,0))

        #line4 = Line((0.125,0.5,0),(0.625,0.5,0))
        self.append_points(gate.get_points())
        self.append_points(wall1.get_points())
        self.append_points(wall2.get_points())
        self.append_points(body.get_tip().get_points())
        self.append_points(body.get_points())
        self.append_points(top_line.get_points())
        self.append_points(bot_line.get_points())
        self.append_points(drain.get_points())
        self.append_points(source.get_points())
        #self.append_points(line4.get_points())   
