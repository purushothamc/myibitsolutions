class Solution:
    def __init__(self):
        pass
    """
    Following is C++ code

    int Solution::titleToNumber(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    long int result = 0, sum = 0, c=0;
    if(A.length() == 0) return 0;
    if(A.length() == 1) return (A[0] - 'A' + 1);
    for(int i=A.length()-1; i>=0; i--) {
        result += pow(26, c)*(A[i] - 'A' + 1);
        c += 1;
    }
    return result;
    }
    """

