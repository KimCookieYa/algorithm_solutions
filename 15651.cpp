#include <bits/stdc++.h>

using namespace std;

int n, m;
int arr[9];

void render(void) {
	for (int i = 1; i <= m; i++) {
		cout << arr[i] << ' ';
	}
	cout << '\n';
}

void func(int x) {
	if (x < 1) {
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		arr[m-x+1] = i;
		func(x-1);
		if (x == 1) {
			render();
		}
	}
}

int main(void) {
	cin >> n >> m;
	
	func(m);
	
	return 0;
}
