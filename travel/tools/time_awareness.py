from datetime import datetime,date


def current_date() -> date:
    """Function to return current date"""
    print("Running tool 'Current_date()'")
    return datetime.now().date()
