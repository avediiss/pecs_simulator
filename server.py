class Server:
    def __init__(self):
        self.busy = False
        self.current_message = None

    def is_busy(self):
        return self.busy

    def start_service(self, message):
        if self.busy:
            return False

        self.current_message = message
        self.busy = True
        return True

    def end_service(self):
        if not self.busy:
            return None

        message = self.current_message

        self.current_message = None
        self.busy = False

        return message