from random import choice

def greet():
    options: list[str] = ["Hello, World", "你好，世界"]
    return choice(options)