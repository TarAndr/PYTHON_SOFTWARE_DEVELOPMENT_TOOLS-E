class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Создаем объекты, представляющие разные автомобили
car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2018)
car3 = Car("Ford", 2022)

# Выводим информацию о каждом автомобиле
print("Информация о первом автомобиле:")
print(f"Марка: {car1.brand}")
print(f"Год выпуска: {car1.year}")

print("\nИнформация о втором автомобиле:")
print(f"Марка: {car2.brand}")
print(f"Год выпуска: {car2.year}")

print("\nИнформация о третьем автомобиле:")
print(f"Марка: {car3.brand}")
print(f"Год выпуска: {car3.year}")
