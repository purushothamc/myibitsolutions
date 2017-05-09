void combineHelper(vector<int> C, int target, vector<int> &temp, vector<vector<int> > &r, int index) {
    if(target == 0) {
        if(find(r.begin(), r.end(), temp) == r.end()) {
            r.push_back(temp);
        }
        return;
    }
    for(int j=index; j<C.size(); j++) {
        if(target < C[j]) {
            return;
        }
        temp.push_back(C[j]);
        combineHelper(C, target-C[j], temp, r, j);
        temp.pop_back();
    }
}
vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    vector<vector<int> > result;
    if(A.size() == 0 || B <= 0) {
        return result;
    }
    sort(A.begin(), A.end());
    vector<int> temp;
    combineHelper(A, B, temp, result, 0);
    return result;
}