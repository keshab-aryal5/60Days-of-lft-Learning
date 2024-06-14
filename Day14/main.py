import requests
from datetime import datetime
TOKEN = "<Your own token for pixela"
USERNAME = "<Your unique name of pixela>"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "My coding graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

posting_value = f"{graph_endpoint}/graph1"

today = datetime.now()
values = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}
# print(today.year)
# response = requests.post(url=posting_value,json=values,headers=headers)
# print(response.text)

# update_endpoint = f"{posting_value}/20240613"
# updated_value={
#     "quantity":"2"
# }
# response = requests.put(url=update_endpoint,json=updated_value,headers=headers)
# print(response.text)


delete_endpoint = f"{posting_value}/20250614"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)


# linke to pixela ----> "https://pixe.la/v1/users"