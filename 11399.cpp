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
	int temp = 0;
	for (int i = 0; i < n; i++) {
		a[i] = temp + a[i];
		temp = a[i];
	}
	
	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans += a[i];
	}
	
	cout << ans;
	
	return 0;
}
