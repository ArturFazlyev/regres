import configparser
import os


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath('C:\\Users\\Артур\\Desktop\\regres\\config.ini'))

    def get_user(self):
        return self.config.get("Users", "user")

    def get_job(self):
        return self.config.get("Users", "job")

    def get_url(self):
        return self.config.get("Users", "url")

    def get_create_user(self):
        return self.config.get("Users", "create_user")