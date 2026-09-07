"""Tests for P&L Calculator"""

import pytest
from src.models.pl_calculator import PLCalculator
from src.data.scenario import Scenario


class TestPLCalculator:
    """Test suite for PLCalculator"""
    
    @pytest.fixture
    def calculator(self):
        """Create calculator instance"""
        return PLCalculator()
    
    @pytest.fixture
    def base_scenario(self):
        """Create base test scenario"""
        return Scenario(
            name="Test Base",
            revenue=1000000,
            cogs_percent=0.45,
            marketing_spend=50000,
            trade_spend=30000
        )
    
    def test_calculate_basic(self, calculator, base_scenario):
        """Test basic P&L calculation"""
        result = calculator.calculate(base_scenario)
        
        assert result.revenue == 1000000
        assert result.cogs == 450000
        assert result.gross_margin == 550000
        assert result.gross_margin_pct == 0.55
        assert result.total_marketing_spend == 80000
        assert result.contribution == 470000
        assert result.contribution_pct == 0.47
    
    def test_calculate_zero_revenue(self, calculator):
        """Test calculation with zero revenue"""
        scenario = Scenario(
            name="Zero Revenue",
            revenue=0,
            cogs_percent=0.5,
            marketing_spend=10000,
            trade_spend=5000
        )
        result = calculator.calculate(scenario)
        
        assert result.gross_margin_pct == 0
        assert result.contribution_pct == 0
    
    def test_compare_scenarios(self, calculator):
        """Test scenario comparison"""
        scenario1 = Scenario(
            name="Base",
            revenue=1000000,
            cogs_percent=0.45,
            marketing_spend=50000,
            trade_spend=30000
        )
        scenario2 = Scenario(
            name="High Marketing",
            revenue=1000000,
            cogs_percent=0.45,
            marketing_spend=75000,
            trade_spend=30000
        )
        
        result1 = calculator.calculate(scenario1)
        result2 = calculator.calculate(scenario2)
        
        comparison = calculator.compare([result1, result2])
        
        assert 'scenarios' in comparison
        assert 'incremental_analysis' in comparison
        assert len(comparison['scenarios']) == 2
