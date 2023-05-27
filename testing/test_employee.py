from unittest import TestCase
from unittest.mock import patch
from employee import Employee

class TestEmployee(TestCase):

    def setUp(self) -> None:
        self.emp_1 = Employee("Sudar", "Kasir", 50000)
        self.emp_2 = Employee("Dav", "Batt", 60000)
        print("setup")


    def tearDown(self) -> None:
        print("teardown\n")

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Sudar.Kasir@email.com')
        self.assertEqual(self.emp_2.email, 'Dav.Batt@email.com')

        self.emp_1.first = 'darsa'
        self.emp_2.first = 'dave'
        self.assertEqual(self.emp_1.email, 'darsa.Kasir@email.com')
        self.assertEqual(self.emp_2.email, 'dave.Batt@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Sudar Kasir')
        self.assertEqual(self.emp_2.fullname, 'Dav Batt')

        self.emp_1.first = 'darsa'
        self.emp_2.first = 'dave'

        self.assertEqual(self.emp_1.fullname, 'darsa Kasir')
        self.assertEqual(self.emp_2.fullname, 'dave Batt')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            sched = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Kasir/May')
            self.assertEqual(sched, 'Success')

            mocked_get.return_value.ok = False
            sched = self.emp_2.monthly_schedule('Jun')
            mocked_get.assert_called_with('http://company.com/Batt/Jun')
            self.assertEqual(sched, 'Bad Response!')

