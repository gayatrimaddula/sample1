import json
from jira import JIRA
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-m", "--months",dest="no_of_months",help="Tickets to be created for every no of months given", required=True)
args=parser.parse_args()
print args.no_of_months
authed_jira=JIRA(server='https://gayatritest.atlassian.net',basic_auth=('admin','s8985622575'))
fo = open("sample.json", "r+")
issue_dict=json.loads(fo.read())
issues_to_be_created = issue_dict.get(args.no_of_months)

for issue in issues_to_be_created:
	new_issue = authed_jira.create_issue(fields=issues_to_be_created[issue].get('issue_details'))
	print "Creating ", issue
	authed_jira.assign_issue(new_issue, issues_to_be_created[issue].get('issue_asignee'))
	fo.close()

print "Tickets created successfully"









#if args.no_of_months=="1":
#  for key,value in issue_dict.iteritems():
#    print issue_dict.get(args.no_of_months)
#Read from user monthly or yearly using argparse
#for key,value in issue_dict.iteritems():
 #if user gave monthly:
     #issue_dict.get('monthly')
     #for j,k in issue_dict.get('monthly'): 




       
