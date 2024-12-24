from generate_reports_path import generate_reports_path

def data_frames_array_save(data_frame, chain, type_string):
    """
    Save the given DataFrame to CSV, Markdown, and HTML formats.

    Args:
        data_frame (pandas.DataFrame): The DataFrame to be saved.
        chain (str): The chain name.
        type_string (str): The type string.

    Returns:
        None
    """
    data_frame.to_csv(generate_reports_path(chain, type_string, "csv"), index=False)
    data_frame.to_markdown(generate_reports_path(chain, type_string, "md"), index=False)
    data_frame.to_html(generate_reports_path(chain, type_string, "html"), index=False)