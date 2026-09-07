# Getting Started with Marketing P&L Simulator

## Installation

```bash
git clone https://github.com/ravisrivaastava-netizen/marketing-simulator-2026.git
cd marketing-simulator-2026
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic Usage

### 1. Create Scenarios

```python
from src.data.scenario import Scenario

base_case = Scenario(
    name="Base Case",
    revenue=1000000,
    cogs_percent=0.45,
    marketing_spend=50000,
    trade_spend=30000
)

promo_case = Scenario(
    name="Increased Promotion",
    revenue=1000000,
    cogs_percent=0.45,
    marketing_spend=75000,  # +$25k
    trade_spend=40000       # +$10k
)
```

### 2. Calculate P&L

```python
from src.models.pl_calculator import PLCalculator

calculator = PLCalculator()

base_result = calculator.calculate(base_case)
promo_result = calculator.calculate(promo_case)
```

### 3. Compare Results

```python
comparison = calculator.compare([base_result, promo_result])

for scenario in comparison['scenarios']:
    print(scenario)

for incremental in comparison['incremental_analysis']:
    print(incremental)
```

## Loading Data from CSV

Create a CSV file with columns: `name`, `revenue`, `cogs_percent`, `marketing_spend`, `trade_spend`

```python
from src.data.loader import DataLoader

scenarios = DataLoader.load_scenarios_from_csv('data/scenarios/my_scenarios.csv')
results = [calculator.calculate(s) for s in scenarios]
```

## Running Tests

```bash
pytest tests/ -v
```

## Next Steps

- Explore `examples/` for sample notebooks
- Check `docs/` for detailed documentation
- Review `src/` for implementation details
