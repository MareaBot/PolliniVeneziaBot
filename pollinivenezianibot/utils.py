import datetime


def get_monday() -> datetime.datetime:
    today = datetime.date.today()
    return today - datetime.timedelta(days=today.weekday())
