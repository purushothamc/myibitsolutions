def gcd(self, A, B):
    if A < B:
        A, B = B, A
    while B:
        C = A % B
        A = B
        B = C
    return A


def cpFact(self, A, B):
    while self.gcd(A, B) != 1:
        A = A / self.gcd(A, B)
    return A