"""Functions are written after tests failed, so they pass"""


def add(a, b):
    return a + b


def display_message():
    return "Message works!"


def show_message(msg):
    return msg


def check_length(value):
    return len(value)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
