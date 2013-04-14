import unittest
import opti_benchmarks

class TestBenchmarkFunctions(unittest.TestCase):

    def testBenchmarkDescriptionBuilderBuild(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.Build()
        self.assertIsNotNone(description)

    def testBenchmarkDescriptionXPlane(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.XPlane(-5,5).Build()
        self.assertEqual(description.x_near, -5)
        self.assertEqual(description.x_far, 5)
        return

    def testBenchmarkDescriptionYPlane(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.YPlane(-5,5).Build()
        self.assertEqual(description.y_near, -5)
        self.assertEqual(description.y_far, 5)
        return

    def testBenchmarkDescriptionZPlane(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.ZPlane(-5,5).Build()
        self.assertEqual(description.z_near, -5)
        self.assertEqual(description.z_far, 5)
        return

    def testBenchmarkDescriptionAmountOfPoints(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.AmountOfPoints(150).Build()
        self.assertEqual(description.amount_of_points, 150)
        return

    def testBenchmarkDescriptionBuilderNewInstance(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.AmountOfPoints(150).NewInstance().XPlane(-10,10).Build()
        self.assertNotEqual(description.amount_of_points, 150)
        self.assertEquals(description.x_near, -10)
        self.assertEquals(description.x_far, 10)
        return

    def testBenchmarkDescriptionWithDeJongF1(self):
        builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = builder.DeJongF1().Build()
        self.assertIsNotNone(description.benchFn)
        self.assertIsNotNone(description.benchTitle)
        self.assertEqual(description.benchTitle, opti_benchmarks.DEJONGF1_TITLE)
        self.assertEqual(description.benchFn, opti_benchmarks.DeJongF1)
        return

    def testBenchRunnerValidateDescription(self):
        runner = opti_benchmarks.BenchmarkRunner()
        self.assertRaises(opti_benchmarks.BenchmarkDescriptionError, runner.validateDescription, None)

if __name__ == "__main__":
    unittest.main()
