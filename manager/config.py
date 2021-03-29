import configparser
import os


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath('config.ini'))

    def get_user(self):
        return self.config.get("Users", "user")

    def get_job(self):
        return self.config.get("Users", "job")
