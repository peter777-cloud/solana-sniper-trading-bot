def data_frames_array_print(data_frame, type_string):
    """
    Print the type string and the first 10 rows of the data frame.

    Args:
        data_frame (pandas.DataFrame): The data frame to be printed.
        type_string (str): The type string to be printed.

    Returns:
        None
    """
    print(type_string)
    print(data_frame.head(n=10))