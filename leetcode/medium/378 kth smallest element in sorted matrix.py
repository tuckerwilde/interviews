class Solution(object):
    # exceeds time limit.
    def kthsmallest(self, matrix, k):
        from collections import Counter
        import heapq
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # First step, creating a min heap to store our information
        heap = []
        heapq.heapify(heap)
        # This is essentially a dictionary, just has better built in methods.
        counts = Counter()
        # Assembling our counter.
        for row in matrix:
            counts += Counter(row)
        # Iterating through the counter, collecting values and pushing into our min heap.
        for key, value in counts.items():
            # The heappush function just allows for easier ways to keep the heap managed as we go.
            heapq.heappush(heap, (key, value))
        # Work our way inwards to find the k that matches our value.
        while k > 0:
            temp = heapq.heappop(heap)
            k -= temp[1]
        # Since we are working on (key, value) tuples, just return the key from that tuple.
        return temp[0]

    def kthsmallest2(self, matrix, k):
        """
        This example is taken from https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms.

        This is in an essence Binary Search. So it just utilises the functionality of binary search to locate the int.

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        lo, hi = matrix[0][0], matrix[-1][-1]
        # Our lo and hi denote where the outer reaches of our binary search area are.
        while lo < hi:
            # While we haven't found what we are looking for.
            mid = (lo + hi) // 2
            # Where is the middle, IE the starting point.
            # This sum one liner is pretty cool, it's bisecting, finding where to place the middle value into each
            # row of the 2d matrix. So depending on the summation of that bisect, we can figure out whether to move lo
            # or hi.
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                # if k is greater than the sum, we need to move lo up.
                lo = mid + 1
            else:
                # other wise move hi down to the middle.
                hi = mid

        return lo
