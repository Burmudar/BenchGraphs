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
        return

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
