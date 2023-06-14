#include <iostream>

using namespace std;

int p[201];

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
	
	if (x != y) {
		p[max(x, y)] = min(x, y);
	}
}

int max(int x, int y) {
	return (x > y) ? x : y;
}

int min(int x, int y) {
	return (x < y) ? x : y;
}

int main(void) {
	int n, m;
	cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int temp;
			cin >> temp;
			if (temp == 1) {
				merge(i+1, j+1);
			}
		}
	}
	
	int visit[m];
	for (int i = 0; i < m; i++) {
		cin >> visit[i];
	}
	
	char* ans = "YES";
	int root = find(visit[0]);
	for (int i = 1; i < m; i++) {
		if (root != find(visit[i])) {
			ans = "NO";
		}
	}
	
	cout << ans;
	
	return 0;
}
