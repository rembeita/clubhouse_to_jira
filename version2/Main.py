from ProjectCB import ProjectCB
import argparse
import sys
from pprint import pprint
import json
import ProjectCB

class Orchestrator():

    def __init__(self):
       self.all_projects = []
       self.project_cb_json = ""

    def project_load_clubhouse_json(self, json_cb_file):
        self.project_cb_json = json.load(open(self.projects_json_cb))
         

    def load_projects(self):
        jira_json = []
        for project_json in self.project_cb_json():
            project = ProjectCB()
            project.entity_type = project['entity_type']
            project.id = project['id']
            project.external_id = project['external_id']
            project.name =  project['name'] 
            project.description =  project['description']
            project.abbreviation =   project['abbreviation']
            project.color =  project['color']
            project.iteration_length =  project['iteration_length']
            project.show_thermometer =  project['show_thermometer']
            project.days_to_thermometer =  project['days_to_thermometer']
            project.start_time =  project['start_time']
            project.created_at =   project['created_at']
            project.updated_at =  project['updated_at']
            project.archived =  project['archived']
#            project.follower_ids = []
            project.team_id =  project['team_id']
#            project.stats = []
            self.all_projects.append(project)

if __name__ == "__main__":
    print("Executing main")
    parser = argparse.ArgumentParser()
    parser.add_argument('--projects', help='Just import on Jira the projects of Clubhouse', action='store_true')
    parser.add_argument('--projectsfile', help='The Json Clubhouse file with the projects')
    parser.add_argument('--outputfile', help='The Json Clubhouse file with the projects')
    args = parser.parse_args()

    if args.projects == None:
    	parser.print_help()
    	sys.exit(1)

    if args.projectsfile != None:
        mig_project = ProjectCB()
        mig_project.load_clubhouse_json(args.projectsfile)
        project_encoded = mig_project.convert_to_jira()
        mig_project.json_to_file(args.outputfile)
        pprint(project_encoded)


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

