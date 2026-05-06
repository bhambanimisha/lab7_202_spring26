import unittest

from lab7_1 import MinHeap, insert, extract, heapify_up, heapify_down


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        heap1:MinHeap = MinHeap([5, 10, 8, 20, 15, 9, 1])
        result = insert(heap1, 6)
        self.assertEqual(result, MinHeap([5, 6, 8, 10, 15, 9, 1, 20]))

    def test_insert_multiple(self):
        heap1:MinHeap = MinHeap([5, 10, 8, 20, 15, 9, 1])
        result = insert(heap1, 6)
        result = insert(result, 3)
        self.assertEqual(result, MinHeap([3, 5, 8, 6, 15, 9, 1, 20, 10]))

    def test_extract(self):
        heap1:MinHeap = MinHeap([1, 10, 5, 20, 15, 9, 8])
        result = extract(heap1)
        self.assertEqual(result, (1, MinHeap([5, 10, 8, 20, 15, 9])))

    def test_extract_twice(self):
        heap1:MinHeap = MinHeap([1, 10, 5, 20, 15, 9, 8])
        result = extract(heap1)
        result = extract(heap1)
        self.assertEqual(result, (1, MinHeap([5, 10, 8, 20, 15, 9])))

    def test_heapify_up(self):
        heap = [5, 10, 8, 20, 15, 9, 1]
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])


if __name__ == "__main__":
    unittest.main()
