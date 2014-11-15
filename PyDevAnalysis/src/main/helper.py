def get_time_range(d):
	import re
	import datetime
	fmt = "%Y %m %d %H %M %S"
	#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
	minday = datetime.datetime.strptime(' '.join(re.split('-|:|\ ', min(d.keys()))), fmt)
	maxday = datetime.datetime.strptime(' '.join(re.split('-|:|\ ', max(d.keys()))), fmt)
	print minday, maxday
	return minday, maxday

	
