# Ozone Premature Mortality Calculator

A Python-based tool for calculating premature mortality attributable to ozone (O₃) exposure, using epidemiological data and concentration-response relationships from peer-reviewed studies and WHO health statistics.

## Overview

This project provides functions to estimate premature mortality from ozone exposure across three major health outcomes:
- **Respiratory diseases** (including COPD, asthma, and respiratory infections)
- **Cardiovascular diseases** (including ischemic heart disease, stroke, and hypertensive heart disease)
- **Lung cancer**

The calculations are based on WHO 2016 mortality data and incorporate threshold-based concentration-response relationships from multiple epidemiological studies.

## Features

- Separate mortality calculations for respiratory, cardiovascular, and lung cancer outcomes
- Region-specific baseline mortality rates (China and US)
- WHO-recommended threshold of 100 μg/m³ (AMDA8) for ozone exposure
- Peer-reviewed concentration-response coefficients from multiple studies
- Population-weighted mortality estimates

## Installation

### Prerequisites

- Python 3.6 or higher
- NumPy

### Setup

1. Clone this repository:
```bash
git clone https://github.com/fzhao70/Ozone-Premature-mortality.git
cd Ozone-Premature-mortality
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
import numpy as np
from src.mortality_calculator import mort_R, mort_C, mort_L

# Example parameters
ozone_concentration = 60  # ppb (AMDA8)
population = 1000000  # persons
region = 'china'  # or 'us'

# Calculate respiratory mortality
respiratory_deaths = mort_R(ozone_concentration, population, region)
print(f"Estimated respiratory deaths: {respiratory_deaths:.2f} persons/yr")

# Calculate cardiovascular mortality
cardiovascular_deaths = mort_C(ozone_concentration, population, region)
print(f"Estimated cardiovascular deaths: {cardiovascular_deaths:.2f} persons/yr")

# Calculate lung cancer mortality
lung_cancer_deaths = mort_L(ozone_concentration, population, region)
print(f"Estimated lung cancer deaths: {lung_cancer_deaths:.2f} persons/yr")

# Total premature mortality
total_deaths = respiratory_deaths + cardiovascular_deaths + lung_cancer_deaths
print(f"Total estimated premature deaths: {total_deaths:.2f} persons/yr")
```

## Methodology

### Input Parameters

- **c** (float): Ozone concentration in ppb (parts per billion), measured as AMDA8 (annual average daily maximum 8-hour ozone concentration)
- **pop** (int/float): Population size in persons
- **region** (str): Geographic region, either 'china' or 'us'

### Thresholds

- **WHO Standard**: AMDA8 100 μg/m³ (50 ppb when converted)
- **China-specific thresholds**:
  - AMDA8: 26.7 ppb (Turner et al. 2016)
  - 6mMDA1: 33.3 ppb (Jerrett et al. 2009)

### Concentration-Response Relationships

The relative risk (RR) is calculated using:

```
RR = exp(β × (c - c₀))
```

Where:
- β = concentration-response coefficient (disease-specific)
- c = ozone concentration (ppb)
- c₀ = threshold concentration (50 ppb, equivalent to WHO's 100 μg/m³)

### Mortality Calculation

```
Mortality = y₀ × ((RR - 1) / RR) × population
```

Where:
- y₀ = baseline mortality rate (region and disease-specific, from WHO 2016 data)

### Data Sources

#### Baseline Mortality Rates (WHO 2016)

**China (Population: 1,411,415 thousand)**
- Respiratory diseases: 1,115.7 deaths per 1,000 population/year
  - Respiratory infections: 177.5
  - COPD: 895.4
  - Asthma: 24.3
  - Other: 18.6
- Cardiovascular diseases: 4,475.7 deaths per 1,000 population/year
- Lung cancer: 637.7 deaths per 1,000 population/year

**United States (Population: 322,180 thousand)**
- Respiratory diseases: 313.3 deaths per 1,000 population/year
  - Respiratory infections: 66.4
  - COPD: 193.2
  - Asthma: 4.2
  - Other: 49.6
- Cardiovascular diseases: 837.2 deaths per 1,000 population/year
- Lung cancer: 84.7 deaths per 1,000 population/year

#### Concentration-Response Coefficients

| Disease Category | RR per 20 ppb | Study Reference |
|-----------------|---------------|-----------------|
| Respiratory | 1.11 | Lipsett et al. 2011 |
| Cardiovascular | 1.02 | Kreski et al. 2009, Smith et al. 2009 |
| Lung Cancer | 0.96 | Turner et al. 2016 |

## Scientific References

### WHO Data Source
- WHO methods and data sources for global causes of death 2000-2016. Global Health Estimates Technical Paper WHO/HIS/IER/GHE/2018.3. Geneva: World Health Organization; 2018.

### Epidemiological Studies
- **Lipsett et al. (2011)**: Long-term exposure to air pollution and cardiorespiratory disease
- **Jerrett et al. (2009)**: Long-term ozone exposure and mortality
- **Turner et al. (2016)**: Long-term ozone exposure and mortality in a large prospective study
- **Kreski et al. (2009)** / **Smith et al. (2009)**: Cardiovascular effects of ozone exposure

## Unit Conversions

The code uses the following conversion for ozone concentrations:
- **μg/m³ to ppb**: Division by 2.00 (Standard Temperature and Pressure - European Union conditions at 20°C)

## Project Structure

```
Ozone-Premature-mortality/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
├── src/
│   └── mortality_calculator.py       # Main calculation functions
├── examples/
│   └── example_usage.py              # Usage examples
└── tests/
    └── test_mortality_calculator.py  # Unit tests
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{ozone_mortality_calculator,
  author = {fzhao70},
  title = {Ozone Premature Mortality Calculator},
  year = {2024},
  url = {https://github.com/fzhao70/Ozone-Premature-mortality}
}
```

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

## Acknowledgments

- World Health Organization for providing comprehensive mortality statistics
- All researchers whose epidemiological studies contributed to the concentration-response relationships used in this tool
