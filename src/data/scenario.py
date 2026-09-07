"""Scenario data model"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Scenario:
    """
    Business scenario for P&L simulation.
    
    Attributes:
        name: Scenario identifier
        revenue: Total revenue in dollars
        cogs_percent: COGS as percentage of revenue (0.0-1.0)
        marketing_spend: Advertising & Promotion spend
        trade_spend: Trade/promotional support spend
        volume_lift: Expected volume increase from marketing (optional)
        price_change: Price change percentage (optional)
        description: Scenario description (optional)
    """
    name: str
    revenue: float
    cogs_percent: float
    marketing_spend: float
    trade_spend: float
    volume_lift: Optional[float] = None
    price_change: Optional[float] = None
    description: Optional[str] = None
    
    def __post_init__(self):
        """Validate scenario parameters"""
        if self.revenue < 0:
            raise ValueError("Revenue must be non-negative")
        if not 0 <= self.cogs_percent <= 1:
            raise ValueError("COGS percent must be between 0 and 1")
        if self.marketing_spend < 0:
            raise ValueError("Marketing spend must be non-negative")
        if self.trade_spend < 0:
            raise ValueError("Trade spend must be non-negative")
