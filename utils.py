from random import choice

def greet():
    options: list[str] = ["Hello, World", "你好，世界"]
    return choice(options)

def temperature_getter():
    options: list[int] = [36, 37, 39]
    return choice(options)

def switch_getter():
    options: list[str] = ["On", "Off"]
    return choice(options)