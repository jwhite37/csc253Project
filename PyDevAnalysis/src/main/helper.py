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


def datetime_from_delta(delta="00:30:00"):
    t0 = datetime.datetime.strptime("00 00 00", "%H %M %S")
    t = datetime.datetime.strptime(' '.join(re.split(':',delta)), "%H %M %S")
    return t - t0

def print_in_order(d):
    assert(type(d) == dict)
    keys = sorted(d.keys())
    for k in keys:
        print d[k]
        print '-' * 50, '\n'
