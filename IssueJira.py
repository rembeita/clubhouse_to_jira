#!/usr/bin/python

import json
from pprint import pprint

class IssueJira():

    def __init__(self):
#        print("Issue created")
        self.priority = ""
	self.description = ""
	self.status =  ""
	self.reporter = ""
        self.labels = []
        self.watchers = []
	self.issueType = ""
        self.resolution = ""
        self.created = ""
        self.updated = ""
        self.affectedVersions = []
        self.summary = ""
        self.asignee = ""
        self.fixedVersions = []
        self.components = []
        self.externalId = ""
        self.history = []
        self.customFieldValues = []
        self.attachments = []



    def json_string(self):
        return '{ "priority": "'          + str(self.priority) + \
                  '", "description": "'            + str(self.description)     + \
                  '", "status": "'          + str(self.status)   + \
                  '", "reporter": "'          + str(self.reporter)   + \
                  '", "watchers":'                   + str(self.watchers) + \
                  ', "issueType": "'         + str(self.issueType) + \
                  '", "resolution": "'                + str(self.resolution) + \
                  '", "created": "'          + str(self.created) + \
                  '", "updated": "'            + str(self.updated) + \
                  '", "affectedVersions": '               + str(self.affectedVersions) + \
                  ', "summary": "'    + str(self.summary) + \
                  '", "asignee": "'    + str(self.asignee) + \
                  '", "fixedVersions": '    + str(self.fixedVersions) + \
                  ', "components": '    + str(self.components) + \
                  ', "externalId": "'    + str(self.externalId) + \
                  '", "history": '    + str(self.history) + \
                  ', "customFieldValues": '    + str(self.customFieldValues) + \
                  ', "attachments": '               + str(self.attachments)  + '}'


'''
"issues": [
                {
                    "priority" : "Major",
                    "description" : "Some nice description here\nMaybe _italics_ or *bold*?",
                    "status" : "Closed",
                    "reporter" : "alice",
                    "labels" : [ "impossible", "to", "test" ],
                    "watchers" : [ "bob" ],
                    "issueType" : "Bug",
                    "resolution" : "Resolved",
                    "created" : "2012-08-31T17:59:02.161+0100",
                    "updated" : "P-1D",
                    "affectedVersions" : [ "1.0" ],
                    "summary" : "My chore for today",
                    "assignee" : "bob",
                    "fixedVersions" : [ "1.0", "2.0" ],
                    "components" : ["Component", "AnotherComponent"],
                    "externalId" : "1",
                    "history" : [
                        {
                            "author" : "alice",
                            "created": "2012-08-31T15:59:02.161+0100",
                            "items": [
                                {
                                    "fieldType" : "jira",
                                    "field" : "status",
                                    "from" : "1",
                                    "fromString" : "Open",
                                    "to" : "5",
                                    "toString" : "Resolved"
                                }
                            ]
                        }
                    ],
                    "customFieldValues": [
                        {
                            "fieldName": "Story Points",
                            "fieldType": "com.atlassian.jira.plugin.system.customfieldtypes:float",
                            "value": "15"
                        },
                        {
                            "fieldName": "Business Value",
                            "fieldType": "com.atlassian.jira.plugin.system.customfieldtypes:float",
                            "value": "34"
                        }
                    ],
                    "attachments" : [
                        {
                            "name" : "battarang.jpg",
                            "attacher" : "admin", 
                            "created" : "2012-08-31T17:59:02.161+0100",
                            "uri" : "http://optimus-prime/~batman/images/battarang.jpg",
							"description" : "This is optimus prime"
                        }
                    ]        
'''

if __name__ == '__main__':
    test_project = IssueJira()
    test_project.priority = "Major"
    test_project.description = "Some nice description here\nMaybe _italics_ or *bold*?"
    test_project.status = "Closed"
    test_project.reporter = "alice"
    test_project.labels = []
    test_project.watchers = []
    test_project.issueType = ""
    test_project.resolution = ""
    test_project.created = "2012-08-31T17:59:02.161+0100"
    test_project.updated = "P-1D"
    test_project.affectedVersions = []
    test_project.summary = "My chore for today"
    test_project.assignee = "bob"
    test_project.fixedVersions = []
    test_project.components = []
    test_project.externalId = "1"
    test_project.history = []
    test_project.customFieldValues = []
    test_project.attachments = []


    pprint(test_project.json_string())

