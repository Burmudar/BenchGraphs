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

    def HasXPlane(self):
        return self.x_near != self.x_far

    def HasYPlane(self):
        return self.y_near != self.y_far

    def HasZPlane(self):
        return self.z_near != self.z_far

    def HasAmountOfPoints(self):
        return self.amount_of_points > 0

    def CreateXLinspace(self):
        if not self.HasXPlane():
            raise BenchmarkDescriptionError("Cannot create X Linspace with no defined X Plane")
        return np.linspace(self.x_near, self.x_far, self.amount_of_points)

    def CreateYLinspace(self):
        if not self.HasYPlane():
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
    def __init__(self,X,Y,Z,benchTitle):
        self.X = X
        self.Y = Y
        self.Z = Z
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

    def IsValidDescription(self,description):
        if description is None:
            return False
        if not description.HasXPlane():
            return False
        if not description.HasYPlane():
            return False
        if not description.HasAmountOfPoints():
            return False
        if description.benchFn is None:
            return False
        return True

    def RunBenchmark(self,description):
        if not self.IsValidDescription(description):
            raise BenchmarkDescriptionError(description, "The benchamrk description given was not valid")
        z = []
        x = description.CreateXLinspace()
        y = description.CreateYLinspace()
        x, y = np.meshgrid(x, y)
        for i in range(description.amount_of_points):
            val = description.benchFn(x[i],y[i])
            z.append(val)
        return BenchmarkResult(x,y, np.array(z), description.benchTitle)

class BenchmarkResultPlotter:
    def __init__(self):
        self.rstride = 1
        self.cstride = 1
        self.cmap = cm.jet
        self.linewidth = 0
        self.antialiased = False
        self.major_formatter = FormatStrFormatter('%.0f')
        return

    def PlotResult(self,benchmarkResult, figureName=''):
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
