import itertools


def check_fun_bbq_not_unique(fun, bbq):
    """
    Check that the 'FUN' and 'BBQ' variable values are unique with
    respect to each other.

    arguments:
        fun(int): integer representing 'FUN' codeword
        bbq(int): integer representing 'BBQ' codeword

    returns:
        boolean
    """
    fun_set = set(str(fun))
    bbq_set = set(str(bbq))

    if len(fun_set.union(bbq_set)) != 5:
        return True
    else:
        return False


def check_summer_not_unique(fun, bbq, summer):
    """
    Check that 'SUMMER' variable values are almost unique to 'FUN'
    (excluding the 'U' variable) and completely unique to 'BBQ'.
    Also check that the 'SUMMER' variable values are unique to each other.

    arguments:
        fun(int): integer representing 'FUN' codeword
        bbq(int): intger representing 'BBQ' codeword
        summer(int) integer repsenting 'SUMMER' codeword

    :returns:
        boolean

    """
    fun_set = set(str(fun))
    bbq_set = set(str(bbq))
    summer_set = set(str(summer))

    summer_fun_union = fun_set.union(summer_set)
    summer_bbq_union = bbq_set.union(summer_set)

    if len(summer_fun_union) != 7 or len(summer_bbq_union) != 7 or len(summer_set) != 5:
        return True
    else:
        return False


solution_list = []
solution_count = 0
digits = list(range(0, 10))

fun_perm = itertools.permutations(digits, 3)
bbq_perm = itertools.permutations(digits, 2)

# convert permutation tuples to list of ints
fun_ints = [int(str(perm[0]) + str(perm[1]) + str(perm[2])) for perm in fun_perm]
bbq_ints = [int(str(perm[0]) + str(perm[0]) + str(perm[1])) for perm in bbq_perm]


for fun in fun_ints:
    for bbq in bbq_ints:
        if check_fun_bbq_not_unique(fun, bbq):
            continue
        summer = (fun * bbq)
        fun_str = str(fun)

        # check that the 'SUMMER' product satisfies the constraint:
        # 'SUMMER' can only represent a six-digit number
        if summer < 100000 or summer > 999999:
            continue
        (s, u, m1, m2, e, r) = str(summer)

        # check that the 'SUMMER' product satisfies the constraints:
        # the 'MM' variables have the same value,
        # the 'U' value in 'SUMMER' equates to 'U' value in 'FUN'
        if m1 != m2 or u != fun_str[1]:
            continue

        if check_summer_not_unique(fun, bbq, summer):
            continue
        solution_list.append((fun, bbq, summer))
        solution_count += 1


print("No. of unique solutions:{}".format(solution_count))
for solution in solution_list:
    print("  {}".format(solution[0]))
    print("X {}".format(solution[1]))
    print("--------")
    print(solution[2])
    print("")
