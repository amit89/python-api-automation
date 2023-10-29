from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/users?page=2")
