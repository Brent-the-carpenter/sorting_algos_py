import unittest
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from list import list_of_nums 

class TestSortingAlgos(unittest.TestCase):
    sorted_list = sorted(list_of_nums.copy())     
    def test_bubble_sort(self):
        copy_list = list_of_nums.copy()
        bubble_sort(list_of_nums)
        self.assertEqual(self.sorted_list , bubble_sort(copy_list))  

    def test_merge_sort(self):
        copy_list = list_of_nums.copy()
        merge_sort(list_of_nums)
        self.assertEqual(self.sorted_list , merge_sort(copy_list))
          
    def test_insertion_sort(self):
                         
        copy_list = list_of_nums.copy()
        self.assertEqual(self.sorted_list , insertion_sort(copy_list))

    def test_quick_sort(self):
        copy_list = list_of_nums.copy()
        self.assertEqual(self.sorted_list , quick_sort(copy_list , 0 ,len(copy_list)-1 ))

    def test_selection_sort(self):
        copy_list = list_of_nums.copy()
                          
        self.assertEqual(self.sorted_list , selection_sort(copy_list))
