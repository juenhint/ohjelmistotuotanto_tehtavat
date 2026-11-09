from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_toml['project']['name'], 
                       parsed_toml['project']['description'],
                       parsed_toml['project']['license'],
                       parsed_toml['project']['authors'], 
                       parsed_toml['project']['dependencies'], 
                       parsed_toml['dependency-groups']['dev'],
                       )
