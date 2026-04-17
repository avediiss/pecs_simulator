class Scheduler:
    def __init__(self):
        self.events = []
        self.current_time = 0.0

    def add_event(self, event):
        inserted = False

        for i in range(len(self.events)):
            if event.get_event_time() < self.events[i].get_event_time():
                self.events.insert(i, event)
                inserted = True
                break

        if not inserted:
            self.events.append(event)

    def get_event(self):
        if len(self.events) == 0:
            return None

        event = self.events.pop(0)
        self.current_time = event.get_event_time()
        return event

    def get_current_time(self):
        return self.current_time