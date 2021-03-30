from unittest import TestCase, main

# from mammal.project.mammal import Mammal
from project.mammal import Mammal


class MammalTest(TestCase):
    name = 'Kitty'
    mammal_type = 'cat'
    sound = 'meow'
    kingdom = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_attrs_set_correctly(self):
        self.assertEqual('Kitty', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual(self.kingdom, self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()
