# importing the requests library
import requests

# api-endpoint
URL = "blob:https://view.vzaar.com/83d2f75f-ec49-4a2b-b03a-95b8d5cf6007"


# sending get request and saving the response as response object
r = requests.get(url = URL)