from pymeaux.leet import leet_list


def test_max_avg_cum():
    assert leet_list.max_avg_cum([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert leet_list.max_avg_cum([5], 1) == 5.0


def test_max_avg_slide():
    assert leet_list.max_avg_slide([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert leet_list.max_avg_slide([5], 1) == 5.0


def test_max_ones():
    assert leet_list.max_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert (
        leet_list.max_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
        == 10
    )


def test_min_start():
    assert leet_list.min_start([-3, 2, -3, 4, 2]) == 5
    assert leet_list.min_start([1, 2]) == 1
    assert leet_list.min_start([1, -2, -3]) == 5


def test_sums_cum():
    assert leet_list.sums_cum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert leet_list.sums_cum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert leet_list.sums_cum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


if __name__ == "__main__":
    from timeit import timeit

    funcs_compare = ["test_max_avg_cum", "test_max_avg_slide"]
    for func in funcs_compare:
        print("{:<30} {}".format(func, timeit(eval(func))))
