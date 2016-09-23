import time
from datetime import date
from datetime import datetime
import sys      # imports the sys moduleimport time

class Milestone:

    def __init__(self, vertical, row):
        print "Milestone: okay we are in Milestone claass"
        self.vertical = row[0]
        self.milestonename = row[1]
        self.milestone_status = row[2]
        self.completion_target_date = row[3]
        #prepare date field
        last_updated = row[4]
        self.last_updated = datetime.strptime(last_updated, "%m/%d/%y")             # Turn the value from a string to a date
        self.highlight = row[5] # row 5 = Highlight
        self.risk = row[6]    # row 6 = Gap
        self.poc = row[7]    # row 7 = People
        print self.milestonename
        print self.last_updated
        
        # other items to include in future
        # self.impact = impact
        # self.notes = notes

    # def __repr__(self):
    #     return '{}: {} {}'.format(self.vertical,
    #                               self.milestonename,
    #                               self.milestone_status,
    #                               self.completion_target_date,
    #                               self.last_updated,
    #                               self.highlight,
    #                               self.risk,
    #                               self.poc)


#['Vertical', 'Goal', 'Workstreams', 'Workstream Status', 'Completion Target', 'updated,'''Highlight', 'Gap', 'People', '']
