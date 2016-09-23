import csv     # imports the csv module
import sys      # imports the sys module
from milestone import Milestone
class Parser:

    def __init__(self, instring):
        #print "start Myparser init"
        global filename
        filename = instring
        #print "end Myparser init filename: %s" % filename

    def start(self):
        allmilestones =[]
        f = open(filename, 'rU') # opens the csv file
        reader = csv.reader(f, delimiter=',')  # creates the reader object with delimer comma
        x = 0 #count and print the number of valid rows
        for row in reader:   # iterates the rows of the file in order
            if row[0] is not None:
                last_updated = str(row[4])
                print last_updated, x
                if last_updated[:1].isdigit():
                    print "\n\n*** Creating a MIlestone"
                    vertical = row[0]
                    milestone = Milestone(vertical,row) #create a milestone with current vertical
                    print milestone.milestonename
                    allmilestones.append(milestone)
                    x += 1
                else:
                    print "\n\n***** No Milestone for you!"
        f.close()      # closing

        # for a in allmilestones:
        #     print a.milestonename, "in parser start()"
        return allmilestones
