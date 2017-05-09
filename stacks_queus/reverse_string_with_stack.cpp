string Solution::reverseString(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    stack<char> s;
    for(int i=0; i<A.length(); i++)
        s.push(A[i]);
    int i = 0;
    while(!s.empty()) {
        A[i] = s.top();
        s.pop();
        i += 1;
    }
    return A;
}
