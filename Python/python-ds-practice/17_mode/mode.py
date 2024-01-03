def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counts_per_letter = {}

    for num in nums: 
        counts_per_letter[num] = counts_per_letter.get(num, 0) + 1

    max_count_num = max(counts_per_letter.values())

    for (num, freq) in counts_per_letter.items():
        if freq == max_count_num: 
            return num