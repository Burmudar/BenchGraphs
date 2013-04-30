import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib
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

    def hasXPlane(self):
        return self.x_near != self.x_far

    def hasYPlane(self):
        return self.y_near != self.y_far

    def hasZPlane(self):
        return self.z_near != self.z_far

    def hasAmountOfPoints(self):
        return self.amount_of_points > 0

    def createXLinspace(self):
        if not self.hasXPlane():
            raise BenchmarkDescriptionError("Cannot create X Linspace with no defined X Plane")
        return np.linspace(self.x_near, self.x_far, self.amount_of_points)

    def createYLinspace(self):
        if not self.hasYPlane():
            raise BenchmarkDescriptionError("Cannot create Y Linspace with no defined Y Plane")
        return np.linspace(self.y_near, self.y_far, self.amount_of_points)

DEJONGF1_TITLE = "DeJong F1"

def DeJongF1(x,y):
	return x**2 + y**2


class BenchmarkDescriptionBuilder:
    def __init__(self):
        self.NewInstance()
        return

    def NewInstance(self):
        self.benchmarkDescription = BenchmarkDescription()
        return self

    def XPlane(self,xNear,xFar):
        self.benchmarkDescription.x_near = xNear
        self.benchmarkDescription.x_far = xFar
        return self

    def YPlane(self,yNear, yFar):
        self.benchmarkDescription.y_near = yNear
        self.benchmarkDescription.y_far = yFar
        return self

    def ZPlane(self,zNear, zFar):
        self.benchmarkDescription.z_near = zNear
        self.benchmarkDescription.z_far = zFar
        return self

    def AmountOfPoints(self, amount):
        self.benchmarkDescription.amount_of_points = amount
        return self

    def DeJongF1(self):
        self.benchmarkDescription.benchTitle = DEJONGF1_TITLE
        self.benchmarkDescription.benchFn = DeJongF1
        return self

    def Build(self):
        builtDescription = self.benchmarkDescription
        self.NewInstance()
        return builtDescription

class BenchmarkResult:
    def __init__(self,X,Y,Z,bencTitle):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.BenchTitle
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

    def isValidDescription(self,description):
        if description is None:
            print 'In None - ' + str(description)
            return False
        if not description.hasXPlane():
            print 'In XPlane - ' + str(description)
            return False
        if not description.hasYPlane():
            print 'In YPlane - ' + str(description)
            return False
        if not description.hasAmountOfPoints():
            print 'In AmountOfPoints - ' + str(description)
            return False
        if description.benchFn is None:
            print 'In benchFn - ' + str(description)
            return False
        return True

    def runBenchmark(self,description):
        if not self.isValidDescription(description):
            raise BenchmarkDescriptionError(description, "The benchamrk description given was not valid")
        z = []
        x = description.createXLinspace()
        y = description.createYLinspace()
        x, y = np.meshgrid(x, y)
        for i in range(description.amount_of_points):
            val = description.benchFn(x[i],y[i])
            z.append(val)
        return BenchmarkResult(description.createXLinspace(), description.createXLinspace(), np.array(z), description.benchTitle)

class BenchmarkResultPlotter:
    def __init__(self):
        self.rstride = 1
        self.cstride = 1
        self.cmap = cm.jet
        self.linewidth = 0
        self.antialiased = False
        self.major_formatter = FormatStrFormatter('%.0f')
        matplotlib.use('PDF')
        return

    def createSurf(self, X, Y, Z):
       return ax.plot_surface(X, Y, Z, rstride = self.rstride, cstride = self.cstride, cmap = self.cm.jet, linewidth=self.linewidth, antialiased=self.antialiased) 

    def PlotResult(self,benchmarkResult, figureName=''):
       fig = plt.figure()
       ax = Axes3D(fig)
       surf = self.createSurf(benchmarkResult.X, benchmarkResult.Y, benchmarkResult.Y)
       ax.w_zaxis.set_major_formatter(self.major_formatter)
       if figureName == '':
           plt.savefig(benchmarkResult.BenchTitle)
       else:
           plt.savefig(figureName)
