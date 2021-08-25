import warnings
import numpy as np

from manimlib.constants import *
from manimlib.mobject.geometry import *
from manimlib.mobject.types.vectorized_mobject import VMobject

#CONSTANTS
LOGIC_WIDTH = 2.0;
LOGIC_HEIGHT = 1.0;


class LogicGate(VMobject):
	CONFIG = {
	"inputA_loc" : 0,
	"inputB_loc" : 0,
	}

	def __init__(self,**kwargs):
		VMobject.__init__(self,**kwargs)


	def set_inputs(self,input1,input2):
		input1_coord = input1.get_points()[0]
		input2_coord = input2.get_points()[0]


        #Getting point locations
		idx = 0
		for coord in self.get_points():
			if coord[0] == input1_coord[0] and coord[1] == input1_coord[1] and coord[2] == input1_coord[2]:
				self.inputA_loc = idx

			if coord[0] == input2_coord[0] and coord[1] == input2_coord[1] and coord[2] == input2_coord[2]:
				self.inputB_loc = idx

			idx += 1







	def get_inputA(self):
		return self.get_points()[self.inputA_loc]

	def get_inputB(self):
		return self.get_points()[self.inputB_loc]

	def get_output(self):
		return self.get_points()[-1]



class AND(LogicGate):


	#input1 = Line()
	#input2 = Line()
	def generate_points(self):

		input1 = Line((-0.5,0.25,0),(-0.1,0.25,0))
		input2 = Line((-0.5,-0.25,0),(-0.1,-0.25,0))
		back = Line((-0.1,-0.5,0),(-0.1,0.5,0))
		top = Line((-0.1,0.5,0),(0.5,0.5,0))
		bot = Line((0.5,-0.5,0),(-0.1,-0.5,0))
		front = Arc(PI/2,-PI,radius=0.5)
		front.shift(RIGHT*0.5)
		output = Line((1,0,0),(1.5,0,0))

		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(back.get_points())
		self.append_points(top.get_points())
		self.append_points(front.get_points())
		self.append_points(bot.get_points())
		self.append_points(output.get_points())

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)

		








class NAND(LogicGate):

	def generate_points(self):


		input1 = Line((-0.5,0.25,0),(-0.1,0.25,0))
		input2 = Line((-0.5,-0.25,0),(-0.1,-0.25,0))
		back = Line((-0.1,-0.5,0),(-0.1,0.5,0))
		top = Line((-0.1,0.5,0),(0.5,0.5,0))
		bot = Line((0.5,-0.5,0),(-0.1,-0.5,0))
		front = Arc(PI/2,-PI,radius=0.5)
		front.shift(RIGHT*0.5)
		output = Line((1.125,0,0),(1.5,0,0))
		
		neg = Circle(radius=0.0625)
		neg.shift(RIGHT*(1 + 0.0625))


		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(back.get_points())
		self.append_points(top.get_points())
		self.append_points(front.get_points())
		self.append_points(bot.get_points())
		self.append_points(neg.get_points())
		self.append_points(output.get_points())

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)

		


# Drawing the OR,NOR,XOR & XNOR shapes were tricky
# used plenty of useful online sources such as

# Drawing perfect parabolas with quadratic bezier: https://www.math.fsu.edu/~rabert/TeX/parabola/parabola.html
# Aproximate quadratic with cubic bezier: https://stackoverflow.com/questions/3162645/convert-a-quadratic-bezier-to-a-cubic-one
# Drawing hald parabola: https://tex.stackexchange.com/questions/285255/drawing-half-a-parabola-using-pstricks-in-latex
class OR(LogicGate):

	def generate_points(self):

		#QP0 = -0.125,0.5
		#QP1 = 0.125,0
		#QP2 = -0.125,-0.5


		# QP0 = (-0.25,0.5,0)
		# QP1 = (0.25,0,0)
		# QP2 = (-0.25,-0.5,0)
		
		# CP0 = QP0
		# CP3 = QP2

		#CP1 = QP0 + 2/3*(QP1-QP0)
		#CP2 = QP2 + 2/3*(QP1-QP2)

		#CP1 = (-0.25,0.5,0) + 2/3*((0.25,0,0) - (-0.25,0.5,0)) = (0.083,0.0.166,0)
		#CP2 = (-0.25,-0.5,0) + 2/3* ( (0.25,0,0) -  (-0.25,-0.5,0) ) = (0.083,-0.166,0)


		back = [(-0.25,0.5,0),(0.083,0.166,0),(0.083,-0.166,0),(-0.25,-0.5,0)]


		# QP0 = (−0.45710678,0,0)
		# QP1 = (0.25,1,0)
		# QP2 = (0.95710678,0,0)


		# CP0 = QP0
		# CP1 = (0.01429774,2/3,0)
		# CP2 = (0.48570226,2/3,0)
		# CP3 = QP2

		input1 = Line((-0.5,0.4,0),(-0.16,0.4,0))
		input2 = Line((-0.5,-0.4,0),(-0.16,-0.4,0))
		output = Line((0.95710678,0,0),(1.5,0,0))
		verts2 = [(-0.45710678,0,0),(0.01429774,2/3,0),(0.48570226,2/3,0),(0.95710678,0,0)]
		topCurve = [(0.25,0.5,0),(0.48570226,0.5,0),(0.72140452,1/3,0),(0.95710678,0,0)]
		botCurve = [(0.25,-0.5,0),(0.48570226,-0.5,0),(0.72140452,-1/3,0),(0.95710678,0,0)]


		#topCurvePoints = topCurve.get_points()
		#print(topCurvePoints)
		top = Line((-0.25,0.5,0),(0.255,0.5,0))
		bot = Line((0.25,-0.5,0),(-0.25,-0.5,0))
		#self.add_cubic_bezier_curve_to(self,vert1[0],vert1[1])
		
		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(topCurve)
		self.append_points(botCurve[::-1])
		self.append_points(bot.get_points())
		self.append_points(back[::-1])
		self.append_points(top.get_points())
		self.append_points(output.get_points())

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)

		

class NOR(LogicGate):

	def generate_points(self):
		back = [(-0.25,0.5,0),(0.083,0.166,0),(0.083,-0.166,0),(-0.25,-0.5,0)]

		input1 = Line((-0.5,0.4,0),(-0.16,0.4,0))
		input2 = Line((-0.5,-0.4,0),(-0.16,-0.4,0))
		neg = Circle(radius=0.0625)
		neg.shift( (0.95710678+0.0625)*RIGHT)

		output = Line((0.95710678+0.125,0,0),(1.5,0,0))
		verts2 = [(-0.45710678,0,0),(0.01429774,2/3,0),(0.48570226,2/3,0),(0.95710678,0,0)]
		topCurve = [(0.25,0.5,0),(0.48570226,0.5,0),(0.72140452,1/3,0),(0.95710678,0,0)]
		botCurve = [(0.25,-0.5,0),(0.48570226,-0.5,0),(0.72140452,-1/3,0),(0.95710678,0,0)]

		top = Line((-0.25,0.5,0),(0.255,0.5,0))
		bot = Line((0.25,-0.5,0),(-0.25,-0.5,0))

		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(topCurve)
		self.append_points(botCurve[::-1])
		self.append_points(bot.get_points())
		self.append_points(back[::-1])
		self.append_points(top.get_points())

		self.append_points(neg.get_points())

		self.append_points(output.get_points())

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)

		


class XOR(LogicGate):
	def generate_points(self):

		back1= [(-0.25-0.1,0.5,0),(0.083-0.1,0.166,0),(0.083-0.1,-0.166,0),(-0.25-0.1,-0.5,0)] 
		back2= [(-0.25,0.5,0),(0.083,0.166,0),(0.083,-0.166,0),(-0.25,-0.5,0)]

		input1 = Line((-0.5,0.4,0),(-0.16-0.1,0.4,0))
		input2 = Line((-0.5,-0.4,0),(-0.16-0.1,-0.4,0))

		output = Line((0.95710678,0,0),(1.5,0,0))
		verts2 = [(-0.45710678,0,0),(0.01429774,2/3,0),(0.48570226,2/3,0),(0.95710678,0,0)]
		topCurve = [(0.25,0.5,0),(0.48570226,0.5,0),(0.72140452,1/3,0),(0.95710678,0,0)]
		botCurve = [(0.25,-0.5,0),(0.48570226,-0.5,0),(0.72140452,-1/3,0),(0.95710678,0,0)]

		top = Line((-0.25,0.5,0),(0.255,0.5,0))
		bot = Line((0.25,-0.5,0),(-0.25,-0.5,0))

		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(back1)

		
		
		self.append_points(topCurve)
		self.append_points(botCurve[::-1])
		self.append_points(bot.get_points())
		self.append_points(back2[::-1])
		self.append_points(top.get_points())

		self.append_points(output.get_points())	

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)

		



class XNOR(LogicGate):
	def generate_points(self):

		back1= [(-0.25-0.1,0.5,0),(0.083-0.1,0.166,0),(0.083-0.1,-0.166,0),(-0.25-0.1,-0.5,0)] 
		back2= [(-0.25,0.5,0),(0.083,0.166,0),(0.083,-0.166,0),(-0.25,-0.5,0)]

		input1 = Line((-0.5,0.4,0),(-0.16-0.1,0.4,0))
		input2 = Line((-0.5,-0.4,0),(-0.16-0.1,-0.4,0))
		neg = Circle(radius=0.0625)
		neg.shift( (0.95710678+0.0625)*RIGHT)

		output = Line((0.95710678+0.125,0,0),(1.5,0,0))
		verts2 = [(-0.45710678,0,0),(0.01429774,2/3,0),(0.48570226,2/3,0),(0.95710678,0,0)]
		topCurve = [(0.25,0.5,0),(0.48570226,0.5,0),(0.72140452,1/3,0),(0.95710678,0,0)]
		botCurve = [(0.25,-0.5,0),(0.48570226,-0.5,0),(0.72140452,-1/3,0),(0.95710678,0,0)]

		top = Line((-0.25,0.5,0),(0.255,0.5,0))
		bot = Line((0.25,-0.5,0),(-0.25,-0.5,0))

		self.append_points(input1.get_points())
		self.append_points(input2.get_points())
		self.append_points(back1)

		self.append_points(topCurve)
		self.append_points(botCurve[::-1])
		self.append_points(bot.get_points())
		self.append_points(back2[::-1])
		self.append_points(top.get_points())

		self.append_points(neg.get_points())

		self.append_points(output.get_points())

		self.set_inputs(input1,input2)
		self.shift(LEFT*0.5)	

		


class Buffer(LogicGate):

	def generate_points(self):

		verts = [(-0.5,0,0),(0,0,0),(0,-0.5,0),(np.sin(PI/3),0,0),(0,0.5,0)]
		output = Line((np.sin(PI/3),0,0),(1.5,0,0))

		self.set_points_as_corners( [*verts,verts[1]] )
		self.append_points(output.get_points())

		self.inputA_loc = 0		
		self.shift(LEFT*0.5)

		


class NOT(LogicGate):

	def generate_points(self):

		verts = [(-0.5,0,0),(0,0,0),(0,-0.5,0),(np.sin(PI/3),0,0),(0,0.5,0)]
		output = Line((np.sin(PI/3)+0.125,0,0),(1.5,0,0))
		neg = Circle(radius=0.0625)
		neg.shift( (np.sin(PI/3)+0.0625)*RIGHT)

		self.set_points_as_corners( [*verts,verts[1]] )
		self.append_points(neg.get_points())
		self.append_points(output.get_points())

		self.inputA_loc = 0
		self.shift(LEFT*0.5)

		

		