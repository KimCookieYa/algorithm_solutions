#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	int a[n];
	stack<int> s;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	int b[n];
	fill_n(b, n, -1);
	for (int i = 0; i < n; i++) {
		while (!s.empty() && a[s.top()] < a[i]) {
			b[s.top()] = a[i];
			s.pop();
		}
		
		s.push(i);
	}
	
	for (int i = 0; i < n; i++) {
		cout << b[i] << ' ';
	}
	
	return 0;
}
