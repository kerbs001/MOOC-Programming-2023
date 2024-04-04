def longest_series_of_neighbours(lst):
    if not lst:
        return 0  # return 0 for an empty list

    consecutive = 1  # start with 1 as we're counting at least the current element
    max_consecutive = 1

    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1] or lst[i] - 1 == lst[i + 1]:  # check if the next number is one more than the current one
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 1  # reset consecutive count if the current pair isn't consecutive

    return max_consecutive

if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(my_list))