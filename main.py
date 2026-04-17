from message import Message
from event import Event
from scheduler import Scheduler


def test_message():
    print("=== TEST MESSAGE ===")

    msg1 = Message(1, 0, 0.5)
    msg2 = Message(2, 0, 1.0)

    msg1.print_message()
    msg2.print_message()

    print("Message 1 ID:", msg1.get_id())
    print("Message 1 source:", msg1.get_source())
    print("Message 1 destination:", msg1.get_destination())
    print("Message 1 timestamp:", msg1.get_timestamp())

    print()


def test_event():
    print("=== TEST EVENT ===")

    msg = Message(1, 0, 0.5)
    event = Event(1, msg, "SEND_MSG", 0.5)

    event.print_event()

    print("Event Time:", event.get_event_time())
    print("Event Type:", event.get_event_type())

    print()


def generate_trace(event, node):
    message = event.message

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

    event1 = Event(1, msg1, "SEND_MSG", 1.202)
    event2 = Event(2, msg1, "RECV_MSG", 1.916)
    event3 = Event(3, msg2, "SEND_MSG", 2.320)
    event4 = Event(4, msg2, "RECV_MSG", 2.391)
    event5 = Event(5, msg1, "MSG_DEPT", 4.572)
    event6 = Event(6, msg2, "MSG_DEPT", 5.916)

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
            node = event.message.get_source()
        else:
            node = 0

        generate_trace(event, node)

    print("Current Time:", scheduler.get_current_time())
    print()


def main():
    test_message()
    test_event()
    test_scheduler()


if __name__ == "__main__":
    main()