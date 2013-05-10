import unittest
import numpy as np
import opti_benchmarks

class TestBenchmarkFunctions(unittest.TestCase):

    def testBenchmarkDescriptionBuilderbuild(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.build()
        self.assertIsNotNone(description)

    def testBenchmarkDescriptionx_plane(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.x_plane(-5,5).build()
        self.assertEqual(description.x_near, -5)
        self.assertEqual(description.x_far, 5)
        self.assertTrue(description.has_x_plane())
        return

    def testBenchmarkDescriptiony_plane(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.y_plane(-5,5).build()
        self.assertEqual(description.y_near, -5)
        self.assertEqual(description.y_far, 5)
        self.assertTrue(description.has_y_plane())
        return

    def testBenchmarkDescriptionz_plane(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.z_plane(-5,5).build()
        self.assertEqual(description.z_near, -5)
        self.assertEqual(description.z_far, 5)
        self.assertTrue(description.has_z_plane())
        return

    def testBenchmarkDescriptionamount_of_points(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.amount_of_points(150).build()
        self.assertEqual(description.amount_of_points, 150)
        return

    def testBenchmarkDescriptionBuildernew_instance(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.amount_of_points(150).new_instance().x_plane(-10,10).build()
        self.assertNotEqual(description.amount_of_points, 150)
        self.assertEquals(description.x_near, -10)
        self.assertEquals(description.x_far, 10)
        return

    def testBenchmarkDescriptionWithdejong_F1(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.dejong_F1().build()
        self.assertIsNotNone(description.benchFn)
        self.assertIsNotNone(description.benchTitle)
        self.assertEqual(description.benchTitle, opti_benchmarks.dejong_F1.__name__)
        self.assertEqual(description.benchFn, opti_benchmarks.dejong_F1)
        return

    def testBenchmarkDescriptionNPLinspaceCreation(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder();
        description = Builder.dejong_F1().amount_of_points(150).x_plane(-5.12,5.12).y_plane(-5.12,5.12).build()
        self.assertIsNotNone(description.create_x_linspace())
        self.assertIsNotNone(description.create_y_linspace())
        self.assertIsInstance(description.create_x_linspace(), np.ndarray, "Expected created X linspace to be of numpy.darray")
        self.assertIsInstance(description.create_y_linspace(), np.ndarray, "Expected created Y linsapce to be of numpy.darray")

    def testBenchRunneris_valid_description(self):
        runner = opti_benchmarks.BenchmarkRunner()
        self.assertFalse(runner.is_valid_description(None))
        self.assertFalse(runner.is_valid_description(opti_benchmarks.BenchmarkDescription()))
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.dejong_F1().amount_of_points(150).x_plane(-5.12,5.12).build()
        self.assertFalse(runner.is_valid_description(description))
        description = Builder.dejong_F1().amount_of_points(150).y_plane(-5.12,5.12).build()
        self.assertFalse(runner.is_valid_description(description))
        description = Builder.dejong_F1().amount_of_points(150).build()
        self.assertFalse(runner.is_valid_description(description))
        description = Builder.dejong_F1().amount_of_points(150).x_plane(-5.12,5.12).y_plane(-5.12,5.12).build()
        self.assertTrue(runner.is_valid_description(description))
        return


    def testBenchRunnerrun_benchmark(self):
        runner = opti_benchmarks.BenchmarkRunner()
        self.assertRaises(opti_benchmarks.BenchmarkDescriptionError, runner.run_benchmark, None)
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder()
        description = Builder.amount_of_points(150).x_plane(-5.12,5.12).y_plane(-5.12,5.12).dejong_F1().build()
        result = runner.run_benchmark(description)
        self.assertIsNotNone(result, "Expected a result after the benchmark was executed")
        self.assertTrue(len(result.X) == description.amount_of_points)
        self.assertTrue(len(result.Y) == description.amount_of_points)
        self.assertTrue(len(result.Z) == description.amount_of_points)
        self.assertTrue(type(result.X) == np.ndarray)
        self.assertTrue(type(result.Y) == np.ndarray)
        self.assertTrue(type(result.Z) == np.ndarray)
        return

    def testBenchmarkFnProperties(self):
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder();
        description = Builder.dejong_F1().build()
        self.assertTrue(opti_benchmarks.dejong_F1 == description.benchFn);
        description = Builder.dejong_F5().build()
        self.assertTrue(opti_benchmarks.dejong_F5 == description.benchFn);
        description = Builder.dejong_F5().build()
        self.assertTrue(opti_benchmarks.dejong_F5 == description.benchFn);
        description = Builder.ackley().build()
        self.assertTrue(opti_benchmarks.ackley == description.benchFn);
        description = Builder.branin().build()
        self.assertTrue(opti_benchmarks.branin == description.benchFn);
        description = Builder.camel().build()
        self.assertTrue(opti_benchmarks.camel == description.benchFn);
        description = Builder.dropwave().build()
        self.assertTrue(opti_benchmarks.dropwave == description.benchFn);
        description = Builder.easom().build()
        self.assertTrue(opti_benchmarks.easom == description.benchFn);
        description = Builder.general_rosenbrock().build()
        self.assertTrue(opti_benchmarks.general_rosenbrock == description.benchFn);
        description = Builder.goldstein().build()
        self.assertTrue(opti_benchmarks.goldstein == description.benchFn);
        description = Builder.griewank().build()
        self.assertTrue(opti_benchmarks.griewank == description.benchFn);
        description = Builder.himmelblau().build()
        self.assertTrue(opti_benchmarks.himmelblau == description.benchFn);
        description = Builder.michalewicz().build()
        self.assertTrue(opti_benchmarks.michalewicz == description.benchFn);
        description = Builder.rosenbrock().build()
        self.assertTrue(opti_benchmarks.rosenbrock == description.benchFn);
        description = Builder.salomon().build()
        self.assertTrue(opti_benchmarks.salomon == description.benchFn);
        description = Builder.schwefel().build()
        self.assertTrue(opti_benchmarks.schwefel == description.benchFn);
        description = Builder.rastrigin().build()
        self.assertTrue(opti_benchmarks.rastrigin == description.benchFn);
        description = Builder.shubert().build()
        self.assertTrue(opti_benchmarks.shubert == description.benchFn);

    def testBenchmarkPlotter(self):
        runner = opti_benchmarks.BenchmarkRunner();
        Builder = opti_benchmarks.BenchmarkDescriptionBuilder();
        description = Builder.amount_of_points(150).x_plane(-65.356,65.356).y_plane(-65.356,65.356).dejong_F5().build();
        result = runner.run_benchmark(description);
        plotter = opti_benchmarks.BenchmarkResultPlotter()
        plotter.plot_result(result)
        with open(result.BenchTitle + ".pdf", "r") as testFile:
            self.assertTrue(result.BenchTitle, testFile.name)

if __name__ == "__main__":
    unittest.main()
