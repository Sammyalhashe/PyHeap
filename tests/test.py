import unittest
from PyHeap.Heap import Heap

test = [((3, 4), 2.8284271247461903), ((8, 9), 9.899494936611665),
        ((10, 2), 9.0), ((0.1, 2), 0.9), ((10, 5), 9.486832980505138)]


class TestPyHeap(unittest.TestCase):
    def test_HeapLen(self):
        """test_HeapLen
        Makes sure the generated heap has the correct number of elements
        """
        heap = Heap()
        heap.buildHeap(test, key=lambda x: x[1])
        self.assertEqual(len(test) + 1, len(heap.heap))

    def test_HeapSort(self):
        """test_HeapSort
        Test the sort implementation
        """
        heap = Heap(key=lambda x: x[1])
        heap.buildHeap(test)
        res = heap.HeapSort()
        res = list(map(lambda x: heap.applyKey(x), res))
        expected = [
            0.9, 2.8284271247461903, 9.0, 9.486832980505138, 9.899494936611665
        ]
        self.assertEqual(sorted(expected), res)

    def test_HeapDeleteVal(self):
        """test_HeapDeleteVal
        Makes sure the deleting an arbitrary value works
        """
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
        """test_DeleteMin
        Makes sure the correct min is deleted
        """
        heap = Heap(arr=test, key=lambda x: x[1])
        res = heap.applyKey(heap.deleteMin())
        expected = 0.9
        self.assertEqual(expected, res)

    def test_MaxHeap(self):
        """test_MaxHeap
        Instead of a minHeap, test maxHeap implementation
        """
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
        """test_MaxHeapDeleteMax
        Makes sure the correct max key is deleted
        """
        heap = Heap(isMin=False, arr=test, key=lambda x: x[1])
        expected = 9.899494936611665
        res = heap.applyKey(heap.deleteMin())
        self.assertEqual(expected, res)

    def test_HeapCorrectAfterHeapSort(self):
        """test_HeapCorrectAfterHeapSort
        Makes sure the underlying heap is still present after heapsort
        """
        heap = Heap()
        heap.buildHeap(test, key=lambda x: x[1])
        init = heap.heap
        heap.HeapSort()
        after = heap.heap
        # tests if they contain the same elements
        # the heap may be in a different order as heapsort
        # fed it a sorted array to build from
        self.assertCountEqual(init, after)

    def test_HeapIter(self):
        """test_HeapIter
        Testing the iteration of the heap
        """
        heap = Heap()
        a = [1, 2, 3, 4, 5, 6]
        heap.buildHeap(a)
        i = 0
        for val in heap:
            self.assertEqual(a[i], val)
            i += 1

    def test_HeapSwapOrientation(self):
        """test_HeapSwapOrientation
        Test the swap orientation; in this case makes sure it returns
        the correct maxHeap
        """
        a = [i for i in range(6)]
        n = len(a)
        heap = Heap(a)
        j = 0
        for val in heap:
            self.assertEqual(a[j], val)
            j += 1
        swapped = heap.swapOrientation()
        j = 0
        for val in swapped:
            self.assertEqual(a[n - 1 - j], val)
            j += 1

    def test_changeKey(self):
        """test_changeKey
        Makes sure the heap maintains integrity after changing key
        """
        a = [i for i in range(1, 6)]
        n = len(a)
        heap = Heap(a)
        j = 0
        for val in heap:
            self.assertEqual(a[j], val)
            j += 1
        heap.reconstructHeap(lambda x: 1 / x)
        j = 0
        for val in heap:
            self.assertEqual(a[n - 1 - j], val)
            j += 1
        # back to identity
        heap.reconstructHeap(None)
        j = 0
        for val in heap:
            self.assertEqual(a[j], val)
            j += 1

    def test_SwapError(self):
        a = Heap([i for i in range(5)])
        self.assertRaises(IndexError, a.swap, 1, -1)
        self.assertRaises(IndexError, a.swap, 1, len(a) + 1)

    def test_HeapIndexItem(self):
        """test_HeapIndexItem
        Makes sure it grabs the correct element by index
        """
        a = Heap([i for i in range(6)])
        expected = 2
        self.assertEqual(expected, a[2])
        expected = 3
        self.assertEqual(expected, a[3])


if __name__ == "__main__":
    unittest.main()
