#!/bin/bash



function __git(){
rama=$(git branch 2> /dev/null)
sirama=$?

if [ $sirama -eq 0 ]; then
    rama=$(git branch | grep "\*" | sed 's/* //')
    $(git status 2> /dev/null | grep "git add" >/dev/null)

    veri=$?

    if [ $veri -eq 0 ]; then
        verificacion="\e[1;31m✗"
    else
        verificacion="\e[1;32m✓"
    fi
    echo -e "\e[1;37m${rama} ${verificacion}"    
fi

#if [[ $sirama -eq 0 ]]; then
#    echo -e "\e[1;37m${rama} ${verificacion}"    
#fi
}


