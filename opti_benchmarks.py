import types
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt

class BenchmarkDescription:
    def __init__(self):
        self.x_near = 0
        self.x_far = 0;
        self.y_near = 0
        self.y_far = 0
        self.z_near = 0;
        self.z_far = 0
        self.amount_of_points = 0
        self.benchFn = None
        self.benchTitle = ""
        return

    def __repr__(self):
        return ("<BenchmarkDescription xPlane["+ str(self.x_near) + "," + str(self.x_far) + "] - " +
        " yPlane[" + str(self.y_near) + "," + str(self.y_far) + "] - " +
        " zPlane[" + str(self.z_near) + "," + str(self.z_far) + "] - " +
        " Amount Of Points [" + str(self.amount_of_points) + "] -" +
        " Benchmark Title [" + str(self.benchTitle) + "] - " +
        " Benchmark Function [" + str(self.benchFn) + "]>")

    def has_x_plane(self):
        return self.x_near != self.x_far

    def has_y_plane(self):
        return self.y_near != self.y_far

    def has_z_plane(self):
        return self.z_near != self.z_far

    def has_amount_of_points(self):
        return self.amount_of_points > 0

    def create_x_linspace(self):
        if not self.has_x_plane():
            raise BenchmarkDescriptionError("Cannot create X Linspace with no defined X Plane")
        return np.linspace(self.x_near, self.x_far, self.amount_of_points)

    def create_y_linspace(self):
        if not self.has_y_plane():
            raise BenchmarkDescriptionError("Cannot create Y Linspace with no defined Y Plane")
        return np.linspace(self.y_near, self.y_far, self.amount_of_points)

def dejong_F1(x,y):
	return x**2 + y**2

#http://www.geatbx.com/docu/fcnindex-01.html
def ackley(x,y):
	a = 20
	b = 0.2
	c = 2* np.pi
	ndiv = 1.0 / 2.0
	ackleySum = -a * np.exp(-b * np.sqrt(ndiv*(x** 2 + y ** 2)))

	ackleySum -= np.exp(ndiv * (np.cos(c*x) + np.cos(c*y))) + a + np.exp(1)
	return ackleySum

def branin(x,y):
	a = 1
	b = 5.1 / (4 * np.pi) ** 2
	c = 5 / np.pi
	d = 6
	e = 10
	f = 1 / 8 * np.pi
	answ = a * (y - b * (x**2) + c*x - d)**2 + e * (1 - f)*np.cos(x) + e
	return answ

def camel(x,y):
	camelSum = (4 - 2.1 * (x ** 2) + (x ** 4.0)/3.0) * x ** 2 + (x * y) + (-4 + 4 * y **2)* y ** 2
	return camelSum

def dropwave(x,y):
	powsum = x ** 2 + y ** 2
	answ = 1 + np.cos(12 * np.sqrt(powsum))
	answ /= 0.5 * powsum + 2
	return answ

def easom(x,y):
	answ = -np.cos(x)*np.cos(y)*np.exp(-1 * ((x - np.pi) ** 2) - ((y - np.pi) ** 2))
	return answ

def general_rosenbrock(x,y):
	answ1 = x ** 2 - 10 * np.cos(2*np.pi*x)
	answ1 += y ** 2 - 10 * np.cos(2*np.pi*y)
	return 100 + answ1

def goldstein(x,y):
	answ = (1 + (( x + y + 1) ** 2) * (19 - 14 * x + ((3*x)**2) - 14 * y + 6 * x * y + ((3 * y) ** 2)))
	answ *= (30 + ((2 * x - 3 * y)**2) * (18 -32 * x +  (12 * x)**2 + 48 * y - 36 * x * y + (27 * y)**2))
	return answ  / 1000000.0

#http://www.geatbx.com/docu/fcnindex-01.html
def griewank(x,y):
	griewankSum1 = (x**2)/4000.0 + (y**2)/4000.0

	griewankSum2 = np.cos(x / np.sqrt(1)) * np.cos(y / np.sqrt(2))
	return griewankSum1 - griewankSum2 + 1

def himmelblau(x,y):
	answ1 = (x ** 2 + y - 11)**2 + (x + y ** 2 - 7) ** 2
	return answ1

def michalewicz(x,y):
	m = 20
	sumAnswx = np.sin(x) * (np.sin((1 - x ** 2) / np.pi))**(2 * m)
	sumAnswy = np.sin(y) * (np.sin((1 - y ** 2) / np.pi))**(2 * m)
	return -1 * (sumAnswx + sumAnswy) 

def rosenbrock(x,y):
	answ1 = 100 * ((x - y**2) ** 2) + (1-x)**2
	return answ1

def salomon(x,y):
	salomonSum1 = 0
	salomonSum1 += x ** 2
	salomonSum1 += y ** 2
	salomonSum1 = -np.cos(2*np.pi*np.sqrt(salomonSum1))
	salomonSum2 = 0
	salomonSum2 += (x ** 2)# + 1
	salomonSum2 += (y ** 2)# + 1
	salomonSum2 = 0.1 * np.sqrt(salomonSum2)+1
	return salomonSum1 + salomonSum2

SCHWEFEL_CONSTANT = 418.9829 * 2
def schwefel(x,y):
	schwefelSum = 0
	schwefelSum += (-1 * x)*np.sin(np.sqrt(abs(x)))
	schwefelSum += (-1 * y)*np.sin(np.sqrt(abs(y)))
	return SCHWEFEL_CONSTANT + schwefelSum

def rastrigin(x,y):
	rastriginSum = 0
	rastriginSum += x**2 + 10*np.cos(2*np.pi*x) + 10
	rastriginSum += y**2 + 10*np.cos(2*np.pi*y) + 10
	return rastriginSum

def shubert(x,y):
	answ1 = 0.0
	for i in range(4):
		answ1 += i * np.cos((i+1) * x + i)
	answ2 = 0.0
	for j in range(4):
		answ2 += i*np.cos((i+1) * y + i)
	return answ1 * answ2

def insert_values_into_matrix(matrix,value,row,index,timesToInsert):
	if matrix.size / 2 >= index + timesToInsert:
		for i in range(timesToInsert):
			matrix[row,index+i] = value
	

def create_dejong_F5_matrix():
	a = np.array([])
	a.resize(2,25)
	for i in range(2):
		value = -32
		for j in range(25):
			a[0,j] = value
			value = value + 16
			if j > 0 and (j+1) % 5 == 0:
				value = -32
				valueIndex = ((j + 1) / 5) - 1
				startIndex = valueIndex * 5
				insert_values_into_matrix(a,a[0,valueIndex],1,startIndex,5) 
	return a


DEJONGF5_MATRIX = create_dejong_F5_matrix()
def dejong_F5(x,y):
	sumj = 0;
	for j in range(25):
		sumi = 0
		sumi = (x - DEJONGF5_MATRIX[0,j])**6 + (y - DEJONGF5_MATRIX[1,j])**6
		sumj = sumj + (j + sumi)**-1
	return (0.002 + sumj)**-1



class BenchmarkDescriptionBuilder:
    def __init__(self):
        self.new_instance()
        return

    def new_instance(self):
        self.benchmarkDescription = BenchmarkDescription()
        return self

    def x_plane(self,xNear,xFar):
        self.benchmarkDescription.x_near = xNear
        self.benchmarkDescription.x_far = xFar
        return self

    def y_plane(self,yNear, yFar):
        self.benchmarkDescription.y_near = yNear
        self.benchmarkDescription.y_far = yFar
        return self

    def z_plane(self,zNear, zFar):
        self.benchmarkDescription.z_near = zNear
        self.benchmarkDescription.z_far = zFar
        return self

    def amount_of_points(self, amount):
        self.benchmarkDescription.amount_of_points = amount
        return self

    def _set_bench_properties(self, benchFn):
        self.benchmarkDescription.benchTitle = benchFn.__name__
        self.benchmarkDescription.benchFn = benchFn

    def ackley(self):
        self._set_bench_properties(ackley)
        return self

    def branin(self):
        self._set_bench_properties(branin)
        return self

    def camel(self):
        self._set_bench_properties(camel)
        return self

    def dropwave(self):
        self._set_bench_properties(dropwave)
        return self

    def easom(self):
        self._set_bench_properties(easom)
        return self

    def general_rosenbrock(self):
        self._set_bench_properties(general_rosenbrock)
        return self

    def goldstein(self):
        self._set_bench_properties(goldstein)
        return self

    def griewank(self):
        self._set_bench_properties(griewank)
        return self

    def himmelblau(self):
        self._set_bench_properties(himmelblau)
        return self

    def michalewicz(self):
        self._set_bench_properties(michalewicz)
        return self

    def rosenbrock(self):
        self._set_bench_properties(rosenbrock)
        return self

    def salomon(self):
        self._set_bench_properties(salomon)
        return self

    def schwefel(self):
        self._set_bench_properties(schwefel)
        return self

    def rastrigin(self):
        self._set_bench_properties(rastrigin)
        return self

    def shubert(self):
        self._set_bench_properties(shubert)
        return self

    def dejong_F1(self):
        self._set_bench_properties(dejong_F1)
        return self

    def dejong_F5(self):
        self._set_bench_properties(dejong_F5)
        return self

    def build(self):
        builtDescription = self.benchmarkDescription
        self.new_instance()
        return builtDescription

class BenchmarkResult:
    def __init__(self,X,Y,Z,benchTitle):
        self.X = X
        self.Y = Y
        self.Z = Z
        if isinstance(benchTitle, types.FunctionType):
            self.BenchTitle = benchTitle.__name__
        else:
            self.BenchTitle = benchTitle
        return

class BenchmarkDescriptionError(Exception):
    def __init__(self,benchDescription,msg):
        self.benchDescription = benchDescription
        self.msg = msg

    def __str__(self):
        return repr(self.benchDescription) + " - Msg: " + self.msg

class BenchmarkRunner:
    def __init__(self):
        return

    def is_valid_description(self,description):
        if description is None:
            return False
        if not description.has_x_plane():
            return False
        if not description.has_y_plane():
            return False
        if not description.has_amount_of_points():
            return False
        if description.benchFn is None:
            return False
        return True

    def run_benchmark(self,description):
        if not self.is_valid_description(description):
            raise BenchmarkDescriptionError(description, "The benchamrk description given was not valid")
        z = []
        x = description.create_x_linspace()
        y = description.create_y_linspace()
        x, y = np.meshgrid(x, y)
        for i in range(description.amount_of_points):
            val = description.benchFn(x[i],y[i])
            z.append(val)
        return BenchmarkResult(x, y, np.array(z), description.benchTitle)

class BenchmarkResultPlotter:
    def __init__(self):
        self.rstride = 1
        self.cstride = 1
        self.cmap = cm.jet
        self.linewidth = 0
        self.antialiased = False
        self.major_formatter = FormatStrFormatter('%.0f')
        return

    def plot_result(self,benchmarkResult, figureName=''):
       fig = plt.figure()
       ax = Axes3D(fig)
       surf = ax.plot_surface(benchmarkResult.X, benchmarkResult.Y, benchmarkResult.Z, rstride = self.rstride, cstride =
               self.cstride, cmap = self.cmap, linewidth=self.linewidth, antialiased=self.antialiased)
       ax.w_zaxis.set_major_formatter(self.major_formatter)
       fig.colorbar(surf, shrink=0.5, aspect=5)
       if figureName == '':
           plt.savefig(benchmarkResult.BenchTitle)
       else:
           plt.savefig(figureName)
