"""P&L Calculator - Core financial model calculations"""

from typing import List, Dict, Any
from dataclasses import dataclass
from ..data.scenario import Scenario


@dataclass
class PLResult:
    """Profit & Loss calculation result"""
    scenario_name: str
    revenue: float
    cogs: float
    gross_margin: float
    gross_margin_pct: float
    marketing_spend: float
    trade_spend: float
    total_marketing_spend: float
    contribution: float
    contribution_pct: float

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'Scenario': self.scenario_name,
            'Revenue': f"${self.revenue:,.2f}",
            'COGS': f"${self.cogs:,.2f}",
            'Gross Margin': f"${self.gross_margin:,.2f}",
            'Gross Margin %': f"{self.gross_margin_pct:.1%}",
            'Marketing Spend': f"${self.marketing_spend:,.2f}",
            'Trade Spend': f"${self.trade_spend:,.2f}",
            'Total Marketing': f"${self.total_marketing_spend:,.2f}",
            'Contribution': f"${self.contribution:,.2f}",
            'Contribution %': f"{self.contribution_pct:.1%}",
        }


class PLCalculator:
    """Calculate P&L metrics for scenarios"""

    def calculate(self, scenario: Scenario) -> PLResult:
        """
        Calculate P&L metrics for a given scenario.
        
        Args:
            scenario: Scenario object with base parameters
            
        Returns:
            PLResult with calculated financial metrics
        """
        # Revenue
        revenue = scenario.revenue
        
        # COGS
        cogs = revenue * scenario.cogs_percent
        
        # Gross Margin
        gross_margin = revenue - cogs
        gross_margin_pct = gross_margin / revenue if revenue > 0 else 0
        
        # Marketing & Trade Spend
        marketing_spend = scenario.marketing_spend
        trade_spend = scenario.trade_spend
        total_marketing_spend = marketing_spend + trade_spend
        
        # Contribution
        contribution = gross_margin - total_marketing_spend
        contribution_pct = contribution / revenue if revenue > 0 else 0
        
        return PLResult(
            scenario_name=scenario.name,
            revenue=revenue,
            cogs=cogs,
            gross_margin=gross_margin,
            gross_margin_pct=gross_margin_pct,
            marketing_spend=marketing_spend,
            trade_spend=trade_spend,
            total_marketing_spend=total_marketing_spend,
            contribution=contribution,
            contribution_pct=contribution_pct,
        )

    def compare(self, results: List[PLResult], base_index: int = 0) -> Dict[str, Any]:
        """
        Compare multiple P&L results.
        
        Args:
            results: List of PLResult objects to compare
            base_index: Index of base case for incremental analysis (default: 0)
            
        Returns:
            Dictionary with comparison metrics
        """
        if not results:
            return {}
        
        base_result = results[base_index]
        comparison = {
            'scenarios': [r.to_dict() for r in results],
            'incremental_analysis': []
        }
        
        for i, result in enumerate(results):
            if i == base_index:
                continue
                
            incremental = {
                'vs': f"{result.scenario_name} vs {base_result.scenario_name}",
                'revenue_delta': result.revenue - base_result.revenue,
                'contribution_delta': result.contribution - base_result.contribution,
                'contribution_delta_pct': (
                    (result.contribution - base_result.contribution) / base_result.contribution * 100
                    if base_result.contribution != 0 else 0
                ),
                'roi': (
                    (result.contribution_delta - base_result.total_marketing_spend) / 
                    base_result.total_marketing_spend * 100
                    if base_result.total_marketing_spend != 0 else 0
                )
            }
            comparison['incremental_analysis'].append(incremental)
        
        return comparison
