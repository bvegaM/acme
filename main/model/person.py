class Person:

    def __init__(self,name:str,workweek:str): 
        self.name: str     = name
        self.workweek:str  = workweek.split(',')
        self.salary:float  = self.get_salary()
    
    def get_salary(self)-> float:
        if '' in self.workweek:
            print('{name} have not complete work week'.format(self.name))
        pass
    