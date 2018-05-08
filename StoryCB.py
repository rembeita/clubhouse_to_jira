#!/usr/bin/python

import json
from pprint import pprint
import re

class StoryCB():

    def __init__(self):
        print("object created")


    def load_clubhouse_json(self, projects_json_cb):
        self.projects_json_cb = projects_json_cb
        self.encoded_json_cb = json.load(open(self.projects_json_cb))
        #pprint(self.encoded_json_cb)
#        pprint(self.encoded_json_cb[0]['name'])



    def convert_to_jira(self):
        completed_list = ['500000018', '500000037', '500000143', '500000393', '500000675']
        jira_json = []
        for json_line in self.encoded_json_cb:
            jira_json_unit = {}
            if json_line['workflow_state_id'] in completed_list:
                jira_json_unit['status'] = 'Completed'
            else:
                jira_json_unit['status'] = 'Open'
            #jira_json_unit['key'] = str(json_line['name'])[:3].upper() + str(json_line['id'])
            jira_json_unit['reporter'] = 'rodrigo'
            #print(json_line['name'])
            cleanString = re.sub('[^A-Za-z0-9 ]+','', json_line['name'])
            jira_json_unit['summary'] = cleanString
            jira_json_unit['description'] = cleanString
            jira_json_unit['externalId'] =  str(json_line['id'])
            jira_json.append(jira_json_unit)
            

        self.jira_json_resp = json.dumps(jira_json, ensure_ascii=False)
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


"entity_type": "story",
	"archived": false,
	"created_at": "2017-10-10T16:29:38Z",
	"updated_at": "2017-10-18T21:50:12Z",
	"id": 92,
	"external_id": null,
	"name": "Clicking on sort by accounts causes back api call",
	"story_type": "bug",
	"position": 2147942400,
	"workflow_state_id": 500000017,
	"moved_at": "2017-10-10T16:29:38Z",
	"started": false,
	"started_at": null,
	"started_at_override": null,
	"completed": false,
	"completed_at": null,
	"completed_at_override": null,
	"blocker": false,
	"blocked": false,
	"estimate": null,
	"deadline": null,
	"project_id": 6,
	"labels": [],
	"requested_by_id": "59d6c24e-6b0a-4d16-b40e-eee0a5bfe337",
	"owner_ids": [],
	"follower_ids": ["59d6c24e-6b0a-4d16-b40e-eee0a5bfe337"],
	"mention_ids": [],
	"epic_id": null,
	"support_tickets": [],
	"external_tickets": [],
	"story_links": [],
	"app_url": "https:\/\/app.clubhouse.io\/stratifi\/story\/92",
	"comment_ids": [],
	"file_ids": [91],
	"linked_file_ids": [],
	"task_ids": []

'''


if __name__ == "__main__":
    test_project = StoryCB()
    test_project.load_clubhouse_json('clubhouse_data/stories.bugs.json')
    project_encoded = test_project.convert_to_jira()
    test_project.json_to_file('jira_json/stories.bugs.json')
    pprint(project_encoded)
