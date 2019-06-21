import unittest


class FormatTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_format_cdata(self):
        pass

    def test_format_description(self):
        pass

    def test_format_title(self):
        pass

    def test_format_tweet(self):
        pass


def suite():
    suite = unittest.TestSuit()
    suite.addTest(FormatTestCase("test formatting functions"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
