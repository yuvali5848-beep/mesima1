class Animal:
    def speak(self):
        raise NotImplementedError("Must implement speak method")


class Dog(Animal):
    def speak(self):
        return "הכלב נובח"


class Cat(Animal):
    def speak(self):
        return "החתול מיילל"


def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())


if __name__ == "__main__":
    main()
