import os

import os

def create_folder_if_not_exists(folder_path):
    """
    Create a folder if it doesn't already exist.

    Args:
        folder_path (str): The path of the folder to be created.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)