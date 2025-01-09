from datetime import datetime as dt, timedelta
from calendar import weekday


def check_input(element):
    try:
        dt.strptime(element, "%Y.%m.%d")
        return True
    except:
        return False


def count_mondays(valid_element):
    current_date = dt.now()
    valid_element_date = dt.strptime(valid_element, "%Y.%m.%d")

    num_days = (current_date - valid_element_date).days
    num_mondays = 0

    for i in range(num_days + 1):
        temporary_date = valid_element_date + timedelta(days=i)
        if temporary_date.weekday() == 0:
            num_mondays += 1

    return num_mondays


def main(list):
    for i in list:
        if check_input(i):
            print(count_mondays(i))
            break
