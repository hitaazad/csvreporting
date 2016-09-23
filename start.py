from myparser import Myparser
from markdown import Markdown

print "start program"
parsefile = Myparser("udp_project_0906.csv")
milestones = parsefile.start()
print milestones[1].vertical

report = Markdown()
report.genmarkdown(milestones)

print "end program"
