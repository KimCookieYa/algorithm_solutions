#include <iostream>

using namespace std;

int length[1001];

int binarySearch(int left, int right, int target) {
	int mid;
	
	while (left < right) {
		mid = (left + right) / 2;
		
		if (target > length[mid]) {
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
	
	int arr[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	int ix = 0;
	length[ix] = arr[0];
	
	for (int i = 1; i < n; i++) {
		if (length[ix] < arr[i]) {
			length[++ix] = arr[i];
		}
		else {
			int temp = binarySearch(0, ix, arr[i]);
			length[temp] = arr[i];
		}
	}
	
	cout << ix+1;
	
	return 0;
}
