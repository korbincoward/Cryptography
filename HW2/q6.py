import math

def find_M(m_sub_1, m_sub_2, m_sub_3):
    M = m_sub_1 * m_sub_2 * m_sub_3
    return M

def find_M_sub1(M, m_sub_1):
    M_sub_1 = M//m_sub_1
    return M_sub_1

def find_M_sub2(M, m_sub_2):
    M_sub_2 = M//m_sub_2
    return M_sub_2

def find_M_sub3(M, m_sub_3):
    M_sub_3 = M//m_sub_3
    return M_sub_3

def find_M_negate_1(M_sub_1, m_sub_1):
    i = 1
    while True:
        if (M_sub_1 * i) % m_sub_1 == 1:
            return i
        i += 1

def find_M_negate_2(M_sub_2, m_sub_2):
    j = 1
    while True:
        if (M_sub_2 * j) % m_sub_2 == 1:
            return j
        j += 1

def find_M_negate_3(M_sub_3, m_sub_3):
    l = 1
    while True:
        if (M_sub_3 * l) % m_sub_3 == 1:
            return l
        l += 1


def find_X (a_sub_1, a_sub_2, a_sub_3, M_sub_1, M_sub_2,M_sub_3, M_negate_1, M_negate_2, M_negate_3, M):
    X = (a_sub_1 * M_sub_1 * M_negate_1) + (a_sub_2 * M_sub_2 * M_negate_2) + (a_sub_3 * M_sub_3 * M_negate_3)
    return X % M

if __name__ == "__main__":
   a_sub_1 = 2
   a_sub_2 = 3
   a_sub_3 = 2
   m_sub_1 = 3
   m_sub_2 = 5
   m_sub_3 = 7
   M = find_M(m_sub_1, m_sub_2, m_sub_3)
   M_sub_1 = find_M_sub1(M, m_sub_1)
   M_sub_2 = find_M_sub2(M, m_sub_2)
   M_sub_3 = find_M_sub3(M, m_sub_3)
   M_negate_1 = find_M_negate_1(M_sub_1, m_sub_1)
   M_negate_2 = find_M_negate_2(M_sub_2, m_sub_2)
   M_negate_3 = find_M_negate_3(M_sub_3, m_sub_3)
   X = find_X(a_sub_1, a_sub_2, a_sub_3, M_sub_1, M_sub_2, M_sub_3, M_negate_1, M_negate_2, M_negate_3, M)
   print(M)
   print(M_sub_1)
   print(M_sub_2)
   print(M_sub_3)
   print(M_negate_1)
   print(M_negate_2)
   print(M_negate_3)

   print("X =", X)