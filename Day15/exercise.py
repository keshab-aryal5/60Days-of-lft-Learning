import requests
from datetime import datetime

TOKEN = "your_own_token_from pixela user account"
USERNAME = "your unique username"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_details ={
#     'id':"exercisegraph",
#     'name':"ExerciseTracker",
#     'unit':'hour',
#     'type':'float',
#     'color':'ajisai'
# }

# graph_response = requests.post(url=graph_endpoint,json=graph_details,headers=headers)
# print(graph_response.text)

today = datetime.now().strftime("%Y%m%d")
exercise_graph_post = f"{graph_endpoint}/exercisegraph"

exercise_details ={
    "date":today,
    "quantity":input("How long did you exericed today? ")
}
response = requests.post(url=exercise_graph_post,json=exercise_details,headers=headers)
print(response.text)