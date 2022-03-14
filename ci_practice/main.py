import toml

CONFIG = toml.load("config.toml")["app"]


def app():
    print(f"This is {CONFIG['APP_NAME']}. Let's build some cool python apps!")
