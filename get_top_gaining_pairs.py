from consts import WS_GAINERS
from get_pairs import get_pairs
from filter_chain_pairs import filter_chain_pairs

def get_top_gaining_pairs(chain: str = None):
    """
    Get the top gaining pairs.

    Args:
        chain (str, optional): The chain to filter the pairs. Defaults to None.

    Returns:
        list: The list of top gaining pairs.
    """
    pairs = get_pairs(WS_GAINERS)
    if chain:
        pairs = filter_chain_pairs(pairs, chain)
    return pairs