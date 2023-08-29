import json
import requests
from dnarest_constants import BASE_URL
import dna_token
import time

#Create Project
def create_project(token):
    headers = {"X-Auth-Token": token, "Content-Type":"application/json"}
    body={"name": "Jacobs Test Project 3", "description":"Test project created with DNAC API"}
    response = requests.post(BASE_URL+"/dna/intent/api/v1/template-programmer/project", headers=headers, json=body, verify=False)
    taskId=response.json()["response"]["taskId"]
    #Get TaskId
    print("Task submitted. Waiting to finish")
    time.sleep(15)
    taskStatus = requests.get(BASE_URL+f"/dna/intent/api/v1/task/{taskId}", headers=headers, verify=False)
    projectId = taskStatus.json()["response"]["data"]
    print(f"Sucessfully created project. Id is {projectId}")
    return projectId
#Create Template
#Test Template
#Version Template


def main():
    token=dna_token.get_token()
    create_project(token)



if __name__=="__main__":
    main()



