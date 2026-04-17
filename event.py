class Event:
    def __init__(self, event_id, message, event_type, event_time):
        self.event_id = Event.next_id
        Event.next_id += 1
        
        self.message = message
        self.event_type = event_type
        self.event_time = event_time

    # Getters
    def get_event_id(self):
        return self.event_id

    def get_event_time(self):
        return self.event_time

    def get_event_type(self):
        return self.event_type

    def get_message(self):
        return self.message

    # Setters
    def set_event_time(self, event_time):
        self.event_time = event_time

    def set_event_type(self, event_type):
        self.event_type = event_type

    # Print
    def print_event(self):
        print(
            f"Event {self.event_id} | "
            f"time={self.event_time} | "
            f"type={self.event_type} | "
            f"msgID={self.message.get_id()}"
        )