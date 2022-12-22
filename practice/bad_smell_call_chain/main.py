# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, population: int, room: int):
        self.__population = population
        self.__room = room

    def get_person_room(self):
        return self.__room

    def get_city_population(self):
        return self.__population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
if __name__ == '__main__':
    person = Person(100500, 42)
    print(f"Person - room {person.get_person_room()}, population {person.get_city_population()}")
