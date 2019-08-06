import unittest

from decorators import true_false, upper_in_title_out


class DecoratorTests(unittest.TestCase):
    def test_true(self):
        @true_false
        def true_function():
            return ['Successful']
        self.assertTrue(true_function())

    def test_false(self):
        @true_false
        def false_function():
            return 0
        self.assertFalse(false_function())

    def test_one_upper_arg(self):
        @upper_in_title_out
        def db2query(environment):
            self.assertEqual(environment, 'USERTEST', msg='Single Arg not uppercase')
            return 'ROSEMARIE GOLD'
        db2query('UserTest')

    def test_multiple_upper_arg(self):
        @upper_in_title_out
        def db2query(company, environment, user):
            self.assertEqual(company, '00004', msg='Arg Company not right')
            self.assertEqual(environment, 'USERTEST', msg='Arg Environment not uppercase')
            self.assertEqual(user, 'MICHELLE', msg='Arg User not uppercase')
            return 'ROSEMARIE GOLD'
        db2query('00004', 'UserTest', 'michelle')

    def test_one_upper_kwarg(self):
        @upper_in_title_out
        def db2query(environment=""):
            self.assertEqual(environment, 'USERTEST', msg='Single Kwarg not uppercase')
            return 'ROSEMARIE GOLD'
        db2query(environment='UserTest')

    def test_multiple_upper_kwarg(self):
        @upper_in_title_out
        def db2query(environment="", user=""):
            self.assertEqual(environment, 'USERTEST', msg='Kwarg environment not uppercase')
            self.assertEqual(user, 'MICHELLE', msg='Kwarg User not uppercase')
            return 'ROSEMARIE GOLD'
        db2query(environment='UserTest', user="michelle")

    def test_kwarg_arg(self):
        @upper_in_title_out
        def db2query(environment, user=""):
            self.assertEqual(environment, 'USERTEST', msg='Arg environment not uppercase')
            self.assertEqual(user, 'MICHELLE', msg='Kwarg user not uppercase')
            return 'ROSEMARIE GOLD'
        db2query('UserTest', user="michelle")

    def test_title_return(self):
        @upper_in_title_out
        def db2query():
            return 'ROSEMARIE GOLD'
        self.assertEqual(db2query(), 'Rosemarie Gold', msg='Not returning title case')


if __name__ == '__main__':
    unittest.main()
