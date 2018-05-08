#!/usr/bin/python

import json
from pprint import pprint

class ProjectCH():

    def __init__(self):
        print("ProjectCH created")
        self.entity_type = ""
        self.id = ""
        self.external_id = ""
        self.name = ""
        self.description = ""
	self.abbreviation =  ""
	self.color = ""
	self.iteration_length =  ""
        self.show_thermometer = ""
	self.days_to_thermometer = ""
	self.start_time = ""
	self.created_at =  ""
	self.updated_at = ""
	self.archived = ""
	self.follower_ids = []
	self.team_id = ""
	self.stats = [] 



    def json_string(self):
        return '{ "entity_type": "'          + str(self.entity_type) + \
                  '", "id":"'                   + str(self.id) + \
                  '", "external_id": "'         + str(self.external_id) + \
                  '", "name": "'                + str(self.name) + \
                  '", "description": "'         + str(self.description) + \
                  '", "abbreviation": "'        + str(self.abbreviation) + \
                  '", "color": "'               + str(self.color) + \
                  '", "iteration_lenght": "'    + str(self.iteration_length) + \
                  '", "show_thermometer": "'    + str(self.show_thermometer) + \
                  '", "days_to_thermometer": "' + str(self.days_to_thermometer) + \
                  '", "start_time": "'          + str(self.start_time)   + \
                  '", "created_at": "'          + str(self.created_at)   + \
                  '", "updated_at": "'          + str(self.updated_at)   + \
                  '", "archived": "'            + str(self.archived)     + \
                  '", "follower_ids": '        + str(self.follower_ids) + \
                  ', "team_id": "'             + str(self.team_id)      + \
                  '", "stats": '               + str(self.stats)  + '}'

'''

	"entity_type": "project",
	"id": 238,
	"external_id": null,
	"name": "Advisor Platform",
	"description": "Work related to keeping advisors happy.",
	"abbreviation": null,
	"color": "#4e0380",
	"iteration_length": 2,
	"show_thermometer": true,
	"days_to_thermometer": 5,
	"start_time": "2017-10-17T19:18:39Z",
	"created_at": "2017-10-17T19:18:39Z",
	"updated_at": "2017-10-18T23:04:27Z",
	"archived": false,
	"follower_ids": [],
	"team_id": 7,
	"stats": {
		"num_stories": 453,
		"num_points": 106
	}


'''

if __name__ == '__main__':
    test_project = ProjectCH()
    test_project.entity_type = "project"
    test_project.id = 238
    test_project.external_id = None
    test_project.name = "Advisor Platform"
    test_project.description = "Work related to keeping advisors happy."
    test_project.abbreviation = None
    test_project.color = "#4e0380"
    test_project.iteration_length = 2
    test_project.show_thermometer = True
    test_project.days_to_thermometer = 5
    test_project.start_time = "2017-10-17T19:18:39Z"
    test_project.created_at = "2017-10-17T19:18:39Z"
    test_project.updated_at = "2017-10-18T23:04:27Z"
    test_project.archived = False
    test_project.follower_ids = []
    test_project.team_id = 7 
    test_project.stats = [] 


    pprint(test_project.json_string())
