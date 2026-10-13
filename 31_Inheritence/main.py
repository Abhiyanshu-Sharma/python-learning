from animal import Animal
from dog import Dog
from cat import Cat
from mouse import Mouse

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
cat.eat()
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()