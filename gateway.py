from queue import Queue
from server import Server


class Gateway:
    def __init__(self):
        self.queue = Queue()
        self.server = Server()

    def print_server_state(self):
        if self.server.is_busy():
            print("Server state: BUSY")
        else:
            print("Server state: IDLE")

    def receive_message(self, message):
        print("Gateway received message:")
        message.print_message()

        self.print_server_state()

        if not self.server.is_busy():
            self.server.start_service(message)
            print("Message sent directly to server")
        else:
            self.queue.enqueue(message)
            print("Server busy → message added to queue")

        print("Queue size:", self.queue.size())
        print()

    def complete_service(self):
        finished_msg = self.server.end_service()

        if finished_msg:
            print("Service completed for:")
            finished_msg.print_message()

        if not self.queue.is_empty():
            next_msg = self.queue.dequeue()
            print("Next message taken from queue:")
            next_msg.print_message()

            self.server.start_service(next_msg)
            print("Server starts next message")
        else:
            print("Queue empty → server becomes idle")

        self.print_server_state()
        print("Queue size:", self.queue.size())
        print()

        return finished_msg