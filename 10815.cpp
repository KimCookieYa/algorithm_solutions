#include <bits/stdc++.h>

using namespace std;

int a[500000];
int b[500000];

int binarySearch(int left, int right, int target) {
	int mid;
	
	while (left <= right) {
		mid = (left + right) / 2;
		
		if (a[mid] > target) {
			right = mid-1;
		}
		else if (a[mid] < target) {
			left = mid+1;
		}
		else {
			return mid;
		}
	}
	
	return -1;
}

int main(void) {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a+n);
	
	int m;
	cin >> m;
	
	int temp;
	for (int i = 0; i < m; i++) {
		cin >> temp;
		
		if (binarySearch(0, n-1, temp) != -1) {
			b[i]++;
		}
	}
	
	for (int i = 0; i < m; i++) {
		cout << b[i] << ' ';
	}
	
	return 0;
}
