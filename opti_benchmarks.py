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
        return ("<BenchmarkDescription xPlane["+ self.x_near + "," + self.x_far + "] - " +
        " yPlane[" + self.y_near + "," + self.y_far + "] - " +
        " zPlane[" + self.z_near + "," + self.z_far + "] - " +
        " Amount Of Points [" + self.amount_of_points + "] -" +
        " Benchmark Title [" + self.benchTitle + "] - " +
        " Benchmark Function [" + self.benchFn + "]>")

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
        return self.benchmarkDescription

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

    def validateDescription(self,description):
        if description is None:
            raise BenchmarkDescriptionError(description,"Description cannot be None")
        if  description.benchFn is None:
            raise BenchmarkDescriptionError(description,"Cannot run benchmark when BenchFn is None")

    def runBenchmark(self,description):
        print "Checking BenchmarkDescription"
        self.validateDescription(description)
        return None
