#Note: change 'firefox' to your default browser

#Imports required items
import os
import webbrowser
import time

#Option variable
tra=""

#Opens tracking number text file
file1 = open('trackingnumbers.txt', 'r')

#Starts Reading file
Lines = file1.readlines() 

#Used for first run
count = 0

#Reads file line by line
for line in Lines:

	#Splits the line into an array
	larr=line.split(':')

	#Looks for the the phrase ship
	if larr[2].find("ship") == 0:

		#Prints out the item name and the tracking number
		print(larr[0]+": " + larr[1])

		#If a bluecare tracking number is found sets the variable for the bluecare url
		if line.find(":BCELC") > 0:
			tra="blue"

		#If a parcelsapp tracking number is found sets the variable for the parcelsapp url
		if line.find(":UJ") > 0:
			tra="parc"

		#If the tra variable is empty then opens USPS
		if tra=="":

			#Checks to see if first run
			if count == 0:
				#Opens a new browser
				webbrowser.get('firefox').open_new("https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&&tLc=2&text28777=&tLabels="+ str(larr[1]))
				count = 1
			else:
				#Opens a new tab
				webbrowser.get('firefox').open_new_tab("https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&&tLc=2&text28777=&tLabels="+ str(larr[1]))

		#If the tra variable is blue then opens Blucare
		if tra=="blue":
			#Checks to see if first run
			if count == 0:
				#Opens a new browser
				webbrowser.get('firefox').open_new("https://bluecare.express/Tracking?trackingReference="+ str(larr[1]))
				count = 1
			else:
				#Opens a new tab
				webbrowser.get('firefox').open_new_tab("https://bluecare.express/Tracking?trackingReference="+ str(larr[1]))

		#If the tra variable is parc then opens Parcelsapp
		if tra=="parc":
			#Checks to see if first run
			if count == 0:
				#Opens a new browser
				webbrowser.get('firefox').open_new("http://parcelsapp.com/en/tracking/"+ str(larr[1]))
				count = 1
			else:
				#Opens a new tab
				webbrowser.get('firefox').open_new_tab("http://parcelsapp.com/en/tracking/"+ str(larr[1]))

	#The script sleeps for 1 second
	time.sleep(1)

	#Resets the variable to be empty
	tra=""
