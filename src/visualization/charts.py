"""Chart and visualization functions"""

import pandas as pd
from typing import List


def create_comparison_chart(results: List[dict]):
    """
    Create comparison charts for scenarios.
    
    Args:
        results: List of P&L result dictionaries
        
    Returns:
        Plotly figure object
    """
    try:
        import plotly.graph_objects as go
        import plotly.express as px
    except ImportError:
        print("Plotly not installed. Install with: pip install plotly")
        return None
    
    df = pd.DataFrame(results)
    
    # Create subplots for key metrics
    fig = go.Figure()
    
    # Add revenue bars
    fig.add_trace(go.Bar(
        name='Revenue',
        x=df['Scenario'],
        y=df['revenue'],
        marker_color='steelblue'
    ))
    
    return fig
