#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a+n);
	
	if (n == 1) {
		cout << a[n-1] * a[n-1];
	}
	else {
		cout << a[0] * a[n-1];
	}
	
	return 0;
}
