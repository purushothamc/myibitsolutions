void getCombinations(string A, vector<string> &r,
                     map<int, string> lookup, int sIdx,int mIdx, string temp) {
    if(sIdx == A.size()) {
        r.push_back(temp);
        return;
    }
    int k = A[sIdx] - '0';
    for(int j=0; j<lookup[k].size(); j++) {
        temp.push_back(lookup[k][j]);
        getCombinations(A, r, lookup, sIdx+1, j+1, temp);
        temp.pop_back();
    }
}
vector<string> Solution::letterCombinations(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    map<int, string> lookup;
    lookup[0] = "0";
    lookup[1] = "1";
    lookup[2] = "abc";
    lookup[3] = "def";
    lookup[4] = "ghi";
    lookup[5] = "jkl";
    lookup[6] = "mno";
    lookup[7] = "pqrs";
    lookup[8] = "tuv";
    lookup[9] = "wxyz";
    vector<string> result;
    if(A.empty()) {
        return result;
    }
    string temp;
    getCombinations(A, result, lookup, 0, 0, temp);
    return result;
}
