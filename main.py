from message import Message
from event import Event
from scheduler import Scheduler
from client import Client
from queue import Queue
from server import Server
from gateway import Gateway


def test_message():
    print("=== TEST MESSAGE ===")

    msg1 = Message(1, 0, 0.5)
    msg2 = Message(2, 0, 1.0)
    msg3 = Message(2, 0, 1.5)
    msg4 = Message(4, 0, 2.0)

    msg1.print_message()
    msg2.print_message()
    msg3.print_message()
    msg4.print_message()

    print("Message 1 ID:", msg1.get_id())
    print("Message 1 source:", msg1.get_source())
    print("Message 1 destination:", msg1.get_destination())
    print("Message 1 timestamp:", msg1.get_timestamp())

    print()


def test_event():
    print("=== TEST EVENT ===")

    msg = Message(1, 0, 0.5)

    event1 = Event(msg, "SEND_MSG", 0.5)
    event2 = Event(msg, "RECV_MSG", 1.0)

    event1.print_event()
    event2.print_event()

    print("Event 1 Time:", event1.get_event_time())
    print("Event 1 Type:", event1.get_event_type())

    print("Event 2 Time:", event2.get_event_time())
    print("Event 2 Type:", event2.get_event_type())

    print()


def generate_trace(event, node):
    message = event.get_message()

    event_label = event.get_event_type()

    if event_label == "SEND_MSG":
        event_label = "SEND"
    elif event_label == "RECV_MSG":
        event_label = "RECV"
    elif event_label == "MSG_DEPT":
        event_label = "DEPT"

    print(
        f"{event.get_event_time():<8} "
        f"{node:<5} "
        f"{event_label:<6} "
        f"{message.get_source():<7} "
        f"{message.get_destination():<5} "
        f"{message.get_id():<5}"
    )


def test_scheduler():
    print("=== TEST SCHEDULER ===")

    scheduler = Scheduler()

    msg1 = Message(1, 0, 1.202)
    msg2 = Message(3, 0, 2.320)

    event1 = Event(msg1, "SEND_MSG", 1.202)
    event2 = Event(msg1, "RECV_MSG", 1.916)
    event3 = Event(msg2, "SEND_MSG", 2.320)
    event4 = Event(msg2, "RECV_MSG", 2.391)
    event5 = Event(msg1, "MSG_DEPT", 4.572)
    event6 = Event(msg2, "MSG_DEPT", 5.916)

    scheduler.add_event(event5)
    scheduler.add_event(event3)
    scheduler.add_event(event1)
    scheduler.add_event(event6)
    scheduler.add_event(event2)
    scheduler.add_event(event4)

    print("time     node  event  source  dest  msgID")

    while True:
        event = scheduler.get_event()

        if event is None:
            break

        if event.get_event_type() == "SEND_MSG":
            node = event.get_message().get_source()
        else:
            node = 0

        generate_trace(event, node)

    print("Current Time:", scheduler.get_current_time())
    print()

def test_client():
    print("=== TEST CLIENT ===")

    client = Client(0, 4)  # destination=0, lambda=4

    client.print_client()

    current_time = 0.0

    for _ in range(5):
        event = client.generate_event(current_time)
        current_time = event.get_event_time()
        event.print_event()

    print()

def test_queue():
    print("=== TEST QUEUE ===")

    q = Queue()

    msg1 = Message(1, 0, 0.5)
    msg2 = Message(2, 0, 1.0)
    msg3 = Message(3, 0, 1.5)

    q.enqueue(msg1)
    q.enqueue(msg2)
    q.enqueue(msg3)

    print("Queue size:", q.size())

    print("Front message:")
    front = q.peek()
    if front:
        front.print_message()

    removed = q.dequeue()

    print("Removed message:")
    if removed:
        removed.print_message()

    print("Queue size after dequeue:", q.size())

    print()
    
def print_server_state(server):
    if server.is_busy():
        print("Server state: BUSY")
    else:
        print("Server state: IDLE")
    
    
def test_server():
    print("=== TEST SERVER ===")

    server = Server()

    msg1 = Message(1, 0, 0.5)

    print_server_state(server)

    started = server.start_service(msg1)
    if started:
        print("Server started processing:")
        msg1.print_message()

    print_server_state(server)

    finished_msg = server.end_service()

    if finished_msg:
        print("Server finished processing:")
        finished_msg.print_message()

    print_server_state(server)

    print()
    
def test_gateway():
    print("=== TEST GATEWAY ===")

    gateway = Gateway()

    msg1 = Message(1, 0, 0.5)
    msg2 = Message(2, 0, 1.0)
    msg3 = Message(3, 0, 1.5)

    gateway.receive_message(msg1)
    gateway.receive_message(msg2)
    gateway.receive_message(msg3)

    gateway.complete_service()
    gateway.complete_service()
    gateway.complete_service()

    print()

    
def main():
    test_message()
    test_event()
    test_scheduler()
    test_client()
    test_queue()
    test_server()
    test_gateway()


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    

