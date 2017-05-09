vector<vector<int> > updateResult(vector<vector<int> > r, vector<int> t, int size) {
	vector<int> temp;
	for(int i=0; i<size; i++)
		temp.push_back(t[i]);
	r.push_back(temp);
	return r;
}

vector<vector<int> > subsetsHelper(vector<int> v, vector<int> temp,
									vector<vector<int> > r, int s, int e, int index) {
	r = updateResult(r, temp, index);
	for(int i=s; i<=e; i++) {
		temp[index] = v[i];
		//printVector(temp);
		r = subsetsHelper(v, temp, r, s+1, e, index+1);
		s += 1;
	}
	return r;
}
void subsetHelper(int i, vector<int> & subset, vector<vector<int>> & ans, vector<int> & A){
    if(i==A.size()){
        ans.push_back(subset);
        return;
    }
    subsetHelper(i+1, subset, ans, A);
    subset.push_back(A[i]);
    subsetHelper(i+1, subset, ans, A);
    subset.pop_back();
}
vector<vector<int> > Solution::subsets(vector<int> &A) {
    /*int s, e;
    sort(v.begin(), v.end());
	vector<int> temp(v.size()), empty;
	for(int i=0; i<v.size(); i++)
		temp[i] = 0;
	vector<vector<int> > result;
	result.push_back(empty);
	for(int i=0; i<v.size(); i++) {
		s = i+1; e = v.size() - 1;
		temp[0] = v[i];
		result = subsetsHelper(v, temp, result, s, e, 1);
	}
	return result;*/
	vector< vector<int> > ans;
    vector<int> subset;
    sort(A.begin(), A.end());
    subsetHelper(0, subset, ans, A);
    sort(ans.begin(), ans.end());
    return ans;
}

