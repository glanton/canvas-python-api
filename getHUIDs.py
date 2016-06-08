# import external libraries
import requests
import json
import csv

# import local token file (ignored by git)
import canvasToken

# initialize empty array to store user id's and sis_login_id's
userData = []

# build URL
domain = "https://canvas.harvard.edu/api/v1/courses/"
course = input("Course ID: ")
query = "/students"

url = domain + course + query + canvasToken.uriTokenString

# request URL and build users array
r = requests.get(url)
users = json.loads(r.text)
print(users)

for user in users:
	userID = user["id"]

	# check for sis_login_id and skip if absent
	if "sis_login_id" in user:
		userHUID = user["sis_login_id"]
		userData.append([userID, userHUID])
	else:
		continue
	
with open("user_ids.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(userData)
