# P&L Model Documentation

## Formula Overview

### Revenue
- **Input**: Base revenue for scenario
- **Adjustments**: Price changes, volume lift (future enhancement)

### Cost of Goods Sold (COGS)
```
COGS = Revenue × COGS %
```

### Gross Margin
```
Gross Margin = Revenue - COGS
Gross Margin % = Gross Margin / Revenue
```

### Marketing & Trade Spend
- **Marketing Spend**: Advertising & Promotion budget
- **Trade Spend**: Promotional support and trade allowances
- **Total**: Marketing Spend + Trade Spend

### Contribution
```
Contribution = Gross Margin - Marketing Spend - Trade Spend
Contribution % = Contribution / Revenue
```

## Key Assumptions

1. **Linear COGS**: COGS scales proportionally with revenue
2. **Fixed Marketing Spend**: Marketing spend is treated as fixed (not volume-dependent)
3. **No Cross-elasticity**: Changes in one variable don't affect others
4. **No Competitive Response**: Assumes competitors don't react
5. **Single Period**: Analyzes one time period (no carryover effects)

## Future Enhancements

- Elasticity modeling (price sensitivity)
- Volume lift correlation with marketing spend
- Competitive response scenarios
- Multi-period analysis with carryover effects
- Attribution modeling
- Channel-level analysis
