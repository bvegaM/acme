from main.utils import util


if __name__ == '__main__':
    text = 'RENE=MO10:00-12:02,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    start_time,end_time = util.get_start_end_time(util.get_range_hours(util.get_workweek(text).split(',')[0]))
    print(end_time)
    pass