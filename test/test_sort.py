import unittest
from sorting.quick_sort import quick_sort
# from sorting.insertion_sort import insertion_sort
 
class TestSort(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_quick_sort(self):
        self.assertEqual(quick_sort([3,2,1,9,54]), [1,2,3,9,54])
        self.assertEqual(quick_sort([1,2,1]), [1,1,2])
        
#     def test_insertion_sort(self):
#         self.assertEqual(insertion_sort([3,2,1]), [1,2,3])
#         self.assertEqual(insertion_sort([1,2,1]), [1,1,2])
 
 
if __name__ == '__main__':
    unittest.main()