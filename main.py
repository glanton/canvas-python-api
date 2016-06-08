# import external libraries
import requests
import json

# import local token file (ignored by git)
import token

print(token.uriTokenString)

# build URL
domain = "https://canvas.harvard.edu/api/v1/courses/"
course = "7832"
query = "/students"

url = domain + course + query + token.uriTokenString
