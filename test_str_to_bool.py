from to_bool import str_to_bool
from unittest import TestCase

class TestToBool(TestCase):
  
  def test_is_true(self):
    self.assert(str_to_bool("yes")) is True
