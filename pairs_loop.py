
from add_data_to_supabase import add_data_to_supabase
from check_if_name_exists_in_supabase import check_if_name_exists_in_supabase
from create_scan_link import create_scan_link
from postgrest.exceptions import APIError

def pairs_loop(pairs, pairsType, chain="solana"):
    """
    Iterate over a list of pairs and perform certain operations on each pair.

    Args:
        pairs (list): A list of pairs.
        pairsType (str): The type of pairs.
        chain (str, optional): The chain name. Defaults to "solana".

    Returns:
        None
    """
    for pair in pairs:
        type_string = pairsType
        try:
            name = pair.get("baseToken").get("name")
            is_data_in_supabase = check_if_name_exists_in_supabase(name, pairsType)
            if is_data_in_supabase:
                continue
            print(f"{name} does not exist in supabase - type {type_string}")
            add_data_to_supabase(pairsType, pair, create_scan_link(chain, pair))
        except APIError as e:
            print(e)