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


def custom_num_list(value):
    return [x for x in range(value)]


def custom_func(value, power, const):
    return const * (value) ** power


def custom_non_lin_num_list(length, const, power):
    return [custom_func(x, const, power) for x in range(length)]


# print(custom_num_list(10))
print(custom_non_lin_num_list(10, 2, 3))
