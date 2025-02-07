from singleton_module import singleton_instance

# Тестирование
a = singleton_instance
b = singleton_instance

print(a is b)  # True
print(a.value)  # 10
print(b.value)  # 10