from consts import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client, Client

def check_if_name_exists_in_supabase(name: str, table: str):
    """
    Check if a name exists in a Supabase table.

    Args:
        name (str): The name to check.
        table (str): The name of the table to search in.

    Returns:
        bool: True if the name exists in the table, False otherwise.
    """
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    d = supabase.table(table).select("*").eq("name", name).execute()
    return len(d.data) > 0