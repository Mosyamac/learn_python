import unittest
from my_package.arithmetic import fibonacci_recursive, fibonacci_iterative
 
class TestFib(unittest.TestCase):
  
    def test_fib_iter(self):
        self.assertEqual([fibonacci_iterative(i) for i in xrange(1, 6)], [1, 1, 2, 3, 5])
        self.assertEqual(fibonacci_iterative(4), 3)
        self.assertEqual(fibonacci_iterative(5), 5)
    
    def test_fib_recursive(self):    
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
#  
 
if __name__ == '__main__':
    unittest.main()