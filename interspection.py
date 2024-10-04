from inspect import getmodule

def introspection_info(obj):
    return {
        'type:': type(obj),
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj)
    }

class Test:
    def __init__(self):
        self.name = 'Alex'

obj = Test()

print(introspection_info(obj))