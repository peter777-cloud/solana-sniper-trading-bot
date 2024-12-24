from consts import WS_TRENDING
from get_pairs import get_pairs
from filter_chain_pairs import filter_chain_pairs

def get_trending_pairs(chain: str = None):
    """
    Get the trending pairs from the WebSocket API.

    Args:
        chain (str, optional): The chain to filter the pairs by. Defaults to None.

    Returns:
        list: A list of trending pairs.
    """
    pairs = get_pairs(WS_TRENDING)
    if chain:
        pairs = filter_chain_pairs(pairs, chain)
    return pairs