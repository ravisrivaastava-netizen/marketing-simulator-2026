"""Data loading utilities"""

import pandas as pd
from pathlib import Path
from typing import List
from .scenario import Scenario


class DataLoader:
    """Load and manage scenario data"""
    
    @staticmethod
    def load_csv(filepath: str) -> pd.DataFrame:
        """
        Load scenarios from CSV file.
        
        Args:
            filepath: Path to CSV file
            
        Returns:
            DataFrame with scenario data
        """
        return pd.read_csv(filepath)
    
    @staticmethod
    def load_scenarios_from_csv(filepath: str) -> List[Scenario]:
        """
        Load Scenario objects from CSV file.
        
        Args:
            filepath: Path to CSV file with columns:
                    name, revenue, cogs_percent, marketing_spend, trade_spend
                    
        Returns:
            List of Scenario objects
        """
        df = pd.read_csv(filepath)
        scenarios = []
        
        for _, row in df.iterrows():
            scenario = Scenario(
                name=row['name'],
                revenue=float(row['revenue']),
                cogs_percent=float(row['cogs_percent']),
                marketing_spend=float(row['marketing_spend']),
                trade_spend=float(row['trade_spend']),
                description=row.get('description', None)
            )
            scenarios.append(scenario)
        
        return scenarios
    
    @staticmethod
    def save_results_to_csv(results: List[dict], output_path: str) -> None:
        """
        Save P&L results to CSV file.
        
        Args:
            results: List of result dictionaries
            output_path: Path to save CSV file
        """
        df = pd.DataFrame(results)
        df.to_csv(output_path, index=False)
