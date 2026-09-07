"""Tests for Scenario model"""

import pytest
from src.data.scenario import Scenario


class TestScenario:
    """Test suite for Scenario"""
    
    def test_scenario_creation(self):
        """Test basic scenario creation"""
        scenario = Scenario(
            name="Test",
            revenue=1000000,
            cogs_percent=0.45,
            marketing_spend=50000,
            trade_spend=30000
        )
        
        assert scenario.name == "Test"
        assert scenario.revenue == 1000000
    
    def test_negative_revenue_raises_error(self):
        """Test that negative revenue raises error"""
        with pytest.raises(ValueError):
            Scenario(
                name="Invalid",
                revenue=-1000,
                cogs_percent=0.45,
                marketing_spend=50000,
                trade_spend=30000
            )
    
    def test_invalid_cogs_percent_raises_error(self):
        """Test that invalid COGS percent raises error"""
        with pytest.raises(ValueError):
            Scenario(
                name="Invalid",
                revenue=1000000,
                cogs_percent=1.5,  # > 1.0
                marketing_spend=50000,
                trade_spend=30000
            )
