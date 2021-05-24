from suds.client import Client
from suds import WebFault
from fixture.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.1/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def project_list(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.1/api/soap/mantisconnect.php?wsdl")
        list = []
        try:
            project = client.service.mc_projects_get_user_accessible(username, password)
            for row in project:
                list.append(Project(project_name=row.name, project_description=row.description))
            return len(list)
        except WebFault:
            return False
