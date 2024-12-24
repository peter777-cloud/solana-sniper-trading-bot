def create_scan_link(chain, pair):
    """
    Creates a scan link based on the given chain and pair.

    Args:
        chain (str): The blockchain chain name.
        pair (dict): The pair information.

    Returns:
        str: The scan link for the given chain and pair.
    """
    if chain == "ethereum" or chain == "eth" or chain == "ethereum-mainnet":
        return f"https://etherscan.io/token/{pair.get('baseToken').get('address')}"
    elif chain == "bsc" or chain == "binance" or chain == "binance-smart-chain":
        return f"https://bscscan.com/address/{pair.get('baseToken').get('address')}"
    elif chain == "polygon":
        return f"https://polygonscan.com/token/{pair.get('baseToken').get('address')}"
    elif chain == "fantom":
        return f"https://ftmscan.com/token/{pair.get('baseToken').get('address')}"
    elif chain == "harmony":
        return f"https://explorer.harmony.one/#/address/{pair.get('baseToken').get('address')}"
    elif chain == "avax":
        return f"https://cchain.explorer.avax.network/tokens/{pair.get('baseToken').get('address')}"
    elif chain == "heco":
        return f"https://hecoinfo.com/address/{pair.get('baseToken').get('address')}"
    elif chain == "celo":
        return f"https://explorer.celo.org/address/{pair.get('baseToken').get('address')}"
    elif chain == "palm":
        return f"https://explorer.palm.io/#/address/{pair.get('baseToken').get('address')}"
    elif chain == "moonriver":
        return f"https://moonriver.subscan.io/account/{pair.get('baseToken').get('address')}"
    # TODO - add more chains