from datetime import datetime,date
from abc import abstractmethod


def calculating_days(issued_on):
    """This method calculates the days based
    on the latest created date and the date today"""
    days_difference = (
        datetime.datetime.strptime(str(date.today()), "%Y-%m-%d").date()
        - datetime.datetime.strptime(str(issued_on), "%Y-%m-%d").date()
    ).days

    return days_difference

@abstractmethod
def calculate_rent(duration,num_books):
    pass
