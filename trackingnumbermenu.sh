#!/bin/bash
#Terminal Title
echo -en "\033]0;Tracking #s\a"
#Menu Prompt
PS3='Please enter your choice: '
#Options
options=("View Tracking #s" "Edit Tracking #s" "Quit")
#Menu Selection
select opt in "${options[@]}"
do
    case $opt in
	#Runs Tracking python script
        "View Tracking #s")
	    #Resets the terminal
	    reset
	    #Runs Tracking python script
            python3 opentracking.py
	    #Recreates the menu
            echo ""
            echo "1) ${options[0]}"
            echo "2) ${options[1]}"
            echo "3) ${options[2]}"
            ;;
        "Edit Tracking #s")
	    #opens the trackingnumbers document
            gedit trackingnumbers.txt
	    #Resets the terminal when done
	    reset
	    #Recreates the meny
            echo "1) ${options[0]}"
            echo "2) ${options[1]}"
            echo "3) ${options[2]}"
            ;;
        "Quit")
	    #Quits the script
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
