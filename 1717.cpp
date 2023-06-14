#include <bits/stdc++.h>

using namespace std;

int p[1000001];

int find(int i) {
	if (p[i] == 0) {
		return i;
	}
	
	p[i] = find(p[i]);
	return p[i];
}

void merge(int x, int y) {
	x = find(x);
	y = find(y);
	
	if (x == y) {
		return;
	}
	
	p[y] = x;
}

int main(void) {
	int n, m;
	cin >> n >> m;
	
	while (m--) {
		int op, x, y;
		cin >> op >> x >> y;
		
		if (op == 0) {
			merge(x, y);
		}
		else {
			x = find(x); y = find(y);
			if (x == y) {
				cout << "YES" << '\n';
			}
			else {
				cout << "NO" << '\n';
			}
		}
	}
	
	return 0;
}
