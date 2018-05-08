from ProjectCH import ProjectCH
from ProjectJira import ProjectJira
from StoryCH import StoryCH
import argparse
import sys
from pprint import pprint
import json

class Orchestrator():

    def __init__(self):
       self.all_projects_ch = []
       self.all_projects_jira = []
       self.all_stories_ch = []
       self.all_issues_jira = []
       self.project_cb_json = ""
       self.project_jira_json = ""
       self.stories_cb_json = ""

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

    def stories_load_clubhouse_json(self, json_cb_file):
        self.stories_cb_json = json.load(open(json_cb_file))
        ##pprint(self.project_cb_json) 

    def load_stories(self):
        for stories_json in self.stories_cb_json:
            story = StoryCH()
            story.entity_type = project_json['entity_type']
            story.id = project_json['id']
            story.external_id = project_json['external_id']
            story.name =  project_json['name'] 
            story.description =  project_json['description']
            story.abbreviation =   project_json['abbreviation']
            story.color =  project_json['color']
            story.iteration_length =  project_json['iteration_length']
            story.show_thermometer =  project_json['show_thermometer']
            story.days_to_thermometer =  project_json['days_to_thermometer']
            story.start_time =  project_json['start_time']
            story.created_at =   project_json['created_at']
            story.updated_at =  project_json['updated_at']
            story.archived =  project_json['archived']
            story.follower_ids = []
            story.team_id =  project_json['team_id']
            story.stats = []
            self.all_stories_ch.append(project)
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
         

if __name__ == "__main__":
    print("Executing main")
    parser = argparse.ArgumentParser()
    parser.add_argument('--projects', help='Just import on Jira the projects of Clubhouse', action='store_true')
    parser.add_argument('--projectsfile', help='The Json Clubhouse file with the projects')
    parser.add_argument('--projoutputfile', help='The Json Output file with the projects for Jira')
    parser.add_argument('--stories', help='Import on Jira the Stories of Clubhouse', action='store_true')
    parser.add_argument('--storiesfile', help='The Json Clubhouse file with the stories')
    parser.add_argument('--storyoutputfile', help='The Json Output file with the issues for Jira')
    args = parser.parse_args()

    if args.projects == None:
    	parser.print_help()
    	sys.exit(1)

    if args.projectsfile != None:
        mig_project = Orchestrator()
        mig_project.project_load_clubhouse_json(args.projectsfile)
        project_list_ch = mig_project.load_projects()
        project_list_jira = mig_project.create_jira_projects()
        print(' { "projects": [  ')
        for i in range(0,len(project_list_jira)):
            if (i == len(project_list_jira) - 1):
                print(project_list_jira[i].json_string())
            else:
                print(project_list_jira[i].json_string() + ",")
                
        print(' ] }  ')
#        pprint(project_encoded)


#test_project = ProjectCB()
#test_project.load_clubhouse_json('clubhouse_data/projects.json')
#project_encoded = test_project.convert_to_jira()
#test_project.json_to_file('jira_json/projects.json')
#pprint(project_encoded)


#    args = parser.parse_args()
#    parser.add_argument('--secret', help='Select the secret to retrieve. E.g. secret/database')
#    parser.add_argument('--vault-url', help='Override vault URL. E.g. http://172.16.12.184:8200')
#    parser.add_argument('--username', help='Username for E.g. vault-api')
#    parser.add_argument('--password', help='Password E.g. M3r1d1an')
#    parser.add_argument('--trusted-url', help='URL of the TrustedEntity for E.g. http://172.16.12.184')
#    args = parser.parse_args()
#    
#    if args.secret == None:
#    	parser.print_help()
#    	sys.exit(1)
#    
#    if args.trusted_url != None:
#    	endpointauth = args.trusted_url 
#    if args.vault_url != None:
#    	vault_url = args.vault_url	
#    if args.username != None:
#    	username = args.username
#    if args.password != None:
#    	password = args.password
#    
#    param = args.secret
#    controller = Controller()
#    one_time_token = controller.getToken(username, password, endpoint, endpointauth)
#    vault = Vault(vault_url, one_time_token)
#    cred = vault.getCredentials(param)
#    print(cred)	

