# Marketing P&L Simulator

## Status
🟡 Starter project — concept and framework stage

## Objective

Connect marketing decisions to commercial outcomes through scenario modeling and financial impact analysis.

## Model

**Revenue → COGS → Gross Margin → Marketing/A&P → Trade Spend → Contribution**

## Features

- **Scenario Builder**: Create and compare multiple business scenarios
- **P&L Calculator**: Automated revenue, margin, and contribution calculations
- **Sensitivity Analysis**: Understand impact of key variables
- **Dashboard**: Visualize financial outcomes across scenarios

## Scenario Examples

- Price increase
- A&P (Advertising & Promotion) budget increase
- Premium mix improvement
- New product launch
- Distribution expansion
- Cost reduction initiatives

## Project Structure

```
marketing-simulator-2026/
├── data/
│   ├── raw/                 # Source data (synthetic datasets)
│   ├── processed/           # Cleaned/transformed data
│   └── scenarios/           # Scenario configurations
├── src/
│   ├── models/              # Core calculation models
│   ├── data/                # Data processing modules
│   ├── utils/               # Utility functions
│   └── visualization/       # Charting and visualization
├── notebooks/               # Jupyter notebooks for exploration
├── tests/                   # Unit and integration tests
├── docs/                    # Documentation and guides
├── config/                  # Configuration files
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
└── README.md               # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

```bash
# Clone the repository
git clone https://github.com/ravisrivaastava-netizen/marketing-simulator-2026.git
cd marketing-simulator-2026

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```python
from src.models.pl_calculator import PLCalculator
from src.data.scenario import Scenario

# Create a base scenario
base = Scenario(
    name="Base Case",
    revenue=1000000,
    cogs_percent=0.45,
    marketing_spend=50000,
    trade_spend=30000
)

# Create an alternative scenario
test = Scenario(
    name="A&P Increase",
    revenue=1000000,
    cogs_percent=0.45,
    marketing_spend=75000,  # Increased A&P
    trade_spend=30000
)

# Calculate P&L
calculator = PLCalculator()
base_pl = calculator.calculate(base)
test_pl = calculator.calculate(test)

# Compare scenarios
comparison = calculator.compare([base_pl, test_pl])
print(comparison)
```

## Data

Currently using synthetic values. Public datasets can be integrated in future versions.

## Output Metrics

Compare scenarios on:
- **Revenue**: Total sales
- **COGS**: Cost of goods sold
- **Gross Margin**: Revenue - COGS
- **Gross Margin %**: Gross Margin / Revenue
- **Marketing Investment**: A&P spending
- **Trade Spend**: Promotional/trade support
- **Contribution**: Gross Margin - Marketing - Trade Spend
- **Contribution %**: Contribution / Revenue
- **Incremental Economics**: Changes vs. base case

## Development

### Running Tests

```bash
pytest tests/
```

### Running Notebooks

```bash
jupyter notebook
```

## Contributing

Contributions welcome! Please:
1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Commit changes (`git commit -am 'Add feature'`)
3. Push to branch (`git push origin feature/your-feature`)
4. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Roadmap

- [ ] Core P&L calculation engine
- [ ] Scenario comparison framework
- [ ] Web UI (Streamlit/Dash)
- [ ] Data import/export (CSV, Excel)
- [ ] Sensitivity analysis module
- [ ] Reporting and export
- [ ] Real-world dataset integration
- [ ] Advanced analytics (elasticity, attribution)
