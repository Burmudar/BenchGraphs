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
    def __init__(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.z = Z
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
        return None
