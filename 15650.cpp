#include <bits/stdc++.h>

using namespace std;

int n, m;
bool check[9];
int arr[9];

void render(void) {
	for (int i = 1; i <= m; i++) {
		cout << arr[i] << ' ';
	}
	cout << '\n';
}

void func(int ix, int x) {
	if (x < 1) {
		return;
	}
	
	for (int i = ix; i <= n; i++) {
		if (!check[i]) {
			check[i] = true;
			arr[m-x+1] = i;
			func(i, x-1);
			if (x == 1) {
				render();
			}
			check[i] = false;
		}
	}
}

int main(void) {
	cin >> n >> m;
	
	func(1, m);
	
	return 0;
}
