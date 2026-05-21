def common_elements():

    by_3 = set([x for x in range(100) if x % 3 == 0])
    by_5 = set([z for z in range(100) if z % 5 == 0])

    result = by_5.intersection(by_3)

    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
