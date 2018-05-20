#!/usr/bin/python

import json
from pprint import pprint

class StoryCH():

    def __init__(self):
    #    print("Story created")
        self.entity_type = ""
	self.archived = ""
	self.created_at =  ""
	self.updated_at = ""
        self.id = ""
        self.external_id = ""
        self.name = ""
        self.story_type = ""
        self.position = ""
        self.workflow_state_id = ""
        self.moved_at = ""
        self.started = ""
        self.started_at = ""
        self.started_at_override = ""
        self.completed = ""
        self.completed_at = ""
        self.completed_at_override = ""
        self.blocker = ""
        self.blocked = ""
        self.estimate = ""
        self.deadline = ""
        self.project_id = ""
        self.labels = []
        self.requested_by_id = ""
	self.owner_ids =  []
	self.follower_ids =  []
	self.mention_ids =  []
	self.epic_id = ""
	self.support_tickets =  ""
        self.external_tickets = ""
	self.story_links = ""
	self.app_url = ""
	self.comment_ids = []
	self.file_ids = ""
	self.linked_file_ids = [] 
	self.task_ids = [] 



    def json_string(self):
        return '{ "entity_type": "'          + str(self.entity_type) + \
                  '", "archived": "'            + str(self.archived)     + \
                  '", "created_at": "'          + str(self.created_at)   + \
                  '", "updated_at": "'          + str(self.updated_at)   + \
                  '", "id":"'                   + str(self.id) + \
                  '", "external_id": "'         + str(self.external_id) + \
                  '", "name": "'                + str(self.name) + \
                  '", "story_type": "'          + str(self.story_type) + \
                  '", "position": "'            + str(self.position) + \
                  '", "workflow_state_id": "'               + str(self.workflow_state_id) + \
                  '", "moved_at": "'    + str(self.moved_at) + \
                  '", "started": "'    + str(self.started) + \
                  '", "started_at": "'    + str(self.started_at) + \
                  '", "started_at_override": "'    + str(self.started_at_override) + \
                  '", "completed": "'    + str(self.completed) + \
                  '", "completed_at": "'    + str(self.completed_at) + \
                  '", "completed_at_override": "'    + str(self.completed_at_override) + \
                  '", "blocker": "' + str(self.blocker) + \
                  '", "blocked": "' + str(self.blocked) + \
                  '", "estimate": "'          + str(self.estimate)   + \
                  '", "deadline": "' + str(self.deadline) + \
                  '", "project_id": "' + str(self.project_id) + \
                  '", "labels": "' + str(self.labels) + \
                  '", "requested_by_id": "' + str(self.requested_by_id) + \
                  '", "owner_ids": "' + str(self.owner_ids) + \
                  '", "follower_ids": "'        + str(self.follower_ids) + \
                  '", "mention_ids": "' + str(self.mention_ids) + \
                  '", "epic_id": "' + str(self.epic_id) + \
                  '", "support_tickets": "' + str(self.support_tickets) + \
                  '", "external_tickets": "' + str(self.external_tickets) + \
                  '", "story_links": "' + str(self.story_links) + \
                  '", "app_url": "' + str(self.app_url) + \
                  '", "comment_ids": "' + str(self.comment_ids) + \
                  '", "file_ids": "' + str(self.file_ids) + \
                  '", "task_ids": '               + str(self.task_ids)  + '}'


'''

	"entity_type": "story",
	"archived": false,
	"created_at": "2017-10-10T01:20:15Z",
	"updated_at": "2017-10-18T21:50:05Z",
	"id": 68,
	"external_id": null,
	"name": "When an account has no account s linked, ui flashes a table which then dissapears",
	"story_type": "bug",
	"position": 2147876864,
	"workflow_state_id": 500000017,
	"moved_at": "2017-10-10T01:20:15Z",
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
	"app_url": "https:\/\/app.clubhouse.io\/stratifi\/story\/68",
	"comment_ids": [],
	"file_ids": [],
	"linked_file_ids": [],
	"task_ids": []

'''

if __name__ == '__main__':
    test_project = StoryCH()
    test_project.entity_type = "story"
    test_project.archived = False
    test_project.created_at = "2017-10-17T19:18:39Z"
    test_project.updated_at = "2017-10-18T23:04:27Z"
    test_project.id = 238
    test_project.external_id = None
    test_project.name = "When an account has no account s linked, ui flashes a table which then dissapears"
    test_project.story_type = "bug"
    test_project.position = "2147876864"
    test_project.workflow_state_id = "500000017"
    test_project.moved_at = "2017-10-10T01:20:15Z"
    test_project.started = False
    test_project.started_at = None
    test_project.started_at_override = None
    test_project.completed = False
    test_project.completed_at = None
    test_project.completed_at_override = None
    test_project.blocker = False
    test_project.blocked = False
    test_project.estimate = None
    test_project.deadline = None
    test_project.project_id = "6" 
    test_project.labels = []
    test_project.requested_by_id = "59d6c24e-6b0a-4d16-b40e-eee0a5bfe337"
    test_project.owner_ids = []
    test_project.project_id = "6" 
    test_project.follower_ids = []
    test_project.mention_ids = []
    test_project.epic_id = None 
    test_project.support_tickets = []
    test_project.external_tickets = []
    test_project.story_links = []
    test_project.app_url = "https:\/\/app.clubhouse.io\/stratifi\/story\/68"
    test_project.comment_ids = []
    test_project.file_ids = []
    test_project.linked_file_ids = []
    test_project.task_ids = []
 

    pprint(test_project.json_string())
