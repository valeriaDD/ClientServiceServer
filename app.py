import itertools
import json
import threading
import time
import random

import requests
from flask import Flask, request
import logging

from constants import FOOD_ORDERING_URL
from src.Menu import Menu

app = Flask(__name__)
logger = logging.getLogger(__name__)

clients = []
clientStateMutex = threading.Lock()


class Client(threading.Thread):
    id_iter = itertools.count()

    def __init__(self):
        super(Client, self).__init__()
        self.id = next(Client.id_iter) + 1
        self.no_order = True
        self.lock =threading.Lock()

    def run(self):
        while True:
            self.lock.acquire()
            if self.no_order:
                self.no_order = False
                self.lock.release()
                self.make_order()
            else:
                self.lock.release()
                time.sleep(3)

    def make_order(self):
        time.sleep(random.randint(0, 3))
        orderItems = []
        for _ in range(0, random.randint(1, 3)):
            orderItems.append(Menu().get_random_menu_item())

        order = {
            "client_id": self.id,
            "order_items": orderItems
        }
        app.logger.info(f"Client {self.id} has placed order")
        requests.post(f'{FOOD_ORDERING_URL}/order', json=json.dumps(order))

    def serve_order(self):
        with self.lock:
            self.no_order = True
            app.logger.info("Order senttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")


@app.route("/")
def miaw():
    return "Hello from clientService server"


@app.route("/serve/<client_id>", methods=["POST"])
def serve_order(client_id):
    app.logger.info(f"Order to client with id: {client_id}")

    data = request.json
    data = json.loads(data)

    app.logger.info(f"Order data: {data}")
    serve_to_client_with_id(client_id)

    return "Hello from clientService server"


def serve_to_client_with_id(client_id):
    for client in clients:
        if int(client.id) == int(client_id):
            app.logger.info(f"Found {client.id} and {client_id}")
            client.serve_order()


if __name__ == '__main__':
    clients_number = 5

    for _ in range(2):
        client_thread = Client()
        client_thread.start()
        clients.append(client_thread)

    app.run(debug=True, port=5002, host="0.0.0.0")
