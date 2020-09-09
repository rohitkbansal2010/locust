import json
import itertools
import logging
import os
import sys

from datetime import datetime

from locust import HttpLocust, TaskSet, task
#sys.path.append('/home/amitjoc/work/locust/locustio/common')
#cwd = os.getcwd()
#pwd = os.path.abspath(os.path.join(cwd, os.pardir))
#sys.path.append(pwd + "/common")

#from common.logutil import app_file_logger
from common import logutil

iter_count = 0
min_number = 1000

logutil.append_file_logger()


class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        self.username = "rohitkbansal2010@gmail.com"
        self.password = "init1234"
        #dttime = datetime.now()
        #self.base = "%s%s%s" % (str(dttime.month + dttime.day),
        #                        str(dttime.hour + dttime.minute),
        #                        str(dttime.second))
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled
        self.login()

    def login(self):
        response = self.client.get("/login/")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post(
            "/login/",
            {
               "email": self.username,
               #"password": self.password
            },
            headers = {"XSRF-TOKEN": csrftoken}
        )

    #@task(2)
    #def account(self):
    #    response = self.client.get("/")

    #@task(1)
    #def profile(self):
    #    response = self.client.get("/users/2/")

    #@task(1)
    #def edit_profile(self):
    #    response = self.client.get("/users/2/edit/")
    #    csrftoken = response.cookies['csrftoken']
    #    response = self.client.post ("/users/2/edit/",
    #        {
    #           "first_name": "amit" + self.base,
    #           "last_name": "joc" + self.base,
    #        },
    #        headers={"X-CSRFToken": csrftoken}
    #    )

    #@task(1)
    #def add_product(self):
    #    response = self.client.get("/inventory/create/")
    #    csrftoken = response.cookies['csrftoken']
    #    response = self.client.post("/inventory/create/",
    #        {
    #            "name": self.base + str(iter_count + min_number) + "Test",
    #            "description": self.base + str(iter_count + min_number) +
    #               "is good product",
    #            "shipping_weight": self.base,
    #            "sku": self.base + str(iter_count + min_number),
    #            "marketplace_product_id": self.base + str(iter_count +
    #                min_number),
    #            "cost": self.base,
    #            "value": self.base,
    #            "quantity": self.base
    #        },
    #        headers={"X-CSRFToken": csrftoken}
    #    )

    #@task(1)
    #def edit_product(self):
    #    response = self.client.get("/inventory/1/edit/")
    #    csrftoken = response.cookies['csrftoken']
    #    response = self.client.post("/inventory/1/edit/",
    #        {
    #            "name": self.base + str(iter_count + min_number) + "EditTest",
    #            "description": "product" + self.base +
    #               str(iter_count + min_number) + "is good product",
    #            "shipping_weight": self.base,
    #            "sku": self.base + str(iter_count + min_number),
    #            "marketplace_product_id": self.base + str(iter_count +
    #                min_number),
    #            "cost": self.base,
    #            "value": self.base,
    #            "quantity": self.base
    #        },
    #        headers={"X-CSRFToken": csrftoken}
    #    )

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
