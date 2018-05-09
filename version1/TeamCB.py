#!/usr/bin/python

import json
from pprint import pprint

class TeamCB():

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
            jira_json_unit['status'] = json_line['name']
            jira_json_unit['key'] = str(json_line['name'])[:3].upper() + str(json_line['id'])
            jira_json_unit['reporter'] = 'software'
            jira_json_unit['summary'] = 'software'
            jira_json_unit['externalId'] = 'software'
            jira_json.append(jira_json_unit)
            

        self.jira_json_resp = json.dumps(jira_json_dict, ensure_ascii=False)
        return self.jira_json_resp


    def json_to_file(self, dest_file):
        with open(dest_file, 'w') as outfile:
            outfile.write(self.jira_json_resp)



'''


{
	"entity_type": "team",
	"id": 7,
	"created_at": "2017-10-05T23:42:33Z",
	"updated_at": "2017-10-05T23:42:33Z",
	"name": "Engineering",
	"description": "Engineering",
	"position": 2,
	"project_ids": [239, 4569, 1293, 43, 235, 230, 236, 238, 237, 6],
	"workflow": {
		"entity_type": "workflow",
		"id": 500000015,
		"created_at": "2017-10-05T23:42:33Z",
		"updated_at": "2017-11-02T02:02:16Z",
		"name": "Default",
		"description": "",
		"team_id": 7,
		"default_state_id": 500000017,
		"auto_assign_owner": true,
		"states": [{
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": null,
			"name": "Unscheduled",
			"num_stories": 109,
			"type": "unstarted",
			"updated_at": "2017-10-05T23:42:33Z",
			"id": 500000017,
			"position": 0,
			"created_at": "2017-10-05T23:42:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": null,
			"name": "Ready for Development",
			"num_stories": 41,
			"type": "unstarted",
			"updated_at": "2017-10-05T23:42:33Z",
			"id": 500000016,
			"position": 1,
			"created_at": "2017-10-05T23:42:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "",
			"name": "High Priority",
			"num_stories": 5,
			"type": "unstarted",
			"updated_at": "2017-10-18T23:18:16Z",
			"id": 500000032,
			"position": 2,
			"created_at": "2017-10-18T23:17:31Z"
		}, {
			"description": "Things that need to be fixed and push to production as soon as possible.",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "",
			"name": "Hotfix",
			"num_stories": 0,
			"type": "unstarted",
			"updated_at": "2017-10-25T16:34:33Z",
			"id": 500000063,
			"position": 3,
			"created_at": "2017-10-25T16:34:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "start",
			"name": "In Development",
			"num_stories": 42,
			"type": "started",
			"updated_at": "2017-10-05T23:42:33Z",
			"id": 500000021,
			"position": 4,
			"created_at": "2017-10-05T23:42:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "",
			"name": "Ready to Review",
			"num_stories": 8,
			"type": "started",
			"updated_at": "2017-11-02T02:01:58Z",
			"id": 500000019,
			"position": 5,
			"created_at": "2017-10-05T23:42:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "",
			"name": "Ready to QA",
			"num_stories": 34,
			"type": "started",
			"updated_at": "2017-11-02T02:02:07Z",
			"id": 500000022,
			"position": 6,
			"created_at": "2017-10-05T23:44:04Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": "finish",
			"name": "Ready to Deploy",
			"num_stories": 1,
			"type": "started",
			"updated_at": "2017-11-02T02:02:16Z",
			"id": 500000020,
			"position": 7,
			"created_at": "2017-10-05T23:42:33Z"
		}, {
			"description": "",
			"entity_type": "workflow-state",
			"color": "",
			"verb": null,
			"name": "Completed",
			"num_stories": 691,
			"type": "done",
			"updated_at": "2017-10-05T23:42:33Z",
			"id": 500000018,
			"position": 9,
			"created_at": "2017-10-05T23:42:33Z"
		}]
	}



'''

#test_project = ProjectCB()
#test_project.load_clubhouse_json('clubhouse_data/projects.json')
#project_encoded = test_project.convert_to_jira()
#test_project.json_to_file('jira_json/projects.json')
#pprint(project_encoded)
