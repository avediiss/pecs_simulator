class Message:
    next_id = 1

    def __init__(self, source, destination, timestamp):
        self.message_id = Message.next_id
        Message.next_id += 1

        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    # Getters
    def get_id(self):
        return self.message_id

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_timestamp(self):
        return self.timestamp

    # Setters
    def set_source(self, source):
        self.source = source

    def set_destination(self, destination):
        self.destination = destination

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def print_message(self):
        print(
            f"Message {self.message_id} | "
            f"source={self.source} | "
            f"destination={self.destination} | "
            f"timestamp={self.timestamp}"
        )