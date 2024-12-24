from consts import WS_NEWEST
from get_pairs import get_pairs
from filter_chain_pairs import filter_chain_pairs

def get_newest_pairs(chain: str = None):
    """
    Retrieves the newest pairs from the WS_NEWEST source.

    Args:
        chain (str, optional): The chain to filter the pairs by. Defaults to None.

    Returns:
        list: The newest pairs, optionally filtered by chain.
    """
    pairs = get_pairs(WS_NEWEST)
    if chain:
        pairs = filter_chain_pairs(pairs, chain)
    return pairs