# класс при помощи функции type()

C = type(
    "C",
    (),
    {
        "a": 100500,
        "fun": lambda self: self.a,
        "__init__": lambda self, x: setattr(self, "a", x),
    },
)
