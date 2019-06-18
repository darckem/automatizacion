#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd /ruta/del/proyeto/$1 #ruta para guardar los proyectos
    git init
    git remote add origin git@github.com:User/$1.git #cambiar el nombre de usuario
    touch README.md
    git add .
    git commit -m "inicio"
    git push -u origin master
    code . #remover esta linea si no usa visual studio code
}
