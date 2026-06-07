from locust import HttpUser, task, between

class AquaCoreUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_feedbacks(self):
        self.client.get("/feedbacks")

    @task
    def login(self):
        self.client.post("/login", data={
            "username": "test@test.com",
            "password": "wrongpassword"
        })
