class PS:


    def __init__(self, client):
        self.client = client


    def get_parameter(self, name):
        return self.client.get_parameter(Name=name)
