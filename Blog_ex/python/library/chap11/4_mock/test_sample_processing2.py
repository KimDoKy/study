from sample_processing import my_processing
from unittest.mock import patch
import unittest

class TestMyClass(unittest.TestCase):
    def test_my_processing(self):
        with patch('sample_processing.OutsideAPI') as APIMock:
            api = APIMock()
            api.do_something.return_value = 'mock 객체로 대체된 결과'

            assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무엇인가를 하고 있다.'

        assert my_processing() == '외부 API로 어떠한 처리를 실행한 결과를 사용하여 무엇인가를 하고 있다.'

if __name__ == "__main__":
    unittest.main()
