class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        import math
        primes = [True for i in xrange(0, A+1)]
        primes[0], primes[1] = False, False
        for i in xrange(2, A+1):
            if primes[i]:
                for j in xrange(i*i, A+1, i):
                    primes[j] = False
        for j in xrange(2, A+1):
            if primes[j] and primes[A-j]:
                return j, A-j

P = Solution()
print P.primesum(4)

"""
bool verifyPrime(int A) {
    int n = (int)sqrt(A) + 1;
    bool isPrime = true;
    for(int i=2; i<n; i++) {
        if(A%i == 0) {
            isPrime = false;
            break;
        }
    }
    if(isPrime) return true;
    else return false;
}
vector<int> Solution::primesum(int A) {
    for(int i=2; i<=A; i++) {
        if(verifyPrime(i) && verifyPrime(A-i)) {
            vector<int> v;
            v.push_back(i);
            v.push_back(A-i);
            return v;
        }
    }
}
"""