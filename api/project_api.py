from api.api_client import APIClient

class ProjectAPI(APIClient):

    def create_project(self, tenant, project):

        self.headers["X-Tenant-ID"] = tenant

        return self.post(
            "/projects",
            project
        )
