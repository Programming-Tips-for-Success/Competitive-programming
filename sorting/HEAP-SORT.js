// We can sort an array in O(n log n) time and O(1) space by making it a heap!

// Make the array a max heap (use maxHeapify)
// Loop over the array, swap the root node with last item in the array
// After swapping each item, run maxHeapify again to find the next root node
// Next loop you'll swap the root node with the second-to-last item in the array and run maxHeapify again.
// Once you've run out of items to swap, you have a sorted array! 

// Heap h = new Heap();
// for (int i = 0; i < data.Length; i++)
//   h.Add(data[i]);
// int[] result = new int[data.Length];
// for (int i = 0; i < data.Length; i++)
//   data[i] = h.RemoveLowest();

// node sorting/HEAP-SORT.js
