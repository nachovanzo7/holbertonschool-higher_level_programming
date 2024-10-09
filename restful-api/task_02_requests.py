#!/usr/bin/python3
"""
Modulo para utilizar python
"""
import requests
"""
Modulo para utilizar la libreria requests
"""

import csv
"""
Modulo para utilizar serializacion csv
"""


def fetch_and_print_posts():
    info = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(info.status_code))

    if info.status_code == 200:
        data = info.json()

        for posts in data:
            print(posts['title']) #Obtener solo los titulos

def fetch_and_save_posts():
    info = requests.get("https://jsonplaceholder.typicode.com/posts")
    if info.status_code == 200:
        posts = []
        for post in info.json():
            estructura = {
                'id' : post['id'],
                'title' : post['title'],
                'body' : post['body']
            }
            posts.append(estructura)

    with open("posts.csv", "w") as archivo:
        titulos = ['id', 'title', 'body']
        writer = csv.DictWriter(archivo, fieldnames=titulos)
        writer.writeheader()

        for post in posts:
            writer.writerow(post)
