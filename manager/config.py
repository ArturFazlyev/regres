import configparser
import os
config = configparser.ConfigParser()
config.read(os.path.abspath("../setting/config.ini"))
URL = config.get("Users", "url")
USER = config.get("Users", "user")
JOB = config.get("Users", "job")
CREATE_USER = config.get("Users", "create_user")