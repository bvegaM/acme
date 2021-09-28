
class Day:

    def __init__(self,start_time:float,end_time:float,day:str):
        self.start_time:float = start_time
        self.end_time:float   = end_time
        self.day:str          = day
        self.type_day:str     = self._get_type_day()

    def _get_type_day(self):
        pass    

    def get_cost_day(self):
        pass