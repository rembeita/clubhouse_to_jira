#!/usr/bin/python

import json
from pprint import pprint

class ProjectCB():

    def __init__(self):
        print("object created")


    def load_clubhouse_json(self, projects_json_cb):
        self.projects_json_cb = projects_json_cb
        self.encoded_json_cb = json.load(open(self.projects_json_cb))
        #pprint(self.encoded_json_cb)
#        pprint(self.encoded_json_cb[0]['name'])



    def convert_to_jira(self):

        jira_json = []
        for json_line in self.encoded_json_cb:
            jira_json_unit = {}
            jira_json_unit['name'] = json_line['name']
            jira_json_unit['key'] = str(json_line['name'])[:3].upper() + str(json_line['id'])
            jira_json_unit['type'] = 'software'
            jira_json_unit['issues'] = []
            jira_json.append(jira_json_unit)
            

        jira_json_dict = {}
        jira_json_dict['projects'] = jira_json
#        pprint(jira_json_dict)
        self.jira_json_resp = json.dumps(jira_json_dict, ensure_ascii=False)
        return self.jira_json_resp


    def json_to_file(self, dest_file):
        with open(dest_file, 'w') as outfile:
            outfile.write(self.jira_json_resp)


'''
{
    "projects": [
        {
            "name": "Sample data",
            "key": "SAM",
			"type": "software",
            "issues": [
                {
					"key" : "SAM-123",
                    "status" : "Open",
                    "reporter" : "admin",
                    "summary" : "Parent case",
                    "externalId": "123"
                }
            ]
        }
    ]
}

'''

#test_project = ProjectCB()
#test_project.load_clubhouse_json('clubhouse_data/projects.json')
#project_encoded = test_project.convert_to_jira()
#test_project.json_to_file('jira_json/projects.json')
#pprint(project_encoded)
