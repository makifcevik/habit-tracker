import requests
from datetime import datetime

# find out how to create on: https://docs.pixe.la/entry/post-user
TOKEN = "TOKEN HERE"
USERNAME = "USERNAME HERE"
# f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1.html"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f" {pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}


def register_user_token():
    response = requests.post(url=pixela_endpoint, json=parameters)
    response.raise_for_status()
    print(response.text)


def post_graph():
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    response.raise_for_status()
    print(response.text)


def post_pixel(date: str, quantity: str):
    pixel_config = {
        "date": date,  # yyyyMMdd
        "quantity": quantity,
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    response.raise_for_status()
    print(response.text)


def update_pixel(date: str, quantity: str):
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
    pixel_config = {
        "quantity": quantity,
    }
    respond = requests.put(url=update_pixel_endpoint, json=pixel_config, headers=headers)
    respond.raise_for_status()
    print(respond.text)


def delete_pixel(date: str):
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
    respond = requests.delete(url=delete_pixel_endpoint, headers=headers)
    respond.raise_for_status()
    print(respond.text)


# register_user_token()
# post_graph()

today = datetime.now().strftime("%Y%m%d")  # will return today's date in yyyyMMdd format
# --- post a pixel
# post_pixel("20231104", "70")  # example
# post_pixel(today, "write_quantity_here") # example for today

# --- update an existing pixel
# update_pixel(today, "80")
# --- delete an existing pixel
# delete_pixel(today)
