def generate_reports_path(chain, type_string, file_type):
    """
    Generate the path for the reports based on the given parameters.

    Args:
        chain (str): The chain name.
        type_string (str): The type of report.
        file_type (str): The file extension.

    Returns:
        str: The generated path for the reports.
    """
    return f"./reports/{chain}/{chain}_{type_string}.{file_type}"