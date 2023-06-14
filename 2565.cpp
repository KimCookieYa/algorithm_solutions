#include <bits/stdc++.h>

using namespace std;

int lis[101];

bool comp(vector<int> &a, vector<int> &b) {
	return a[0] < b[0];
}

int get_max(int a, int b) {
	return a > b ? a : b;
}

int binarySearch(int left, int right, int target) {
	int mid;
	
	while (left < right) {
		mid = (left + right) / 2;
		
		if (target > lis[mid]) {
			left = mid+1;
		}
		else {
			right = mid;
		}
	}
	
	return right;
}

int main(void) {
	int n;
	cin >> n;
	
	vector<vector<int>> arr(n);
	for (int i = 0; i < n; i++) {
		arr[i] = vector<int>(2);
		cin >> arr[i][0] >> arr[i][1];
	}
	
	sort(arr.begin(), arr.end(), comp);
	
	int ix = 0;
	lis[ix] = arr[0][1];
	
	for (int i = 1; i < n; i++) {
		if (lis[ix] < arr[i][1]) {
			lis[++ix] = arr[i][1];
		}
		else {
			int temp = binarySearch(0, ix, arr[i][1]);
			lis[temp] = arr[i][1];
		}
	}
	
	cout << n - ix - 1;
	
	return 0;
}
