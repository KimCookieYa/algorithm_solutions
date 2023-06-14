#include <iostream>

using namespace std;

int func(int x) {
	if (x == -1)
		return -1;
	return 3*x*x + 3*x + 1;
}

int main(void) {
	int n;
	cin >> n;
	
	int ans = 0;
	while (1) {
		if (func(ans-1) < n && n <= func(ans)) {
			ans++;
			break;
		}
		else {
			ans++;
		}
	}
	
	cout << ans;
	
	return 0;
}
