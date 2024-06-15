import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "your_own_token_from pixela user account"
USERNAME = "your unique username"
user_parameter = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    
}

# user_creation = requests.post(url=pixela_endpoint,json=user_parameter)
# print(user_creation.text)
# print(user_creation.status_code)

coding_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN":TOKEN
}
# coding_graph_info = {
#     'id':"codinggraph",
#     'name':"CodingTracker",
#     'unit':'hour',
#     'type':'float',
#     'color':'kuro'
# }
# graph_creation = requests.post(url=coding_graph_endpoint,json=coding_graph_info,headers=headers)
# print(graph_creation.text)
# yyyymmdd



# updating a graph.
# updated_pixel_info = {
#     "quantity":"4"
# }
# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/codinggraph/20240615",json=updated_pixel_info,headers=headers)
# print(response.text)
# print(response.status_code)



# today = datetime(2024,6,11).strftime("%Y%m%d")

today = datetime.now().strftime("%Y%m%d")
coding_graph_post = f"{coding_graph_endpoint}/codinggraph"

coding_details = {
    "date":today,
    "quantity":input("How long did you code today? ")
}
response = requests.post(url=coding_graph_post,json=coding_details,headers=headers)
print(response.text)
