
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if len(S) == 0:
        return len(T)
    if len(T) == 0:
        return len(S)
    if S[0] == T[0]:
        return MED(S[1:], T[1:])
    return 1 + min(MED(S[1:], T), MED(S, T[1:]), MED(S[1:], T[1:]))


def fast_MED(S, T, MED_func):
    if len(S) == 0:
        return len(T)
    if len(T) == 0:
        return len(S)
    min_cost = MED_func(S[1:], T[1:]) + (0 if S[0] == T[0] else 1)
    insert_cost = MED_func(S, T[1:])
    if insert_cost < min_cost:
        min_cost = insert_cost
    delete_cost = MED_func(S[1:], T)
    if delete_cost < min_cost:
        min_cost = delete_cost
    return min_cost


def build_MED(S, T, MED_func):
    memo = {}
    return MED_func(S, T)



def fast_align_MED(S, T, MED_func):
    if len(S) == 0:
        return "-" * len(T), T
    if len(T) == 0:
        return S, "-" * len(S)

    insert_S, insert_T = fast_align_MED(S, T[1:], MED_func)
    delete_S, delete_T = fast_align_MED(S[1:], T, MED_func)
    substitute_S, substitute_T = fast_align_MED(S[1:], T[1:], MED_func)

    min_cost = MED_func(S, T)
    align_S, align_T = S, T

    if MED_func(insert_S, insert_T) + 1 < min_cost:
        min_cost = MED_func(insert_S, insert_T) + 1
        align_S = "-" + insert_S
        align_T = T[0] + insert_T

    if MED_func(delete_S, delete_T) + 1 < min_cost:
        min_cost = MED_func(delete_S, delete_T) + 1
        align_S = S[0] + delete_S
        align_T = "-" + delete_T

    if MED_func(substitute_S, substitute_T) + (S[0] != T[0]) < min_cost:
        min_cost = MED_func(substitute_S, substitute_T) + (S[0] != T[0])
        align_S = S[0] + substitute_S
        align_T = T[0] + substitute_T

    return align_S, align_T


def test_align():
  S = "kitten"
  T = "sitting"
  aligned_S, aligned_T = fast_align_MED(S, T, MED)
  print("S:", aligned_S)
  print("T:", aligned_T)

test_align()
