import unittest

class TestSample(unittest.TestCase):
    def setUp(self):
        self.target = 'foo'

    @unittest.skip("이 테스트를 건너뜁니다.")
    def test_upper(self):
        self.assertEqual(self.target.upper(), 'Foo')

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSample)
    unittest.TextTestRunner(verbosity=2).run(suite)
