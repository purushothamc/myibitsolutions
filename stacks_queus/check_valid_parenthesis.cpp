int Solution::isValid(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    stack<char> s;
    int ln = A.length();
    for(int i=0; i<ln; i++) {
        if(A[i] == '{' || A[i] == '(' || A[i] == '[')
            s.push(A[i]);
        else if(A[i] == '}' || A[i] == ')' || A[i] == ']') {
            if(s.empty())
                return 0;
            char c = s.top();
            if( (A[i] == '}' && c != '{') || (A[i] == ')' && c != '(') || (A[i] == ']' && c != '[') )
                return 0;
            s.pop();
        }
    }
    if(!s.empty())
        return 0;
    return 1;
}
