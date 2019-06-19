#!/bin/bash

function create() {
    cd
    source .env
    python3 create.py $1
    cd $FILEPATH$1 #ruta para guardar los proyectos
    git init
    git remote add origin git@github.com:$USERNAME/$1.git #cambiar el nombre de usuario
    touch README.md
    git add .
    git commit -m "Commit inicial"
    git push -u origin master
    code . #remover esta linea si no usa visual studio code
}
