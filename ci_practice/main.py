import toml

CONFIG = toml.load("config.toml")["app"]


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def app():
    print(f"This is {CONFIG['APP_NAME']}. Let's build some cool python apps!")
