import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUE0sITV7qEi5j-kYwNM6E1DjfezdmlwICYKnkhhRtcNC4HEjUBPLcAPJxyIKulRW7TdSByRxUr6p4ZK"
        self.client_secret = "ENd5FP9ESUNVYyPyp15wyxyyrRMvkBr9F6g601DgzWb3Qg-iwW5_uhYfuHHaxDB1YdMalR_LGGQiIRw-"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)