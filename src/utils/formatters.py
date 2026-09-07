"""Formatting utilities for output"""


def format_currency(value: float, precision: int = 2) -> str:
    """
    Format value as currency string.
    
    Args:
        value: Numeric value to format
        precision: Decimal places (default: 2)
        
    Returns:
        Formatted currency string
    """
    return f"${value:,.{precision}f}"


def format_percentage(value: float, precision: int = 1) -> str:
    """
    Format value as percentage string.
    
    Args:
        value: Numeric value to format (0.5 = 50%)
        precision: Decimal places (default: 1)
        
    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.{precision}f}%"
