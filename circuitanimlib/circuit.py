import warnings
import numpy as np

from manimlib.constants import *
from manimlib.mobject.geometry import *
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
        "is_polar" : False
    }
    pos_side = 0;
    neg_side = 0;

    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)

    def generate_points(self):

        pos = Line((-0.5,0,0),(-0.125,0,0))
        if (self.is_polar):
            wall1 = CubicBezier( [(-0.125,0.5,0),(0.083/2,0.166,0),(0.083/2,-0.166,0),(-0.125,-0.5,0)])
            wall1.shift(LEFT*0.125)
        else:
            wall1 = Line((-0.125,0.5,0),(-0.125,-0.5,0))

        wall2 = Line((0.125,0.5,0),(0.125,-0.5,0))
        neg = Line((0.125,0,0),(0.5,0,0))
        self.append_points(pos.get_points())
        self.append_points(wall1.get_points())
        self.append_points(wall2.get_points())
        self.append_points(neg.get_points())  



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
        line1 = Line((-0.5,0,0),(-0.375,0,0))
        arc1 = Arc(TAU/2, -TAU/2,radius=0.125)
        arc1.shift(0.25*LEFT)
        arc2 = Arc(TAU/2, -TAU/2,radius=0.125)
        arc3 = Arc(TAU/2, -TAU/2,radius=0.125)
        arc3.shift(0.25*RIGHT)
        line2 = Line((0.375,0,0),(0.5,0,0))

        self.append_points(line1.get_points())
        self.append_points(arc1.get_points())
        self.append_points(arc2.get_points())
        self.append_points(arc3.get_points())
        self.append_points(line2.get_points())

# Diode Enums
DIODE_DEFAULT = 0
DIODE_ZENER = 1;
DIODE_SCHOTTKY = 2;
class Diode(CircuitComponent):
    CONFIG = {
    "diode_type" : DIODE_DEFAULT
    }

    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)

    def generate_points(self):
        line1 = Line((-0.5,0,0),(-0.25,0,0))
        tri = WeirdShape([(-0.25,0.25,0),(-0.25,-0.25,0),(np.sin(PI/3)*0.5-0.25,0,0),(-0.25,0.25,0)])

        if(self.diode_type == DIODE_ZENER):
            l1 = Line((np.sin(PI/3)*0.5-0.1,0.3,0),(np.sin(PI/3)*0.5-0.25,0.3,0))
            l2 = Line((np.sin(PI/3)*0.5-0.25,0.3,0),(np.sin(PI/3)*0.5-0.25,-0.3,0))
            l3 = Line((np.sin(PI/3)*0.5-0.25,-0.3,0),(np.sin(PI/3)*0.5-0.4,-0.3,0))

            front = [*l1.get_points(),*l2.get_points(),*l3.get_points()]
        elif(self.diode_type == DIODE_SCHOTTKY):
            l0 = Line((np.sin(PI/3)*0.5-0.1,0.25,0),(np.sin(PI/3)*0.5-0.1,0.3,0))
            l1 = Line((np.sin(PI/3)*0.5-0.1,0.3,0),(np.sin(PI/3)*0.5-0.25,0.3,0))
            l2 = Line((np.sin(PI/3)*0.5-0.25,0.3,0),(np.sin(PI/3)*0.5-0.25,-0.3,0))
            l3 = Line((np.sin(PI/3)*0.5-0.25,-0.3,0),(np.sin(PI/3)*0.5-0.4,-0.3,0))
            l4 = Line((np.sin(PI/3)*0.5-0.4,-0.3,0),(np.sin(PI/3)*0.5-0.4,-0.25,0))


            front = [*l0.get_points(),*l1.get_points(),*l2.get_points(),*l3.get_points(),*l4.get_points()]
        else:
            l1 = Line((np.sin(PI/3)*0.5-0.25,0.3,0),(np.sin(PI/3)*0.5-0.25,-0.3,0))
            front =[*l1.get_points()]

        line2 = Line((np.sin(PI/3)*0.5-0.25,0,0),(0.5,0,0))
        self.append_points(line1.get_points())
        self.append_points(tri.get_points())
        self.append_points(front)
        self.append_points(line2.get_points())


class VoltageSource(CircuitComponent):
    CONFIG = {
    "is_dependent" : False
    }

    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)

    def generate_points(self):

        if(self.is_dependent):
            neg = Line((-0.5,0,0),(-0.35,0,0))
            neg_label = Line((-0.15,0.05,0),(-0.15,-0.05,0))
            pos_label1 = Line((0.15,0.05,0),(0.15,-0.05,0))
            pos_label2 = Line((0.1,0,0),(0.2,0,0))
            mid = Square(side_length=0.5)
            mid.rotate(PI/4)
            pos = Line((0.35,0,0),(0.5,0,0))        
        else:
            neg = Line((-0.5,0,0),(-0.25,0,0))
            neg_label = Line((-0.15,0.05,0),(-0.15,-0.05,0))
            pos_label1 = Line((0.15,0.05,0),(0.15,-0.05,0))
            pos_label2 = Line((0.1,0,0),(0.2,0,0))
            mid = Circle(radius=0.25)
            pos = Line((0.25,0,0),(0.5,0,0))

        self.append_points(neg.get_points())
        self.append_points(mid.get_points())
        self.append_points(neg_label.get_points())
        self.append_points(pos_label1.get_points())
        self.append_points(pos_label2.get_points())
        self.append_points(pos.get_points())



class CurrentSource(CircuitComponent):
    CONFIG = {
    "is_dependent" : False
    }

    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)


    def generate_points(self):

        if(self.is_dependent):
            neg = Line((-0.5,0,0),(-0.35,0,0))
            arr = Vector((0.3,0,0))
            arr.shift(LEFT*0.15)
            mid = Square(side_length=0.5)
            mid.rotate(PI/4)
            pos = Line((0.35,0,0),(0.5,0,0))           
        else:
            neg = Line((-0.5,0,0),(-0.25,0,0))
            arr = Vector((0.3,0,0))
            arr.shift(LEFT*0.15)
            mid = Circle(radius=0.25)
            pos = Line((0.25,0,0),(0.5,0,0))

        self.append_points(neg.get_points())
        self.append_points(mid.get_points())
        self.append_points(arr.get_points())
        self.append_points(arr.get_tip().get_points())
        self.append_points(pos.get_points())

class ACSource(CircuitComponent):

    def generate_points(self):

        verts = [(-1.5,-0.5,0),(0.3642-1.5,-0.5,0),(0.6358-1.5,0.5,0),(1-1.5,0.5,0),(1-1.5,0.5,0),(1.3634-1.5,0.5,0),(1.6358-1.5,-0.5,0),(2-1.5,-0.5,0),(2-1.5,-0.5,0),(2.3642-1.5,-0.5,0),(2.6358-1.5,0.5,0),(1.5,0.5,0)]
        sinewave = CubicBezier(verts)
        sinewave.rotate(-PI/2)
        sinewave.scale(0.1)
        mid = Circle(radius=0.25)
        neg = Line((-0.5,0,0),(-0.25,0,0))
        pos = Line((0.25,0,0),(0.5,0,0))

        self.append_points(neg.get_points())
        self.append_points(mid.get_points())
        self.append_points(sinewave.get_points())
        self.append_points(pos.get_points())


#Transistors
class Bjt(CircuitComponent):
    CONFIG = {
    "is_npn" : True,
    "collector_loc" : 0,
    "emitter_loc" : 0
    }

    

    def __init__(self,**kwargs):
        VMobject.__init__(self, **kwargs)
        

    def generate_points(self):

        
        base = Line((-0.5,0,0),(0,0,0))
        wall = Line((0,0.5,0),(0,-0.5,0))

        e_coord = (0,0,0)

        if(self.is_npn):
            emitter = Vector(direction = (0.5,-0.375,0))
            collector = Line((0,0.125,0),(0.5,0.5,0))
            emitter.shift(0.125*DOWN)

            e_coord = emitter.get_tip().get_points()[len(emitter.get_tip().get_points()) - 1]
        else:
            emitter = Vector(direction = (-0.5,-0.375,0))
            collector = Line((0,-0.125,0),(0.5,-0.5,0))
            emitter.shift(0.5*RIGHT + UP*0.5)

            e_coord = emitter.get_points()[0]

        
        c_coord = collector.get_points()[len(collector.get_points()) - 1]


        self.append_points(base.get_points())
        self.append_points(wall.get_points())
        self.append_points(collector.get_points())
        self.append_points(emitter.get_points())
        self.append_points(emitter.get_tip().get_points())

        #Getting point locations
        idx = 0
        for coord in self.get_points():
            if coord[0] == c_coord[0] and coord[1] == c_coord[1] and coord[2] == c_coord[2]:
                self.collector_loc = idx

            if coord[0] == e_coord[0] and coord[1] == e_coord[1] and coord[2] == e_coord[2]:
                self.emitter_loc = idx

            idx += 1




    def get_base(self):
        return self.get_points()[0]

    def get_emitter(self):
        return self.get_points()[self.emitter_loc]

    def get_collector(self):
        return self.get_points()[self.collector_loc]







class Mosfet(CircuitComponent):
    CONFIG = {
    "is_nmos" : True,
    "drain_loc" : 0,
    "source_loc" : 0
    }

    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)


    def generate_points(self):


        gate = Line((-0.5,0,0),(-0.125,0,0))
        wall1 = Line((-0.125,0.4,0),(-0.125,-0.4,0))
        wall2 = Line((0.125,0.5,0),(0.125,-0.5,0))
        top_line = Line((0.125,0.4,0),(0.5,0.4,0))
        bot_line = Line((0.125,-0.4,0),(0.5,-0.4,0))


        verts = []

        if(self.is_nmos):
            body = Vector(direction=(-0.375,0,0))
            body.shift(RIGHT*0.5)
            drain = Line((0.5,0.4,0),(0.5,0.75,0))
            source = Line((0.5,0,0),(0.5,-0.75,0))

            verts = [*bot_line.get_points(),*top_line.get_points(),*drain.get_points(),*body.get_tip().get_points(),*body.get_points()[::-1],*source.get_points()]
        else:
            body = Vector(direction=(0.375,0,0))
            body.shift(RIGHT*0.125)
            drain = Line((0.5,-0.4,0),(0.5,-0.75,0))
            source = Line((0.5,0,0),(0.5,0.75,0))

            verts = [*top_line.get_points(),*bot_line.get_points(),*drain.get_points(),*body.get_points(),*body.get_tip().get_points(),*source.get_points()]


        s_coord = source.get_points()[len(source.get_points()) - 1]
        d_coord = drain.get_points()[len(drain.get_points()) - 1]



        self.append_points(gate.get_points())
        self.append_points(wall1.get_points())
        self.append_points(wall2.get_points())

        self.append_points(verts)
        
        


        idx = 0
        for coord in self.get_points():

            if coord[0] == s_coord[0] and coord[1] == s_coord[1] and coord[2] == s_coord[2]:
                self.source_loc = idx

            if coord[0] == d_coord[0] and coord[1] == d_coord[1] and coord[2] == d_coord[2]:
                self.drain_loc = idx

            idx += 1


    def get_gate(self):
        return self.get_points()[0]

    def get_source(self):
        return self.get_points()[self.source_loc]

    def get_drain(self):
        return self.get_points()[self.drain_loc]


