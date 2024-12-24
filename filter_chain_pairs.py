@staticmethod
def filter_chain_pairs(pairs: list, chain: str):
    """
    Filters a list of pairs based on a given chain.

    Args:
        pairs (list): The list of pairs to filter.
        chain (str): The chain ID to filter by.

    Returns:
        list: The filtered list of pairs.
    """
    return list(filter(lambda x: x["chainId"] == chain, pairs))