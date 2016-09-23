import csv     # imports the csv module
import sys      # imports the sys moduleimport time
from datetime import date
from datetime import datetime, timedelta


def  f(test):
    if test == "what":
        return None
    else:
        return "success"

mytest = f("what")
if mytest is not None:
    print "it's NOT None"

if mytest is None:
    print "no it's None"

# f = open("udp_project_0906.csv", 'rU') # opens the csv file
# reader = csv.reader(f, delimiter=',')  # creates the reader object with delimer comma
# for row in reader:   # iterates the rows of the file in order
#     #check to see if the milestone has an update
#     #process the last_update string into a date value
#     string_date = (row[4])
#     #check to see if there is a date value. Only process if there is anything else.
#     first_char = string_date[:1]
#     print "first char is %s" % first_char
#     if first_char.isdigit():
#         date = datetime.strptime(string_date, "%m/%d/%y")
#         type_date = type(date)
#         print "after datetime() %s" % type_date
#         print type_date
#         seven_days = date - timedelta(days=7)
#         print seven_days
