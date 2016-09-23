import sys
from parser import Parser
from reports import Markdown #ReportFactory,

print "***start program***"
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

report_type = str(sys.argv[1])
filename = str(sys.argv[2])
print "REPORT TYPE is *****%s*****" % report_type

parsefile = Parser(filename)
milestones = parsefile.start() #returns list of milestone objects
# for m in milestones:
#     print m.milestonename
report = Markdown() #TODO replace with Report factory and pass in sys.argv
report.genreport(milestones)
#report.newReport(report_type)
#report.genreport(milestones)

#sorted(milestones, key=attrgetter('risk'))


print "***end program***"
