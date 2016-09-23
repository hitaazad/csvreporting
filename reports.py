from __future__ import generators
import random
import time
from datetime import date
from datetime import datetime, timedelta

# class ReportFactory:
#     def newReport(self, type):#(type):
#         #return eval(type + "()")
#         print "in Report factory"
#         if type == "markdown": return Markdown()
#         #if type == "pdf": return PDF()
#
#     # def __init__(self):
#     #     print "start Markdown init"
#     #     print "end Markdown init filename"

# TODO - next vs
# class Markdown(ReportFactory):
#     def __init__(self):
#
class Markdown:

    def __init__(self):#not sure if i should do the genreport() in init
        print "init Markdown"


    def genreport(self, allmilestones):
        #allmilesontes is a list of milestone objects, all with valid last_updated values
        report_type = "markdown"
        markdown_report = open(report_type, 'w') #create a file
        markdown_report.write("#User Data Protection Weekly Update (Week of _____)\n---")
        last_report_date = datetime.today() - timedelta(days=7) #to be used to confirm the milestone is a recent update

        current_vertical = None
        printed_verticals = []

        for i in allmilestones:
            current_vertical = i.vertical
            #track the milestones we have addressed
            if current_vertical not in printed_verticals:
                print i.vertical
                markdown_report.write("# %s\n" % current_vertical)#Write the Vertical Header to the file
                printed_verticals.append(current_vertical) #keep track of it vertical headers printed
            markdown_report.write("## %s - %s\n**[Completion ETA: %s - POC: %s]**\n**Summary:** %s\n\n" % (i.milestonename, i.milestone_status, i.completion_target_date, i.poc, i.highlight))


            # while in a given vertical, print milestones that have been updated since the last report (less than 7 days ago)

            #if i.last_updated >= seven_days:


            # Milestone Name - Status
            # Completion ETA: QQ'YY - POC: names
            # Summary:
                #

#determine when the last report was. Then exclude milestone highlights older than this value.
