import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[1])
    print("Repositorio creado {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()


#no funciona