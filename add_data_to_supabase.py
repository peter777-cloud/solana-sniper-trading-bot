from consts import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client, Client


def add_data_to_supabase(pairsType, pair, createscanLink):
    """
    Add data to Supabase table.

    Args:
        pairsType (str): The type of pairs.
        pair (dict): The pair data.
        createscanLink (str): The scan link.

    Returns:
        None
    """
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    supabase.table(pairsType).insert({
                "name": pair.get("baseToken").get("name"),
                "scan": createscanLink,
                "json_data": pair, 
                "type": pairsType
    }).execute()