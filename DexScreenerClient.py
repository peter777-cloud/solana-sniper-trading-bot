from src.modules import init
from consts import trending_pairs_string_slugged, top_gaining_pairs_string_slugged, newest_pairs_string_slugged
from create_data_frame import create_data_frame
from data_frames_array_print import data_frames_array_print
from generate_files import generate_files
from get_newest_pairs import get_newest_pairs
from get_top_gaining_pairs import get_top_gaining_pairs
from get_trending_pairs import get_trending_pairs
from pairs_loop import pairs_loop

def i_am_the_watcher_free_version(chain="solana", shouldGenerateFiles=True, shouldPrintDataFrames=False, shouldAddToSupabase=False):
    """
    This function performs various operations based on the provided parameters.
    
    Parameters:
    - chain (str): The blockchain to retrieve data from. Default is "solana".
    - shouldGenerateFiles (bool): Whether to generate files based on the retrieved data. Default is True.
    - shouldPrintDataFrames (bool): Whether to print the data frames. Default is False.
    - shouldAddToSupabase (bool): Whether to add the data to Supabase. Default is False.
    """
    trending_pairs = get_trending_pairs(chain)
    top_gaining_pairs = get_top_gaining_pairs(chain)
    newest_pairs = get_newest_pairs(chain)
    trending_pairs_df = create_data_frame(trending_pairs)
    top_gaining_pairs_df = create_data_frame(top_gaining_pairs)
    newest_pairs_df = create_data_frame(newest_pairs)

    if shouldGenerateFiles:
        generate_files(trending_pairs_df, top_gaining_pairs_df, newest_pairs_df, chain)

    if shouldPrintDataFrames:
        data_frames_array_print(trending_pairs_df, "Trending Pairs")
        data_frames_array_print(top_gaining_pairs_df, "Top Gaining Pairs")
        data_frames_array_print(newest_pairs_df, "Newest Pairs")

    if shouldAddToSupabase:
        pairs_loop(trending_pairs, trending_pairs_string_slugged, chain)
        pairs_loop(top_gaining_pairs, top_gaining_pairs_string_slugged, chain)
        pairs_loop(newest_pairs, newest_pairs_string_slugged, chain)
    
if __name__ == "__main__":
    i_am_the_watcher_free_version("ethereum", shouldGenerateFiles=False, shouldPrintDataFrames=True, shouldAddToSupabase=False)
