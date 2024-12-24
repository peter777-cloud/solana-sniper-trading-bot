from consts import newest_pairs_string_slugged, top_gaining_pairs_string_slugged, trending_pairs_string_slugged
from create_folder_if_not_exists import create_folder_if_not_exists
from data_frames_array_save import data_frames_array_save
from generate_full_report_html import generate_full_report_html

def generate_files(trending_pairs_df, top_gaining_pairs_df, newest_pairs_df, chain):
    """
    Generate files for the given data frames and chain.

    Parameters:
    - trending_pairs_df (DataFrame): Data frame containing trending pairs.
    - top_gaining_pairs_df (DataFrame): Data frame containing top gaining pairs.
    - newest_pairs_df (DataFrame): Data frame containing newest pairs.
    - chain (str): Chain name.

    Returns:
    None
    """
    create_folder_if_not_exists(f"./reports")
    create_folder_if_not_exists(f"./reports/{chain}")
    data_frames_array_save(trending_pairs_df, chain, trending_pairs_string_slugged)
    data_frames_array_save(top_gaining_pairs_df, chain, top_gaining_pairs_string_slugged)
    data_frames_array_save(newest_pairs_df, chain, newest_pairs_string_slugged)
    generate_full_report_html(trending_pairs_df, top_gaining_pairs_df, newest_pairs_df, chain)