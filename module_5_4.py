class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.number_of_floors = numbers_of_floors

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        """ True, если количество этажей одинаковое у self и у other """
        return self.number_of_floors == other

    def __lt__(self, other):
        """ True, если количество этажей меньше, чем other """
        return self.number_of_floors < other

    def __le__(self, other):
        """ True, если количество этажей меньше или равно, чем other """
        return self.number_of_floors <= other

    def __gt__(self, other):
        """ True, если количество этажей больше, чем other """
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        """ True, если количество этажей не равно other """
        return self.number_of_floors != other

    def __str__(self):
        """ Возвращает название и количество этажей """
        return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'

    def __add__(self, value):
        # print(isinstance(value, House))
        if isinstance(value, int):
            self.number_of_floors =  self.number_of_floors + value
            return House(self.name, self.number_of_floors)
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return House(self.name, self.number_of_floors)

    def __radd__(self, value):
        return self + value

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __del__(self):
        print(f'{self} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)