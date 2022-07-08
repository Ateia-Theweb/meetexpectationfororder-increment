"""
    __all__ has the necessary to work the module;

    the first argument to __eq__ is 'a';

    if_not_list does less than if_list for one insertion;

    [::] copies faster than list;

    clear when returncode does not meet expectation;

    pairs retried;

    can be silent
"""

__all__ = ['two2', 'twoN', 'late']

from subprocess import Popen
from sys import argv
from sys import exit
from sys import stdout
from time import sleep
from typing import Callable

insert_to_end = list.append


def if_list(
        insertion: int, out: list, expectation: list, /, *, raze: bool = True
) -> None:
    a = out[::]
    insert_to_end(a, insertion)

    if a == expectation[:len(a)]:
        insert_to_end(out, insertion)
    elif raze:
        out.clear()
    else:
        raise ValueError('does not meet expectation')


def if_not_list(
        insertion: int, out: list, expectation: list, /
) -> None:
    assert not out, 'list'

    a = [insertion]

    if a == expectation[:1]:
        insert_to_end(out, insertion)


# equalitytest
def lis(
        insertion: int, out: list, expectation: list, /
) -> None:
    if not out:
        if_not_list(insertion, out, expectation)
    else:
        if_list(insertion, out, expectation)


def two1(
        insertionm: Callable, insertionn: Callable, out: list, expectation: list, /
) -> None:
    lis(insertionm(), out, expectation)
    print(out)

    if not out:
        return

    lis(insertionn(), out, expectation)
    print(out)


def two2(
        insertionm: Callable, insertionn: Callable, out: list, expectation: list, /
) -> None:
    two1(insertionm, insertionn, out, expectation)

    if not out:
        two1(insertionm, insertionn, out, expectation)


# equalitytest
def twoN(
        insertionm: Callable, insertionn: Callable, out: list, expectation: list, /
) -> None:
    while not (out == expectation):
        two1(insertionm, insertionn, out, expectation)


def main():
    insertionm = late(argv[1:])
    insertionn = insertionm
    out = []
    expectation = [0, 0]

    two2(insertionm, insertionn, out, expectation)


def _patchprint(prin):
    # noinspection PyShadowingBuiltins,PyGlobalUndefined
    global print

    # noinspection PyShadowingBuiltins
    print = prin


def late(commandline):
    def wrapper():
        child_program_in_a_new_process = Popen(commandline)

        s = 0.100

        while child_program_in_a_new_process.poll() is None:
            stdout.write('\r.  ')

            sleep(s)
            stdout.write('\r.. ')

            sleep(s)
            stdout.write('\r...')

            sleep(s)

        return child_program_in_a_new_process.returncode

    return wrapper


if __name__ == '__main__':
    try:
        main()
    except OSError:
        exit(failure := 1)
    else:
        exit(success := 0)
