#!/usr/bin/python

import json
from pprint import pprint

class ProjectJira():

    def __init__(self):
        print("ProjectJira created")
        self.name = ""
        self.key = ""
        self.type = ""
        self.issues = []

    def json_string(self):
        return  '{ "name": "'           + str(self.name) + \
                  '", "key":"'          + str(self.key) + \
                  '", "type": "'        + str(self.type) + \
                  '", "issues": '       + str(self.issues) + \
                 '}'

'''
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

'''

if __name__ == '__main__':
    test_project = ProjectJira()
    test_project.name = "Sample data"
    test_project.key = "SAM"
    test_project.type = "software"
    test_project.issues = []

    pprint(test_project.json_string())
