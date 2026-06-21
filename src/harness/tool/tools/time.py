import datetime


def get_current_date() -> str:
    """
    return the current date in string format

    Returns:
        A string corresponding to the current date in ISO format YYYY-MM-DD HH:MM:SS.mmmmmm
    """

    return datetime.datetime.now().isoformat()
