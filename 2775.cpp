#include <iostream>

using namespace std;

int func(int k, int n) {
	if (k == 0) {
		return n;
	}
	
	int sum = 0;
	for (int i = 1; i <= n; i++) {
		sum += func(k-1, i);
	}
	return sum;
}

int main(void) {
	int t, k, n;
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		cin >> k >> n;
		cout << func(k, n) << endl;
	}
	
	return 0;
}
