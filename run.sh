#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo "File missing"
    exit 1
fi
python angalg_project.py $1
