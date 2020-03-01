import unittest
from datetime import date
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testArea(self):
        expected = 3.14
        self.assertEqual(expected, task.area(1))

        expected = 12.56
        self.assertEqual(expected, task.area(2))

    def testGetElements(self):
        list = [1, 2, 3, 4]
        expected = [1, 4]

        self.assertEqual(expected, task.get_elements(list))

    def testDate(self):
        date1 = date(2018, 12, 13)
        date2 = date(2019, 2, 25)

        expected = 74

        self.assertEqual(expected, task.get_date(date1, date2))


if __name__ == '__main__':
    unittest.main()
