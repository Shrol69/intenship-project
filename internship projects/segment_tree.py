class SegmentTree:
    def __init__(self, arr, operation='sum'):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.operation = operation

        # Initialize the segment tree with the given array
        self.build(arr)

    def build(self, arr):
        # Build the tree from the original array
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            if self.operation == 'sum':
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            elif self.operation == 'min':
                self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
            else:
                raise ValueError("Unsupported operation. Use 'sum' or 'min'.")

    def update(self, index, value):
        # Update the value at the given index
        pos = index + self.n
        self.tree[pos] = value

        # Recompute the tree upwards
        while pos > 1:
            pos //= 2
            if self.operation == 'sum':
                self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            elif self.operation == 'min':
                self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def range_query(self, left, right):
        # Query the range [left, right)
        left += self.n
        right += self.n

        res = 0 if self.operation == 'sum' else float('inf')

        while left < right:
            if left % 2:
                if self.operation == 'sum':
                    res += self.tree[left]
                elif self.operation == 'min':
                    res = min(res, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                if self.operation == 'sum':
                    res += self.tree[right]
                elif self.operation == 'min':
                    res = min(res, self.tree[right])
            left //= 2
            right //= 2

        return res

    def display(self):
        # Display the segment tree
        print("Segment Tree:", self.tree[self.n:self.n*2])

# Example usage
if __name__ == "__main__":
    array = [2, 5, 1, 4, 9, 3]

    # Sum Segment Tree
    print("Sum Segment Tree:")
    seg_tree_sum = SegmentTree(array, operation='sum')
    seg_tree_sum.display()
    print("Range Sum [1, 5):", seg_tree_sum.range_query(1, 5))
    seg_tree_sum.update(3, 7)
    seg_tree_sum.display()
    print("Range Sum [1, 5) after update:", seg_tree_sum.range_query(1, 5))

    # Min Segment Tree
    print("\nMin Segment Tree:")
    seg_tree_min = SegmentTree(array, operation='min')
    seg_tree_min.display()
    print("Range Min [1, 5):", seg_tree_min.range_query(1, 5))
    seg_tree_min.update(3, 7)
    seg_tree_min.display()
    print("Range Min [1, 5) after update:", seg_tree_min.range_query(1, 5))
