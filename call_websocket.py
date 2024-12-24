import websocket
import ssl
import json
from get_header import get_header

def call_websocket_load_json(uri) -> dict:
    """
    Calls a WebSocket URI and returns the received JSON data as a dictionary.

    Args:
        uri (str): The URI of the WebSocket server.

    Returns:
        dict: The received JSON data as a dictionary.
    """
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.connect(uri, header=get_header(), suppress_origin=True)
    return json.loads(ws.recv())