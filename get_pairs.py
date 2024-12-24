from call_websocket import call_websocket_load_json
from consts import MAX_TRIES

def get_pairs(uri):
    """
    Retrieves a list of pairs from the given URI.

    Args:
        uri (str): The URI to fetch data from.

    Returns:
        list: A list of pairs retrieved from the URI.

    """
    for i in range(MAX_TRIES):
        data = call_websocket_load_json(uri)
        if pairs := data.get("pairs"):
            return pairs
        print(f"({i + 1}/{MAX_TRIES}) -- {data}")
    return []