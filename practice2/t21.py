class TreeCheck:
    def __init__(self, choices, index, comparison_options):
        self.index = index
        self.choices = choices
        self.comparison_options = comparison_options

    def check(self, arr):
        for i in range(len(self.comparison_options)):
            if arr[self.index] == self.comparison_options[i]:
                if type(self.choices[i]) is TreeCheck:
                    return self.choices[i].check(arr)

                return self.choices[i]


def init():
    level4 = [
        TreeCheck([0, 1, 2], 0, ['csv', 'cool', 'apex']),
        TreeCheck([3, 4, 5], 0, ['csv', 'cool', 'apex']),
        TreeCheck([6, 7], 3, ['pod', 'org']),
        TreeCheck([8, 9, 10], 2, [1985, 2014, 1972]),
        11
    ]

    level3 = [
        TreeCheck([level4[0], level4[1]], 3, ['pod', 'org']),
        TreeCheck([level4[2], level4[3], level4[4]], 0, ['csv', 'cool', 'apex'])
    ]

    level2 = [
        TreeCheck([level3[0], level3[1]], 4, [1980, 1986]),
        12
    ]

    return TreeCheck([level2[0], level2[1]], 1, [2012, 1981])


def f21(arr):
    tree_check = init()
    return tree_check.check(arr)


if __name__ == '__main__':
    print(f21(['apex', 1981, 2014, 'org', 1986]))
    print(f21(['apex', 2012, 1972, 'org', 1980]))
