class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


# Тестирование
a = SingletonClass(10)
b = SingletonClass(20)

print(a is b)  # True
print(a.value)  # 10
print(b.value)  # 10