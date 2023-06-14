#include <bits/stdc++.h>

using namespace std;
using ull = unsigned long long;

int main(void) {
	int n;
	cin >> n;
	
	ull d[n-1];
	ull p[n];
	for (int i = 0; i < n-1; i++) {
		cin >> d[i];
	}
	
	int min = 1000000000;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
		if (min > p[i]) {
			min = p[i];
		}
		p[i] = min;
	}
	
	ull ans = 0;
	for (int i = 0; i < n-1; i++) {
		ans += d[i] * p[i];
	}
	
	cout << ans;
	
	return 0;
}
