void combineHelper(int total, int next, int len, int k,
                                    vector<int> temp, vector<vector<int> > & r) {
    if(len == k) {
        r.push_back(temp);
        return;
    }
    if(len > k || next > total) {
        return;
    }
    combineHelper(total, next+1, len, k, temp, r);
    temp.push_back(next);
    combineHelper(total, next+1, len+1, k, temp, r);
    temp.pop_back();
}

vector<vector<int> > Solution::combine(int n, int k) {
    vector<vector<int>> result;
    if(n < k) {
        return result;
    }
    vector<int> temp;
    combineHelper(n, 1, 0, k, temp, result);
    sort(result.begin(), result.end());
    return result;
}