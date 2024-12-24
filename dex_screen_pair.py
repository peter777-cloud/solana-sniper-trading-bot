from typing import List, NamedTuple

# Define a named tuple to store DexScreenerPair data
DexScreenerPair = NamedTuple('DexScreenerPair', [
    ('chain', str),
    ('dex', str),
    ('pair_address', str),
    ('base_token_symbol', str),
    ('base_token_name', str),
    ('base_token_address', str),
    ('quote_token_symbol', str),
    ('quote_token_name', str),
    ('quote_token_address', str),
    ('pair_create_timestamp', float),
    ('price_usd', str),
    ('market_cap', float),
    ('volumn_5m', float),
    ('volumn_1h', float),
    ('volumn_6h', float),
    ('volumn_24h', float),
    ('price_change_5m', float),
    ('price_change_1h', float),
    ('price_change_6h', float),
    ('price_change_24h', float)
])

def from_dict(obj: dict) -> DexScreenerPair:
    """
    Converts a dictionary object to a DexScreenerPair object.

    Args:
        obj (dict): The dictionary object containing the pair information.

    Returns:
        DexScreenerPair: The converted DexScreenerPair object.
    """
    return DexScreenerPair(
        chain=obj["chainId"],
        dex=obj["dexId"],
        pair_address=obj["pairAddress"],
        base_token_symbol=obj["baseToken"]["symbol"],
        base_token_name=obj["baseToken"]["name"],
        base_token_address=obj["baseToken"]["address"],
        quote_token_symbol=obj["quoteToken"]["symbol"],
        quote_token_name=obj["quoteToken"]["name"],
        quote_token_address=obj["quoteToken"]["address"],
        pair_create_timestamp=obj["pairCreatedAt"],
        price_usd=obj.get("priceUsd"),
        market_cap=obj.get("marketCap"),
        volumn_5m=obj["volume"].get("m5"),
        volumn_1h=obj["volume"].get("h1"),
        volumn_6h=obj["volume"].get("h6"),
        volumn_24h=obj["volume"].get("h24"),
        price_change_5m=obj["priceChange"].get("m5"),
        price_change_1h=obj["priceChange"].get("h1"),
        price_change_6h=obj["priceChange"].get("h6"),
        price_change_24h=obj["priceChange"].get("h24"),
    )

def dicts_to_list(objs: List[dict]) -> List[DexScreenerPair]:
    return [from_dict(obj) for obj in objs]