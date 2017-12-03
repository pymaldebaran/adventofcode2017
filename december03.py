#!/usr/bin/env python
"""--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this::

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data
must be carried back to square 1 (the location of the only access port for this
memory system) by programs that can only move up, down, left, or right. They
always take the shortest path: the
`Manhattan Distance<https://en.wikipedia.org/wiki/Taxicab_geometry>`_ between
the location of the data and square 1.

For example:

*   Data from square 1 is carried 0 steps, since it's at the access port.
*   Data from square 12 is carried 3 steps, such as: down, left, left.
*   Data from square 23 is carried only 2 steps: up twice.
*   Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?
"""

from itertools import count

import pytest


def nth_odd(n):
    """
    >>> nth_odd(0)
    1
    >>> nth_odd(1)
    3
    >>> nth_odd(2)
    5
    """
    return 2 * n + 1


def last_number_in_nth_square(n):
    """Return the last number present in a square of the loop.

    First square is the 0th one.

    >>> last_number_in_nth_square(0)
    1
    >>> last_number_in_nth_square(1)
    9
    >>> last_number_in_nth_square(2)
    25
    """
    a = nth_odd(n)
    return a * a


def first_number_in_nth_square(n):
    """Return the first number present in a square of the loop.

    First square is the 0th one.

    >>> first_number_in_nth_square(0)
    1
    >>> first_number_in_nth_square(1)
    2
    >>> first_number_in_nth_square(2)
    10
    >>> first_number_in_nth_square(3)
    26
    """
    if n == 0:
        return 1

    return last_number_in_nth_square(n - 1) + 1


def min_steps_to_nth_square(n):
    """Return the minimum number of steps to reach nth square from center.

    First square is the 0th one.

    >>> min_steps_to_nth_square(1)
    1
    >>> min_steps_to_nth_square(2)
    2
    >>> min_steps_to_nth_square(3)
    3
    >>> min_steps_to_nth_square(4)
    4
    """
    return n


def steps_in_nth_square_side(n):
    """Return the length in steps of the nth square side.

    First square is the 0th one.

    >>> steps_in_nth_square_side(0)
    1
    >>> steps_in_nth_square_side(1)
    3
    >>> steps_in_nth_square_side(2)
    5
    >>> steps_in_nth_square_side(3)
    7
    """
    return nth_odd(n)


def is_in_nth_square(target, n):
    """Does target belong to nth square.

    First square is the 0th one.

    >>> is_in_nth_square(1, 0)
    True
    >>> is_in_nth_square(1, 1)
    False
    >>> is_in_nth_square(2, 1)
    True
    >>> is_in_nth_square(5, 1)
    True
    >>> is_in_nth_square(5, 0)
    False
    >>> is_in_nth_square(23, 2)
    True
    >>> is_in_nth_square(27, 3)
    True
    """
    first = first_number_in_nth_square(n)
    last = last_number_in_nth_square(n)
    return first <= target <= last


def which_square(target):
    """In which square is the target number?

    First square is the 0th one.

    >>> which_square(1)
    0
    >>> which_square(2)
    1
    >>> which_square(5)
    1
    >>> which_square(6)
    1
    >>> which_square(23)
    2
    >>> which_square(27)
    3
    """
    for i in count(0):
        if is_in_nth_square(target, i):
            return i


class SquareSpec(object):
    """All the usefull number about the nth square.

    First square is the 0th one.
    """
    def __init__(self, n):
        if n == 0:
            self.first = 1
            self.last = 1
            self.steps_to_equivalent = 1
            self.top_right = 1
            self.top_left = 1
            self.bottom_left = 1
            self.bottom_right = 1
            self.middle_top = 1
            self.middle_bottom = 1
            self.middle_right = 1
            self.middle_left = 1
        else:
            self.first = first_number_in_nth_square(n)
            self.last = last_number_in_nth_square(n)
            self.steps_to_equivalent = steps_in_nth_square_side(n) - 1
            self.top_right = self.first + self.steps_to_equivalent - 1
            self.top_left = self.first + 2 * self.steps_to_equivalent - 1
            self.bottom_left = self.first + 3 * self.steps_to_equivalent - 1
            self.bottom_right = self.first + 4 * self.steps_to_equivalent - 1
            self.middle_top = self.top_right + self.steps_to_equivalent // 2
            self.middle_bottom = self.bottom_left + self.steps_to_equivalent // 2
            self.middle_right = self.top_right - self.steps_to_equivalent // 2
            self.middle_left = self.top_left + self.steps_to_equivalent // 2


@pytest.mark.parametrize("rank,expected", [
    (0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [2, 9, 2, 3, 5, 7, 9, 4, 8, 2, 6]),
    (2, [10, 25, 4, 13, 17, 21, 25, 15, 23, 11, 19]),
    ])
def test_quare_spec(rank, expected):
    sqr = SquareSpec(rank)
    assert sqr.first == expected[0]
    assert sqr.last == expected[1]
    assert sqr.steps_to_equivalent == expected[2]
    assert sqr.top_right == expected[3]
    assert sqr.top_left == expected[4]
    assert sqr.bottom_left == expected[5]
    assert sqr.bottom_right == expected[6]
    assert sqr.middle_top == expected[7]
    assert sqr.middle_bottom == expected[8]
    assert sqr.middle_right == expected[9]
    assert sqr.middle_left == expected[10]


def vertical_distance_to_center(target):
    """Vertical distance to the center of the square.

    >>> vertical_distance_to_center(1)
    0
    >>> vertical_distance_to_center(2)
    0
    >>> vertical_distance_to_center(3)
    1
    >>> vertical_distance_to_center(9)
    1
    >>> vertical_distance_to_center(11)
    0
    >>> vertical_distance_to_center(15)
    2
    >>> vertical_distance_to_center(16)
    2
    >>> vertical_distance_to_center(23)
    2
    >>> vertical_distance_to_center(26)
    2
    """
    if target == 1:
        return 0

    square_rank = which_square(target)
    square = SquareSpec(square_rank)

    if square.top_right <= target <= square.top_left \
            or square.bottom_left <= target <= square.bottom_right:
        return min_steps_to_nth_square(square_rank)
    elif square.first <= target < square.top_right:
        return abs(target - square.middle_right)
    else:
        return abs(target - square.middle_left)


def horizontal_distance_to_center(target):
    """Horizontal distance to the center of the square.

    >>> horizontal_distance_to_center(1)
    0
    >>> horizontal_distance_to_center(2)
    1
    >>> horizontal_distance_to_center(3)
    1
    >>> horizontal_distance_to_center(9)
    1
    >>> horizontal_distance_to_center(11)
    2
    >>> horizontal_distance_to_center(15)
    0
    >>> horizontal_distance_to_center(16)
    1
    >>> horizontal_distance_to_center(23)
    0
    >>> horizontal_distance_to_center(26)
    3
    """
    if target == 1:
        return 0

    square_rank = which_square(target)
    square = SquareSpec(square_rank)

    if square.top_right <= target <= square.top_left:
        return abs(target - square.middle_top)
    elif square.bottom_left <= target <= square.bottom_right:
        return abs(target - square.middle_bottom)
    else:
        return min_steps_to_nth_square(square_rank)


def steps_to_carry_data(target):
    h = horizontal_distance_to_center(target)
    v = vertical_distance_to_center(target)
    return h + v


@pytest.mark.parametrize("target,steps", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
    ])
def test_steps_to_carry_data(target, steps):
    assert steps_to_carry_data(target) == steps


if __name__ == '__main__':
    SQUARE_TO_RETREIVE = 368078

    print(steps_to_carry_data(SQUARE_TO_RETREIVE))
