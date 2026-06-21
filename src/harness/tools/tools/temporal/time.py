import datetime


def get_current_date_time() -> str:
    """
    return the current system date-time as an iso-8601 format string

    Returns:
        A string corresponding to the current system date-time in ISO format YYYY-MM-DD HH:MM:SS.mmmmmm
    """

    return datetime.datetime.now().isoformat()


def get_day_of_week(iso8601_datum: str) -> str:
    """
    return the day of the week for the datum

    Args:
        datum: a datetime string in iso-8601 format (YYYY-MM-DD HH:MM:SS.mmmmmm)

    Returns:
        The corresponding day of the week, as a string
    """

    return datetime.datetime.fromisoformat(iso8601_datum).strftime("%A")
