from typing import Tuple,List

def get_name(text:str)->str:
    return text.split('=')[0]

def get_workweek(text:str)->str:
    return text.split('=')[1]

def get_acr_day(daywork:str)->str:
    return daywork[:2]

def get_range_hours(daywork:str)->str:
    return daywork[2:]

def get_start_end_time(range_hours:str)->List:
    range_hours = range_hours.split('-')       
    return range_hours

def convert_hour_in_decimal(hour_complete:str)->float:
    hour_complete = hour_complete.split(':')
    hour          = int(hour_complete[0])
    minute        = int(hour_complete[1])
    decimal_hour  = hour + minute/60
    return decimal_hour