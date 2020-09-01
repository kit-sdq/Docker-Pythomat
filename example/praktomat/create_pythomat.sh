#!/bin/bash
#title          :create_pythomat.sh
#description    :This script will patch the pythomat folder for the current assignment
#author         :majuwa
#date           :20111101
#version        :0.2
#usage          :bash create_pythomat.sh
#notes          :Please execute in your assignment folder and a cleaned pyhtomatfolder should be available
#bash_version   :5.0
#requires       :dos2unix, zip


function create_pythomat_for_folder {
	#convert scripts to unix line ending
	find . -type f -print0 | xargs -0 dos2unix

	#check if copy contains terminal
	if [ ! -e copy/code/_intern/Terminal.java ] && [ ! -e copy/code/Terminal.java ]; then
	    cp ../../../../../BlattX/praktomat/TaskX/copy/code/Terminal.java copy/code/_intern/Terminal.java
	fi

	#checks if a pythomat archive exist
	if [ ! -e pythomat.zip ]; then
	    cp -r ../../../../../pythomat/pythomat2/pythomat pythomat
	    zip -r pythomat.zip pythomat
	    rm -rf pythomat
	fi

	#create resource folders and patch pythomat
	mkdir ressources
	cp -r copy ressources
	cp -r ../checkstyle ressources
	zip -r pythomat.zip ressources
	zip -r copy.zip copy
	rm -rf ressources

	#create archive with solutions
	TASK="${PWD##*/}"
	PATH_OUT='../../solution/'
	COMPLETE_PATH=$PATH_OUT$TASK
	cp -r $COMPLETE_PATH solution
	zip -r solution.zip solution
	rm -rf solution
}

for folder in `find . -maxdepth 1 -iname "Task*" -type d`
do
cd "$folder"
echo $PWD
create_pythomat_for_folder
cd ..
done