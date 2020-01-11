import unittest
from PyHeap.Heap import Heap

test = [((3, 4), 2.8284271247461903), ((8, 9), 9.899494936611665),
        ((10, 2), 9.0), ((0.1, 2), 0.9), ((10, 5), 9.486832980505138)]


class TestPyHeap(unittest.TestCase):
    def test_HeapLen(self):
        heap = Heap()
        heap.buildHeap(test, key=lambda x: x[1])
        self.assertEqual(len(test) + 1, len(heap.heap))

    def test_HeapSort(self):
        heap = Heap(key=lambda x: x[1])
        heap.buildHeap(test)
        res = heap.HeapSort()
        res = list(map(lambda x: heap.applyKey(x), res))
        expected = [
            0.9, 2.8284271247461903, 9.0, 9.486832980505138, 9.899494936611665
        ]
        self.assertEqual(sorted(expected), res)

    def test_HeapDeleteVal(self):
        heap = Heap()
        heap.buildHeap(test, key=lambda x: x[1])
        heap.deleteVal(9.0)
        self.assertEqual(len(test), len(heap.heap))
        expected = [
            0.9, 2.8284271247461903, 9.486832980505138, 9.899494936611665
        ]
        res = heap.HeapSort()
        res = list(map(lambda x: heap.applyKey(x), res))
        self.assertEqual(sorted(expected), res)

    def test_DeleteMin(self):
        heap = Heap(arr=test, key=lambda x: x[1])
        res = heap.applyKey(heap.deleteMin())
        expected = 0.9
        self.assertEqual(expected, res)

    def test_MaxHeap(self):
        heap = Heap(isMin=False, arr=test, key=lambda x: x[1])
        expected = sorted(
            [
                0.9, 2.8284271247461903, 9.0, 9.486832980505138,
                9.899494936611665
            ],
            reverse=True)
        res = heap.HeapSort()
        res = list(map(lambda x: heap.applyKey(x), res))
        self.assertEqual(expected, res)

    def test_MaxHeapDeleteMax(self):
        heap = Heap(isMin=False, arr=test, key=lambda x: x[1])
        expected = 9.899494936611665
        res = heap.applyKey(heap.deleteMin())
        self.assertEqual(expected, res)

    def test_HeapCorrectAfterHeapSort(self):
        heap = Heap()
        heap.buildHeap(test, key=lambda x: x[1])
        init = heap.heap
        heap.HeapSort()
        after = heap.heap
        # tests if they contain the same elements
        # the heap may be in a different order as heapsort
        # fed it a sorted array to build from
        self.assertCountEqual(init, after)


if __name__ == "__main__":
    unittest.main()
