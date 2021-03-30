from unittest import TestCase, main

from hero.project.hero import Hero
# from project.hero import Hero ---> for Judge


class HeroTest(TestCase):
    def setUp(self) -> None:
        username = 'Main hero'
        level = 5
        health = 100
        damage = 10
        self.hero = Hero(username, level, health, damage)

    def test_init_attributes__set_correctly(self):
        expected_name = 'Main hero'
        expected_level = 5
        expected_health = 100
        expected_damage = 10
        self.assertEqual(expected_name, self.hero.username)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle__when_hero_username_equal__expect_raise_exception(self):
        same_username_hero = Hero('Main hero', 6, 80, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(same_username_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__when_hero_health_below_or_equal_to_0__expect_raise_exception(self):
        enemy = Hero('Enemy', 1, 10, 10)
        self.hero.health = -self.hero.health
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__when_enemy_health_below_or_equal_to_0__expect_raise_exception(self):
        enemy = Hero('Enemy', 1, -1, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle__when_hero_wins(self):
        enemy = Hero('Enemy', 1, 20, 10)
        expected_hero_damage = self.hero.damage + 5
        expected_hero_health = (self.hero.health - (enemy.damage * enemy.level)) + 5
        expected_hero_level = self.hero.level + 1
        self.assertEqual("You win", self.hero.battle(enemy))
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_damage, self.hero.damage)

    def test_battle__when_hero_loses(self):
        enemy = Hero('Enemy', 6, 110, 20)
        expected_enemy_damage = enemy.damage + 5
        expected_enemy_health = (enemy.health - (self.hero.damage * self.hero.level)) + 5
        expected_enemy_level = enemy.level + 1
        self.assertEqual("You lose", self.hero.battle(enemy))
        self.assertEqual(expected_enemy_level, enemy.level)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_enemy_damage, enemy.damage)

    def test_battle__when_draw(self):
        enemy = Hero('Enemy', 5, 100, 20)
        self.hero.damage = 20
        self.assertEqual("Draw", self.hero.battle(enemy))

    def test_str_representation(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage: {self.hero.damage}\n", self.hero.__str__())

if __name__ == '__main__':
    main()