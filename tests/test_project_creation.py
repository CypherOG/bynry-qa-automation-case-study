from api.project_api import ProjectAPI

def test_project_creation():

    token = "sample_token"

    api = ProjectAPI(token)

    project = {

        "name":"Automation Project",

        "description":"Created by Automation",

        "team_members":[]
    }

    response = api.create_project(
        "company1",
        project
    )

    assert response.status_code == 200
