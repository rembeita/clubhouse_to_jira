from ProjectCB import ProjectCB
import argparse
import sys
from pprint import pprint

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

