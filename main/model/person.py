from main.utils import util
from main.model.day import Day

class Person:

    def __init__(self,name:str,workweek:str): 
        self.name: str     = name
        self.workweek:str  = workweek.split(',')
        self.salary:float  = self.get_salary()
    
    def get_salary(self)->float:
        if '' in self.workweek:
            print('{name} have not complete work week'.format(self.name))
        
        salary=0
        for workday in self.workweek:
            acr_day             = util.get_acr_day(workday)
            start_time,end_time = util.get_start_end_time(util.get_range_hours(workday))
            start_time          = util.convert_hour_in_decimal(start_time)
            end_time            = util.convert_hour_in_decimal(end_time)
            day                 = Day(start_time,end_time,acr_day)
            salary+=day.cost_day
        return salary