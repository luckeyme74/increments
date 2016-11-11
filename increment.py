class Time(object):
    """represents the time of day in hours, minutes and seconds"""
t = Time()
t.second = 30
t.minute = 20
t.hour = 10
seconds = 60
def increment(t, seconds):
    t.second += seconds
    if t.second >= 60:
        t.second -= 60
        t.minute += 1
    if t.minute >= 60:
            t.minute -= 60
            t.hour += 1
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

increment(t, seconds)
