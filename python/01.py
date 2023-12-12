from inputs import Input01
import re, timeit


def task01():
    return sum(
        [
            int((d := re.findall("\d", l))[0] + d[-1])
            for l in Input01.splitlines()
            if l != ""
        ]
    )


def task01Original():
    return sum(
        [
            int(re.search("\d", l).group() + re.search("\d", l[::-1]).group())
            for l in Input01.splitlines()
            if l != ""
        ]
    )


def doCalibration(arr=Input01):
    result = 0
    for entry in arr:
        # digits = [char for char in entry if char.isdigit()]
        digits = re.findall("\d")
        result += int(digits[0] + digits[-1]) if digits else 0
    return result


if __name__ == "__main__":
    print(f"Alice:    {timeit.timeit('task01()', globals=globals(), number=100)}")
    print(task01(), "\n")

    print(
        f"AliceOld: {timeit.timeit('task01Original()', globals=globals(), number=100)}"
    )
    print(task01Original(), "\n")

    print(
        f"Amelia    {timeit.timeit('task01Original()', globals=globals(), number=100)}"
    )
    print(task01Original(), "\n")
