from dex_screen_pair import dicts_to_list
import pandas as pd

def create_data_frame(pairs):
    """
    Create a pandas DataFrame from a list of DexScreenerPair dictionaries.

    Args:
        pairs (list): A list of DexScreenerPair dictionaries.

    Returns:
        pandas.DataFrame: The DataFrame created from the input list of dictionaries.
    """
    return pd.DataFrame(dicts_to_list(pairs))