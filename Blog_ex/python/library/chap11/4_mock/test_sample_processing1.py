from sample_processing import my_processing
from unittest.mock import patch
import unittest

class TestMyClass(unittest.TestCase):
    @patch('sample_processing.OutsideAPI')
    def test_my_processing(self, APIMock):
        api = APIMock()
        api.do_something.return_value = 'mock 객체로 대체된 결과'
        assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무언가를 하고 있다.'

if __name__ == "__main__":
    unittest.main()
