from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        self.username = "demouser+ba@spendlabs.com"
        self.password = "Test@123"

    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled
        self.login(),
        #self.pwd()

    # User Login
    def login(self):
        response = self.client.get("/api/v1/isLoggedIn")
        csrftoken = response.cookies['XSRF-TOKEN']
        print("csrftoken ==> " + csrftoken)

        response1 = self.client.get("/api/v1/c2id/initSpendfitClient")
        print("res==> " + str(response1))

        headers = {
            'Content-type': 'application/json',
            'X-XSRF-TOKEN': csrftoken}
        data = {'email': self.username}
        response = self.client.post(
            "/api/v1/auth/initiate",
            data = json.dumps(data),
            headers = headers
        )
        print("username ==> " + str(response1))
        #self.pwd()

        #data1 = {'passowrd': self.password}
        #headers = {
        #    'Content-type': 'application/json',
        #    'X-XSRF-TOKEN': csrftoken }

    #def pwd(self):
    #    response = self.client.get('/api/v1/isLoggedIn')
    #    csrftoken = response.cookies['XSRF-TOKEN']
    #    headers = {
    #        'Content-type': 'application/json',
    #        'X-XSRF-TOKEN': csrftoken}
    #    data = {'passowrd': self.password}
    #    response = self.client.post(
    #        "/api/v1/auth/nextStep",
    #        data = json.dumps(data1),
    #        headers = headers
    #    )

    @task(2)
    def account(self):
        self.client.get("/")



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
