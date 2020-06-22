from datetime import datetime,date
from abc import abstractmethod


def calculating_days(issued_on):
    """This method calculates the days based
    on the latest created date and the date today"""
    days_difference = (
        datetime.strptime(str(date.today()), "%Y-%m-%d").date()
        - datetime.strptime(str(issued_on),  "%Y-%m-%d %H:%M:%S.%f").date()
    ).days

    return days_difference


def calculate_total_rent(data):

    total_rent = 0
    first_two_days = 2
    if len(data) == 0:
        return
    else:
        for i in range(len(data)):
            if data[i].books.book_type.name == "REGULAR":
                if calculating_days(data[i].issued_on)>2:
                    total_days = calculating_days(data[i].issued_on)
                    rent = data[i].quantity * (1 * first_two_days) + \
                           data[i].quantity * (total_days - first_two_days) + data[i].books.book_charge.value
                    total_rent = total_rent + rent
                    print(total_rent)
                else:
                    """Calculates the rent for reggie"""
                    total_days = calculating_days(data[i].issued_on)
                    rent = data[i].quantity * (total_days * data[i].min_book_charge.value)
                    total_rent = total_rent + rent
            if data[i].books.book_type.name == "NOVEL":
                 if calculating_days(data[i].issued_on) < 3:
                     total_days = calculating_days(data[i].issued_on)
                     rent = data[i].quantity * (total_days * data[i].min_book_charge.value)
                     total_rent = total_rent + rent
                 else:
                     total_days = calculating_days(data[i].issued_on)
                     rent = data[i].quantity * (total_days * data[i].books.book_charge.value)
                     total_rent = total_rent + rent

            else:
                total_days = calculating_days(data[i].issued_on)
                rent = data[i].quantity * (total_days * data[i].books.book_charge.value)
                total_rent = total_rent + rent
    return total_rent









