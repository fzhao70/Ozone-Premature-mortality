"""
Unit tests for the Ozone Premature Mortality Calculator

Run with: python -m pytest tests/
or: python -m unittest tests/test_mortality_calculator.py
"""

import unittest
import sys
import os

# Add the parent directory to the path to import the src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mortality_calculator import mort_R, mort_C, mort_L


class TestMortalityCalculator(unittest.TestCase):
    """Test cases for mortality calculation functions."""

    def setUp(self):
        """Set up test parameters."""
        self.test_population = 1_000_000
        self.threshold = 50  # ppb, equivalent to WHO 100 μg/m³

    def test_mort_R_china_above_threshold(self):
        """Test respiratory mortality calculation for China above threshold."""
        result = mort_R(60, self.test_population, 'china')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_R_us_above_threshold(self):
        """Test respiratory mortality calculation for US above threshold."""
        result = mort_R(60, self.test_population, 'us')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_R_below_threshold(self):
        """Test respiratory mortality at threshold (should be zero)."""
        result = mort_R(40, self.test_population, 'china')
        self.assertEqual(result, 0, "Mortality should be zero below threshold")

    def test_mort_C_china_above_threshold(self):
        """Test cardiovascular mortality calculation for China above threshold."""
        result = mort_C(60, self.test_population, 'china')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_C_us_above_threshold(self):
        """Test cardiovascular mortality calculation for US above threshold."""
        result = mort_C(60, self.test_population, 'us')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_C_below_threshold(self):
        """Test cardiovascular mortality below threshold (should be zero)."""
        result = mort_C(40, self.test_population, 'china')
        self.assertEqual(result, 0, "Mortality should be zero below threshold")

    def test_mort_L_china_above_threshold(self):
        """Test lung cancer mortality calculation for China above threshold."""
        result = mort_L(60, self.test_population, 'china')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_L_us_above_threshold(self):
        """Test lung cancer mortality calculation for US above threshold."""
        result = mort_L(60, self.test_population, 'us')
        self.assertGreater(result, 0, "Mortality should be positive above threshold")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_mort_L_below_threshold(self):
        """Test lung cancer mortality below threshold (should be zero)."""
        result = mort_L(40, self.test_population, 'china')
        self.assertEqual(result, 0, "Mortality should be zero below threshold")

    def test_mortality_increases_with_concentration(self):
        """Test that mortality increases as ozone concentration increases."""
        conc_low = 55
        conc_high = 70

        # Test for respiratory
        mort_r_low = mort_R(conc_low, self.test_population, 'china')
        mort_r_high = mort_R(conc_high, self.test_population, 'china')
        self.assertLess(mort_r_low, mort_r_high,
                       "Higher ozone should result in higher respiratory mortality")

        # Test for cardiovascular
        mort_c_low = mort_C(conc_low, self.test_population, 'china')
        mort_c_high = mort_C(conc_high, self.test_population, 'china')
        self.assertLess(mort_c_low, mort_c_high,
                       "Higher ozone should result in higher cardiovascular mortality")

        # Test for lung cancer
        mort_l_low = mort_L(conc_low, self.test_population, 'china')
        mort_l_high = mort_L(conc_high, self.test_population, 'china')
        self.assertLess(mort_l_low, mort_l_high,
                       "Higher ozone should result in higher lung cancer mortality")

    def test_mortality_scales_with_population(self):
        """Test that mortality scales proportionally with population."""
        pop_small = 100_000
        pop_large = 1_000_000
        conc = 60

        # Test respiratory
        mort_r_small = mort_R(conc, pop_small, 'china')
        mort_r_large = mort_R(conc, pop_large, 'china')
        ratio = mort_r_large / mort_r_small
        self.assertAlmostEqual(ratio, 10, places=5,
                             msg="Mortality should scale linearly with population")

    def test_china_vs_us_baseline_rates(self):
        """Test that China has higher mortality rates than US (due to higher baseline)."""
        conc = 65
        pop = self.test_population

        # Respiratory
        mort_r_china = mort_R(conc, pop, 'china')
        mort_r_us = mort_R(conc, pop, 'us')
        self.assertGreater(mort_r_china, mort_r_us,
                          "China should have higher respiratory mortality (higher baseline)")

        # Cardiovascular
        mort_c_china = mort_C(conc, pop, 'china')
        mort_c_us = mort_C(conc, pop, 'us')
        self.assertGreater(mort_c_china, mort_c_us,
                          "China should have higher cardiovascular mortality (higher baseline)")

        # Lung cancer
        mort_l_china = mort_L(conc, pop, 'china')
        mort_l_us = mort_L(conc, pop, 'us')
        self.assertGreater(mort_l_china, mort_l_us,
                          "China should have higher lung cancer mortality (higher baseline)")

    def test_at_threshold(self):
        """Test mortality at exactly the threshold concentration."""
        # At threshold (50 ppb), mortality should be zero (RR = 1)
        mort_r = mort_R(50, self.test_population, 'china')
        mort_c = mort_C(50, self.test_population, 'china')
        mort_l = mort_L(50, self.test_population, 'china')

        self.assertEqual(mort_r, 0, "Respiratory mortality should be zero at threshold")
        self.assertEqual(mort_c, 0, "Cardiovascular mortality should be zero at threshold")
        self.assertEqual(mort_l, 0, "Lung cancer mortality should be zero at threshold")

    def test_zero_population(self):
        """Test that zero population results in zero mortality."""
        result = mort_R(60, 0, 'china')
        self.assertEqual(result, 0, "Zero population should result in zero mortality")

    def test_high_concentration(self):
        """Test calculations with very high ozone concentrations."""
        high_conc = 150  # Very high ozone level
        result = mort_R(high_conc, self.test_population, 'china')
        self.assertGreater(result, 0, "Should handle high concentrations")
        self.assertLess(result, self.test_population,
                       "Mortality should not exceed population")


class TestInputValidation(unittest.TestCase):
    """Test input validation and edge cases."""

    def test_negative_concentration(self):
        """Test behavior with negative concentration (should return 0)."""
        result = mort_R(-10, 1000000, 'china')
        self.assertEqual(result, 0, "Negative concentration should result in zero mortality")

    def test_negative_population(self):
        """Test behavior with negative population."""
        result = mort_R(60, -1000000, 'china')
        # Should be negative (mathematically), though not realistic
        self.assertLess(result, 0, "Negative population results in negative mortality")


def run_tests():
    """Run all tests and print summary."""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestMortalityCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestInputValidation))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)

    return result


if __name__ == '__main__':
    run_tests()
