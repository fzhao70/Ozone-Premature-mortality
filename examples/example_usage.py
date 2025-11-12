"""
Example usage of the Ozone Premature Mortality Calculator

This script demonstrates how to use the mortality calculation functions
to estimate premature deaths from ozone exposure.
"""

import sys
import os

# Add the parent directory to the path to import the src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mortality_calculator import mort_R, mort_C, mort_L


def calculate_mortality_for_region(ozone_conc, population, region):
    """
    Calculate total premature mortality for a given region.

    Parameters:
    -----------
    ozone_conc : float
        Ozone concentration in ppb (AMDA8)
    population : int/float
        Population size in persons
    region : str
        Region identifier ('china' or 'us')

    Returns:
    --------
    dict : Dictionary containing mortality estimates by cause
    """
    respiratory = mort_R(ozone_conc, population, region)
    cardiovascular = mort_C(ozone_conc, population, region)
    lung_cancer = mort_L(ozone_conc, population, region)
    total = respiratory + cardiovascular + lung_cancer

    return {
        'respiratory': respiratory,
        'cardiovascular': cardiovascular,
        'lung_cancer': lung_cancer,
        'total': total
    }


def main():
    """Main example demonstrating mortality calculations."""

    print("=" * 70)
    print("Ozone Premature Mortality Calculator - Example Usage")
    print("=" * 70)
    print()

    # Example 1: China with moderate ozone levels
    print("Example 1: China - Moderate Ozone Exposure")
    print("-" * 70)
    ozone_china = 60  # ppb (AMDA8)
    pop_china = 1_000_000  # 1 million people
    region_china = 'china'

    results_china = calculate_mortality_for_region(ozone_china, pop_china, region_china)

    print(f"Ozone Concentration: {ozone_china} ppb (AMDA8)")
    print(f"Population: {pop_china:,} persons")
    print(f"Region: {region_china.upper()}")
    print()
    print("Estimated Premature Deaths (persons/year):")
    print(f"  Respiratory diseases:    {results_china['respiratory']:>10.2f}")
    print(f"  Cardiovascular diseases: {results_china['cardiovascular']:>10.2f}")
    print(f"  Lung cancer:             {results_china['lung_cancer']:>10.2f}")
    print(f"  {'=' * 35}")
    print(f"  Total:                   {results_china['total']:>10.2f}")
    print()

    # Example 2: US with high ozone levels
    print("\nExample 2: United States - High Ozone Exposure")
    print("-" * 70)
    ozone_us = 75  # ppb (AMDA8)
    pop_us = 500_000  # 500,000 people
    region_us = 'us'

    results_us = calculate_mortality_for_region(ozone_us, pop_us, region_us)

    print(f"Ozone Concentration: {ozone_us} ppb (AMDA8)")
    print(f"Population: {pop_us:,} persons")
    print(f"Region: {region_us.upper()}")
    print()
    print("Estimated Premature Deaths (persons/year):")
    print(f"  Respiratory diseases:    {results_us['respiratory']:>10.2f}")
    print(f"  Cardiovascular diseases: {results_us['cardiovascular']:>10.2f}")
    print(f"  Lung cancer:             {results_us['lung_cancer']:>10.2f}")
    print(f"  {'=' * 35}")
    print(f"  Total:                   {results_us['total']:>10.2f}")
    print()

    # Example 3: Below threshold (should show zero mortality)
    print("\nExample 3: Below WHO Threshold")
    print("-" * 70)
    ozone_low = 40  # ppb (AMDA8) - below 50 ppb threshold
    pop_low = 1_000_000
    region_low = 'us'

    results_low = calculate_mortality_for_region(ozone_low, pop_low, region_low)

    print(f"Ozone Concentration: {ozone_low} ppb (AMDA8)")
    print(f"Population: {pop_low:,} persons")
    print(f"Region: {region_low.upper()}")
    print()
    print("Estimated Premature Deaths (persons/year):")
    print(f"  Respiratory diseases:    {results_low['respiratory']:>10.2f}")
    print(f"  Cardiovascular diseases: {results_low['cardiovascular']:>10.2f}")
    print(f"  Lung cancer:             {results_low['lung_cancer']:>10.2f}")
    print(f"  {'=' * 35}")
    print(f"  Total:                   {results_low['total']:>10.2f}")
    print()
    print("Note: No mortality attributed because ozone is below the WHO")
    print("      threshold of 50 ppb (100 μg/m³)")
    print()

    # Example 4: Comparing regions
    print("\nExample 4: Regional Comparison")
    print("-" * 70)
    ozone_comp = 65  # ppb
    pop_comp = 1_000_000

    results_china_comp = calculate_mortality_for_region(ozone_comp, pop_comp, 'china')
    results_us_comp = calculate_mortality_for_region(ozone_comp, pop_comp, 'us')

    print(f"Ozone Concentration: {ozone_comp} ppb (AMDA8)")
    print(f"Population: {pop_comp:,} persons (same for both regions)")
    print()
    print(f"{'Cause':<25} {'China':>15} {'United States':>15}")
    print("-" * 70)
    print(f"{'Respiratory':<25} {results_china_comp['respiratory']:>15.2f} {results_us_comp['respiratory']:>15.2f}")
    print(f"{'Cardiovascular':<25} {results_china_comp['cardiovascular']:>15.2f} {results_us_comp['cardiovascular']:>15.2f}")
    print(f"{'Lung Cancer':<25} {results_china_comp['lung_cancer']:>15.2f} {results_us_comp['lung_cancer']:>15.2f}")
    print("-" * 70)
    print(f"{'Total':<25} {results_china_comp['total']:>15.2f} {results_us_comp['total']:>15.2f}")
    print()
    print("Note: China shows higher mortality rates due to higher baseline")
    print("      disease rates in the population (WHO 2016 data)")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
