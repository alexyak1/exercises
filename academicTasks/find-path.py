# You are given an undericted graph consisting of N vertices, numbered from 1 to N,
# and M edges.


def solution(N, A, B):
    i = 0
    pairs = {}
    for a_element in A:
        if is_pair(a_element, B[i]):
            pairs[a_element] = B[i]
        i = i + 1

    return check_chane(N, pairs)


def is_pair(first_elemet, second_element):
    if first_elemet + 1 == second_element or first_elemet - 1 == second_element:
        return True
    return False


def check_chane(N, pairs):
    prev_pair = []
    for x in pairs:
        if not prev_pair:
            prev_pair = [x, pairs[x]]
            continue

        if x in prev_pair or pairs[x] in prev_pair:
            if N == x or N == pairs[x]:
                return True

            prev_pair = [x, pairs[x]]
            continue

    return False
