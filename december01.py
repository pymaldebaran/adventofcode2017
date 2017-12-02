#!/usr/bin/env python
"""--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The
printer's broken! We can't print the Naughty or Nice List!" By the time you
make it to sub-basement 17, there are only a few minutes until midnight. "We
have a big problem," she says; "there must be almost fifty bugs in this system,
but nothing else can print The List. Stand in this square, quick! There's no
time to explain; if you can convince them to pay you in stars, you'll be able
to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than
before. She must have sent you inside the computer! You check the system clock:
25 milliseconds until midnight. With that much time, you should be able to
collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day millisecond in the advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along
one wall. The only door is locked, but it includes a small interface.
"Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove
you're not a human. Apparently, you only get one millisecond to solve the
captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and
find the sum of all digits that match the next digit in the list. The list is
circular, so the digit after the last digit is the first digit in the list.

For example:

*   1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
    second digit and the third digit (2) matches the fourth digit.
*   1111 produces 4 because each digit (all 1) matches the next.
*   1234 produces 0 because no digit matches the next.
*   91212129 produces 9 because the only digit that matches the next one is the
    last digit, 9.

What is the solution to your captcha?

--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door
isn't yet satisfied, but it did emit a star as encouragement. The instructions
change:

Now, instead of considering the next digit, it wants you to consider the digit
halfway around the circular list. That is, if your list contains 10 items, only
include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.

For example:

*   1212 produces 6: the list contains 4 items, and all four digits match the
    digit 2 items ahead.
*   1221 produces 0, because every comparison is between a 1 and a 2.
*   123425 produces 4, because both 2s match each other, but no other digit has
    a match.
*   123123 produces 12.
*   12131415 produces 4.

What is the solution to your new captcha?

"""
from itertools import cycle, tee, islice


# From https://docs.python.org/3.6/library/itertools.html#itertools-recipes
def pairwise(iterable, n=1):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    for _ in range(n):
        next(b, None)
    return zip(a, b)


def solver_part1(seq):
    s = 0
    for cur, nex in islice(pairwise(cycle(seq)), len(seq)):
        if cur == nex:
            s += int(cur)
    return s


def solver_part2(seq):
    s = 0
    for cur, mid in islice(pairwise(cycle(seq), len(seq)//2), len(seq)):
        if cur == mid:
            s += int(cur)
    return s


def test_part1_1():
    assert solver_part1("1122") == 3


def test_part1_2():
    assert solver_part1("1111") == 4


def test_part1_3():
    assert solver_part1("1234") == 0


def test_part1_4():
    assert solver_part1("91212129") == 9


def test_part2_1():
    assert solver_part2("1212") == 6


def test_part2_2():
    assert solver_part2("1221") == 0


def test_part2_3():
    assert solver_part2("123425") == 4


def test_part2_4():
    assert solver_part2("123123") == 12


def test_part2_5():
    assert solver_part2("12131415") == 4


if __name__ == '__main__':
    SEQ = "683763347952248558274598352939674972954641755898815882568823446994"\
        "73595413912688278647235862566123233983921662578792917453912795352746"\
        "42651264996561591958851212556718683741137117987528762148875976142962"\
        "91748869722983491977224234582993231415294131913276224852494958641681"\
        "81327197661454464926326248274999448373741839963155646828842752761293"\
        "14235642296435534952198748321149636128966637577972834595223164945371"\
        "16845391648931518118496533318459989985979911468813617172345179117598"\
        "93792348815818755262456378627116779495435596139617246571678531183335"\
        "95624416387144567424476558644636252915985413753596211718487519227387"\
        "22228998873572923129782861826362329212525747381183475211876378296238"\
        "31872437381979223955675634257889137823684924127338433248519515211796"\
        "73259931492161139973657127722254633236946113627741741979486552412398"\
        "97224923565368323139375974377178737875938494688367336425293785471511"\
        "46397532997237439387663769334722979172954835154486382983716698212694"\
        "35739815339292625527296138462613182967817121956928868559714113235532"\
        "27882541639238883781555739487531854231589978777186876424464574466434"\
        "22536541238979761725496426292359382168535641216124211741896552562128"\
        "94182417224191387353782897617273827698391523224145158942191112156722"\
        "88998539346679547862562236146215546182944671912551533952565247861597"\
        "58429643756586457639177183891162214163549688595416893383194995824534"\
        "24784141424752626821276195491371945211487676474579998279259475375962"\
        "63343196311919178943681167388935487976611118996641383983548189311354"\
        "86984944719992393148681724116616741428937687985152658296679845474766"\
        "47774155363271296867917535645298745976112643721675817118239521939328"\
        "91991489968137628499914846784297935786293312157969967514843757848955"\
        "61682156658579887518746862371751372692472765217374791324656745291574"\
        "78449529947736296467635114818367689712236683865634274594494527526361"\
        "77293598314665656949832172525942378281876128575233442654182278832193"\
        "83138893873384775659548637662867572687198263688597865118173921615178"\
        "16544213398736238272144484495271559295574473987367783884769398237969"\
        "6776"
    print(solver_part1(SEQ))
    print(solver_part2(SEQ))
