import unittest
from bank_system import OnlineBank, User


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.online_bank = OnlineBank()
        self.user = User("Nizar", "admin")
        self.online_bank.register("Alberto", "123azerty")
        self.online_bank.log_in_user("Alberto", "123azerty")

    def test_valid_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.password, "admin")
        self.assertEqual(self.user.balance, 0)
 
        self.assertFalse(self.user.is_logged_in)
        
    def test_user_balance_is_less_than_100(self):
        self.assertLess(self.user.balance,100)
        

    def test_password_is_correct(self):
        self.assertEqual(self.online_bank.users[0].password, "123azerty")

    def test_successful_deposit(self):
        valid_result = self.online_bank.deposit("Alberto", 100)
        self.assertEqual(valid_result, 100)
        another_valid_result = self.online_bank.deposit("Alberto", 100)
        self.assertEqual(another_valid_result, 200)
        self.assertGreater(another_valid_result,50)

    def test_not_successful_deposit(self):
        invalid_result = self.online_bank.deposit("Alberto", -100)
        self.assertIsNone(invalid_result)

    def test_successful_withdrawal(self):
        self.online_bank.deposit("Alberto", 100)
        valid_result = self.online_bank.withdraw("Alberto", 50)
        self.assertEqual(valid_result, 50)

    def test_insufficient_balance(self):
        self.online_bank.deposit("Alberto", 100)
        invalid_result = self.online_bank.withdraw("Alberto", 150)
        self.assertIsNone(invalid_result)

    def test_user_in_DB(self):
        self.assertIn("Alberto", [user.username for user in self.online_bank.users])

    def test_user_is_not_in_the_DB(self):
        self.assertNotIn("Nizar", [user.username for user in self.online_bank.users])

    def test_is_user_logged_in(self):
        self.assertTrue(self.online_bank.is_user_logged_in("Alberto"))

    def test_user_instance(self):
        user = self.online_bank.users[0]
        self.assertIs(user, self.online_bank.users[0])

    def test_user_logged_out_user(self):
        self.online_bank.logout_user("Alberto")
        result = self.online_bank.is_user_logged_in("Alberto")
        self.assertFalse(result)

    def test_desposit_without_login_user(self):
        self.online_bank.logout_user("Alberto")
        result = self.online_bank.deposit("Alberto", 4000)
        self.assertIsNone(result)

    def test_withdraw_without_login_user(self):
        self.online_bank.logout_user("Alberto")
        result = self.online_bank.withdraw("Alberto", 4000)
        self.assertIsNone(result)

    def test_deposit_withan_invalid_user(self):
        result = self.online_bank.deposit("Darth Vader", 4000)
        self.assertIsNone(result)