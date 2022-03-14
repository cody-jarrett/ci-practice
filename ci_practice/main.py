import toml

CONFIG = toml.load("config.toml")["app"]


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def app():
    name = f"This is {CONFIG['APP_NAME']}"
    print(name)
    return name


if __name__ == "__main__":
    app()
