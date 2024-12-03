class dump(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value):
                original_method = value

                def make_wrapper(method_name, method):
                    def wrapped_method(self, *args, **kwargs):
                        print(f"{method_name}: {args}, {kwargs}")
                        return method(self, *args, **kwargs)

                    return wrapped_method

                dct[key] = make_wrapper(key, original_method)

        return super().__new__(cls, name, bases, dct)


import sys


exec(sys.stdin.read())
