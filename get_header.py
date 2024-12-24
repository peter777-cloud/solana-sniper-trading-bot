@staticmethod
def get_header():
    """
    Returns the header dictionary containing the User-Agent and Origin values.

    Returns:
        dict: The header dictionary.
    """
    return {
        "User-Agent": " ".join(
            [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/113.0.0.0 Safari/537.36",
            ]
        ),
        "Origin": "https://dexscreener.com",
    }