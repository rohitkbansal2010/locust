#from bs4 import BeautifulSoup

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        self.username = "divick.kishore@gmail.com"
        self.password = "init1234"

    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled
        self.login()

    # User Login
    def login(self):
        response = self.client.get("/login/")
        print(response.text)
        csrftoken = response.cookies['csrftoken']
        print("Csrf Token: " + csrftoken)
        response = self.client.post (
            "/login/",
            {
                "login": self.username,
                "password": self.password
            },
            headers = { "X-CSRFToken": csrftoken }
        )

    @task(2)
    def account(self):
        self.client.get("/")

    ## access the fullfillment form
    #@task(1)
    #def fullfillment_list(self):
    #    self.client.get (
    #        "/cratejoy/fulfillments/"
    #    )
    #    # send ajax request for fullfillment form to get fullfillment list
    #    response = self.client.get (
    #        '/cratejoy/fulfillments/list/',
    #        headers = {
    #            'X-Requested-With': 'XMLHttpRequest'
    #        }
    #    )

    #    #fullfillment edit form
    #    soup = BeautifulSoup(response.text, 'html.parser')
    #    link = soup.find_all('a')[11]['href']
    #    response =  self.client.get(link)
    #    #send ajax request for fullfillment edit form to get fullfillment list
    #    url = link.split('/')
    #    response = self.client.get (
    #        "/" + url[1] + "/" + url[2] + "/" + url[3] +
    #            "/get-inventory-products/",
    #        headers = {
    #            'X-Requested-With': 'XMLHttpRequest' 
    #        }
    #    )
    #    print(response.text);


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
