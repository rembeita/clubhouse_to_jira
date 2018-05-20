from ProjectCH import ProjectCH
from ProjectJira import ProjectJira
from StoryCH import StoryCH
from IssueJira import IssueJira
import argparse
import sys
from pprint import pprint
import json

class Orchestrator():

    def __init__(self):
       self.project_stratifi = []
       self.all_projects_ch = []
       self.all_projects_jira = []
       self.all_stories_ch = []
       self.all_issues_jira = []
       self.project_cb_json = ""
       self.project_jira_json = ""
       self.stories_cb_json_bugs = ""
       self.stories_cb_json_features = ""
       self.stories_cb_json_chores = ""

    def project_load_clubhouse_json(self, json_cb_file):
        self.project_cb_json = json.load(open(json_cb_file))
        ##pprint(self.project_cb_json) 

    def load_projects(self):
        for project_json in self.project_cb_json:
            project = ProjectCH()
            project.entity_type = project_json['entity_type']
            project.id = project_json['id']
            project.external_id = project_json['external_id']
            project.name =  project_json['name'] 
            project.description =  project_json['description']
            project.abbreviation =   project_json['abbreviation']
            project.color =  project_json['color']
            project.iteration_length =  project_json['iteration_length']
            project.show_thermometer =  project_json['show_thermometer']
            project.days_to_thermometer =  project_json['days_to_thermometer']
            project.start_time =  project_json['start_time']
            project.created_at =   project_json['created_at']
            project.updated_at =  project_json['updated_at']
            project.archived =  project_json['archived']
#            project.follower_ids = []
            project.team_id =  project_json['team_id']
#            project.stats = []
            self.all_projects_ch.append(project)
        return self.all_projects_ch

    def stories_load_clubhouse_json_bugs(self, json_cb_file):
        self.stories_cb_json_bugs = json.load(open(json_cb_file))
        ##pprint(self.project_cb_json) 
    
    def stories_load_clubhouse_json_chores(self, json_cb_file):
        self.stories_cb_json_chores = json.load(open(json_cb_file))
        ##pprint(self.project_cb_json) 
    
    def stories_load_clubhouse_json_features(self, json_cb_file):
        self.stories_cb_json_features = json.load(open(json_cb_file))

    def load_stories(self, stories):
#        for story_json in self.stories_cb_json:
        for story_json in stories:
            story = StoryCH()
            story.entity_type = story_json['entity_type']
	    story.archived = story_json['archived']
	    story.created_at =  story_json['created_at']
	    story.updated_at = story_json['updated_at']
            story.id = story_json['id']
            story.external_id = story_json['external_id']
            story.name = story_json['name']
            story.story_type = story_json['story_type']
            story.position = story_json['position']
            story.workflow_state_id = story_json['workflow_state_id']
            story.moved_at = story_json['moved_at']
            story.started = story_json['started']
            story.started_at = story_json['started_at']
            story.started_at_override = story_json['started_at_override']
            story.completed = story_json['completed']
            story.completed_at = story_json['completed_at']
            story.completed_at_override = story_json['completed_at_override']
            story.blocker = story_json['blocker']
            story.blocked = story_json['blocked']
            story.estimate = story_json['estimate']
            story.deadline = story_json['deadline']
            story.project_id = story_json['project_id']
            story.labels = story_json['labels']
            story.requested_by_id = story_json['requested_by_id']
	    story.owner_ids =  story_json['owner_ids']
	    story.follower_ids =  story_json['follower_ids']
	    story.mention_ids =  story_json['mention_ids']
	    story.epic_id = story_json['epic_id']
	    story.support_tickets =  story_json['support_tickets']
            story.external_tickets = story_json['external_tickets']
	    story.story_links = story_json['story_links']
	    story.app_url = story_json['app_url']
	    story.comment_ids = story_json['comment_ids']
	    story.file_ids = story_json['file_ids']
	    story.linked_file_ids = story_json['linked_file_ids']
	    story.task_ids = story_json['task_ids']
            self.all_stories_ch.append(story)
        return self.all_stories_ch

    def create_jira_projects(self):
        for project_ch in self.all_projects_ch:
            project_jira = ProjectJira()
            project_jira.name = project_ch.name 
            project_jira.key =  str(project_ch.name)[:3].upper() + str(project_ch.id)
            project_jira.type = "software"
            project_jira.issues = []
            self.all_projects_jira.append(project_jira)

        return self.all_projects_jira
         
    def create_jira_issues(self):
        for story_ch in self.all_stories_ch:
              
            issue_jira = IssueJira()
            issue_jira.priority = "Major"
            #print(story_ch.name)
	    issue_jira.description = self.delete_special_chars(story_ch.name) 
            if story_ch.completed == False:
	        issue_jira.status =  "Open"
            else:
	        issue_jira.status =  "Closed"
                
	    issue_jira.reporter = "rodrigo"
            issue_jira.labels = []
            issue_jira.watchers = []
            if (self.delete_special_chars(story_ch.story_type).capitalize() == "Bug"):
	        #issue_jira.issueType = self.delete_special_chars(story_ch.story_type).capitalize()
	        issue_jira.issueType = "Bug" 
            else:
	        issue_jira.issueType = "Story" 
                
	    #issue_jira.issueType = "Bug"
            issue_jira.resolution = ""
            issue_jira.created = story_ch.created_at
            issue_jira.updated = story_ch.updated_at
            issue_jira.affectedVersions = []
            issue_jira.summary = self.delete_special_chars(story_ch.name)
            issue_jira.asignee = ""
            issue_jira.fixedVersions = []
            issue_jira.components = []
            issue_jira.externalId = ""
            issue_jira.history = []
            issue_jira.customFieldValues = []
            issue_jira.attachments = []
            self.all_issues_jira.append(str(issue_jira.json_string()))

        return self.all_issues_jira


    def delete_special_chars(self, word):
        return str(word.encode('ascii','ignore')).replace("'","").replace("[","").replace("]","").replace("\\","").replace('"','').replace("(","").replace(")","").replace(":","").replace(",","").replace("."," "). replace("_"," "). replace("\n","")

    def create_cb_project_on_jira(self):
        project_jira = ProjectJira()
        project_jira.name = "Clubhouse History"
        project_jira.key =  "CB123"
        project_jira.type = "software"
        project_jira.issues = "[" + ','.join(self.create_epics_from_projects()) #+ "]"
        self.project_stratifi.append(project_jira)
        return self.project_stratifi
 
    def create_epics_from_projects(self):
        issues_epics = []
        for project_ch in self.all_projects_ch:
            issue_jira = IssueJira()
            issue_jira.priority = "Medium"
            issue_jira.summary = project_ch.name 
            issue_jira.status = "Open"
            issue_jira.reporter = "rodrigo"
            issue_jira.issueType = "Epic"
            issue_jira.watchers = []
            issue_jira.customFieldValues = '[ { "fieldName": "Epic Name", "fieldType": "com.pyxis.greenhopper.jira:gh-epic-label", "value": " ' + self.delete_special_chars(project_ch.name) + '" } ]'
            issue_jira.created = project_ch.created_at
            issue_jira.updated = project_ch.updated_at
            issue_jira.description = str(project_ch.description).replace('"','')
            issues_epics.append(issue_jira.json_string())
        return issues_epics

if __name__ == "__main__":
    #print("Executing main")
    parser = argparse.ArgumentParser()
    parser.add_argument('--projects', help='Just import on Jira the projects of Clubhouse', action='store_true')
    parser.add_argument('--stories', help='Import on Jira the Stories of Clubhouse', action='store_true')
    parser.add_argument('--projectsfile', help='The Json Clubhouse file with the projects')
    #parser.add_argument('--outputfile', help='The Json Output file with the projects for Jira')
    #parser.add_argument('--storiesfile', help='The Json Clubhouse file with the stories')
    args = parser.parse_args()

    if args.projects == None and arg.stories == None:
    	parser.print_help()
    	sys.exit(1)

    #if args.projectsfile != None:
    mig_project = Orchestrator()
    mig_project.project_load_clubhouse_json("clubhouse_data/projects.json")
    project_list_ch = mig_project.load_projects()
    project_list_jira = mig_project.create_jira_projects()
    
#    if args.projectsfile != None:
#        mig_project = Orchestrator()
#        mig_project.stories_load_clubhouse_json_bugs(args.storiesfile)
    if args.stories:
        mig_project.stories_load_clubhouse_json_bugs("clubhouse_data/stories.bugs.json")
        mig_project.stories_load_clubhouse_json_chores("clubhouse_data/stories.chores.json")
        mig_project.stories_load_clubhouse_json_features("clubhouse_data/stories.features.json")
        mig_project.load_stories(mig_project.stories_cb_json_bugs)
        mig_project.load_stories(mig_project.stories_cb_json_chores)
        mig_project.load_stories(mig_project.stories_cb_json_features)
        issues_list_jira = mig_project.create_jira_issues()
#        print(' { "projects": [  ')
#        for i in range(0,len(project_list_jira)):
#            if (i == len(project_list_jira) - 1):
#                print(project_list_jira[i].json_string())
#            else:
#                print(project_list_jira[i].json_string() + ",")
#        print(' ] }  ')

        clubhouse_mig = mig_project.create_cb_project_on_jira()
        print(' { "projects": [  ')
        for i in range(0,len(clubhouse_mig)):
            print(clubhouse_mig[i].json_string() + ",")
        for i in range(0,len(issues_list_jira)):
            if (i == len(issues_list_jira) - 1):
                print(issues_list_jira[i] )
#                print(issues_list_jira[i].json_string())
            else:
                print(issues_list_jira[i] + ",")
        print(' ] }  ] }')
#        pprint(project_encoded)


