# load external libraries
import requests
import csv

# load canvas API token
import canvasToken

# initialize list to store user data
userData = []

# store IDs and email addresses in userData from the csv file
with open("test.csv", "r") as f:
	reader = csv.reader(f)
	for row in reader:
		userData.append(row)

for user in userData:
	userID = user[0]
	newEmailData = {'user[email]' : user[1]}

	# build URL
	domain = "https://canvas.harvard.edu/api/v1/users/"
	url = domain + userID

	requests.put(url, data=newEmailData, headers=canvasToken.token)