import sys
import os
from github import Github

path = "/ruta/del/proyecto/" #ruta para guardar los proyectos

username = "" #usuario de GitHub
password = "" #Contraseña de GitHub

def create():
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[1])
    print("Repositorio creado {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
