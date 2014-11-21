import re
import datetime


def make_datetime_struct(time_str):
    """
    take time string and make datetime structure
    """
    fmt = "%Y %m %d %H %M %S"
    time_struct = datetime.datetime.strptime(' '.join(re.split('-|:|\ ', time_str)), fmt)
    return time_struct


def get_time_range(d):
    """
    take in a dictionary
    """
    fmt = "%Y %m %d %H %M %S"
    #https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    minday = datetime.datetime.strptime(' '.join(re.split('-|:|\ ', min(d.keys()))), fmt)
    maxday = datetime.datetime.strptime(' '.join(re.split('-|:|\ ', max(d.keys()))), fmt)
    print minday, maxday
    return minday, maxday
