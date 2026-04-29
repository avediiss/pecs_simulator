import random
from message import Message
from event import Event


class Client:
    next_id = 1

    def __init__(self, destination, lambda_value):
        self.client_id = Client.next_id
        Client.next_id += 1

        self.destination = destination
        self.lambda_value = lambda_value

    def generate_interarrival_time(self):
        return random.expovariate(self.lambda_value)

    def generate_message(self, timestamp):
        return Message(self.client_id, self.destination, timestamp)

    def generate_event(self, current_time):
        interarrival_time = self.generate_interarrival_time()
        event_time = current_time + interarrival_time

        msg = self.generate_message(event_time)
        return Event(msg, "SEND_MSG", event_time)

    def print_client(self):
        print(
            f"Client {self.client_id} -> Destination {self.destination} "
            f"| lambda={self.lambda_value}"
        )