import unittest
from scrape import scrape
from sql import obtainCollection, existReportForToday

class TestScrape(unittest.TestCase):
    def test_scrape(self):
        data = scrape()
        self.assertEqual(len(data), 100)
        data = []
        self.assertEqual(len(data), 0)

class TestSql(unittest.TestCase):
    def test_obtain(self):
        collection = obtainCollection('CryptoPunks')
        self.assertEqual(collection[1], 'CryptoPunks')
        collection = obtainCollection('CryptoPunk')
        self.assertEqual(collection, None)

    def test_exist(self):
        report = existReportForToday()
        self.assertEqual(type(report), type([]))
        report = existReportForToday()
        self.assertNotEqual(report, None)