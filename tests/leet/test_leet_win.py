from pymeaux.leet import leet_win


def test_win_avg_max_cum():
    assert leet_win.win_avg_max_cum([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert leet_win.win_avg_max_cum([5], 1) == 5.0


def test_win_avg_max_slide():
    assert leet_win.win_avg_max_slide([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert leet_win.win_avg_max_slide([5], 1) == 5.0


if __name__ == "__main__":
    from timeit import timeit

    to_compare = ["test_win_avg_max_cum", "test_win_avg_max_slide"]
    for f in to_compare:
        print("{:<30} {}".format(f, timeit(eval(f))))
