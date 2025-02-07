class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


a = SingletonClass(10)
b = SingletonClass(20)

print(a is b)  # True
print(a.value)  # 20 (значение перезаписано при втором вызове)
print(b.value)  # 20
