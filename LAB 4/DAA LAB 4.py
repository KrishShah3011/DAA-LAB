def integer_mul(a, b):
    """
    Multiply two integers using a manual approach by creating
    a dictionary of multiples for the larger integer and
    summing results for the digits of the smaller integer.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of multiplying a and b.
        str: "Invalid Datatype" if inputs are not integers.
    """
    if isinstance(a, int) and isinstance(b, int):
        x = min(a, b)
        y = max(a, b)
        ans_dict = {}

        for i in range(10):
            ans_dict[i] = y * i

        ans = 0
        count = 0

        for i in reversed(str(x)):
            zeros = "0" * count
            ans += int(str(ans_dict[int(i)]) + zeros)
            count += 1

        return ans
    else:
        return "Invalid Datatype"


def d_c_integer_mul(a, b):
    """
    Multiply two integers using a divide-and-conquer approach.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of multiplying a and b.
        str: "Invalid Datatype" if inputs are not integers.
    """
    if isinstance(a, int) and isinstance(b, int):
        if a < 10 or b < 10:
            return a * b

        n = max(len(str(a)), len(str(b))) // 2

        x1 = a // 10 ** n
        x0 = a % 10 ** n
        y1 = b // 10 ** n
        y0 = b % 10 ** n

        p = d_c_integer_mul(x1, y1)
        q = d_c_integer_mul(x0, y0)
        r = d_c_integer_mul(x1 + x0, y1 + y0) - p - q

        return p * 10 ** (2 * n) + r * 10 ** n + q
    else:
        return "Invalid Datatype"


def check_compatible(arr):
    """
    Check if the array is compatible with the global 'base' array.

    Compatibility means both arrays contain the same elements.

    Args:
        arr (list): Input array to check against the base array.

    Returns:
        bool: True if arrays are compatible, False otherwise.
    """
    global base
    temp = arr.copy()
    temp2 = base.copy()

    for i in base:
        if i in temp:
            temp.remove(i)
            temp2.remove(i)

    if temp or temp2:
        return False

    return True


def count_inversions(arr):
    """
    Count the number of inversions in an array using a merge sort approach.

    An inversion occurs if for any pair (i, j), where i < j, arr[i] > arr[j].

    Args:
        arr (list): The array for which to count inversions.

    Returns:
        int: The number of inversions in the array.
        str: "The array is not compatible!!" if the array is not compatible.
    """

    def merge_and_count(arr, temp_arr, left, right):
        """ Recursively count inversions by dividing and merging halves. """
        if left >= right:
            return 0

        mid = (left + right) // 2

        inversions = merge_and_count(arr, temp_arr, left, mid)
        inversions += merge_and_count(arr, temp_arr, mid + 1, right)
        inversions += merge_halves(arr, temp_arr, left, mid, right)

        return inversions

    def merge_halves(arr, temp_arr, left, mid, right):
        """
        Merge two halves of the array and count inversions.

        During merging, if an element from the right half is smaller
        than an element from the left half, it means an inversion.
        """
        i = left
        j = mid + 1
        k = left
        inversions = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inversions += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inversions

    if check_compatible(arr):
        return merge_and_count(arr, arr.copy(), 0, len(arr) - 1)
    else:
        return "The array is not compatible!"


# Test Cases
base = [1, 2, 3, 4, 5]
course_list = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [1, 2, 3, 5, 4], [1, 2, 3, 4, 5], [5, 3, 4, 1, 2], [1, 2, 3, 4],
               [6, 2, 1, 4], [1, 2, 3, 4, 5, 6], [7, 8, 9, 10], []]

for i in course_list:
    print("Number of inversions:", count_inversions(i))

print(integer_mul(4554210, 7891105))
print(integer_mul(724578, 975432))
print(integer_mul(9821204, 7045222))
print(integer_mul(966425, 993044))
print(integer_mul(70854699, 24753112))
print(integer_mul(5678.00, 60799.17))
print(integer_mul(333.333, 666.666))
print(integer_mul(7974.17, 93210.22))
print(integer_mul(12345.17, 54321.61))
print(integer_mul(786132.14, 215473.66))

print(d_c_integer_mul(4554210, 7891105))
print(d_c_integer_mul(724578, 975432))
print(d_c_integer_mul(9821204, 7045222))
print(d_c_integer_mul(966425, 993044))
print(d_c_integer_mul(70854699, 24753112))
print(d_c_integer_mul(5678.00, 60799.17))
print(d_c_integer_mul(333.333, 666.666))
print(d_c_integer_mul(7974.17, 93210.22))
print(d_c_integer_mul(12345.17, 54321.61))
print(d_c_integer_mul(786132.14, 215473.66))
