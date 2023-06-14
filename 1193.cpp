#include <iostream>

using namespace std;

int func(int x) {
	return x*(x+1)/2;
}

int main(void) {
	int n;
	cin >> n;
	
	int x = 0;
	int ans;
	while (1) {
		if (func(x-1) < n && n <= func(x)) {
			ans = x - (func(x) - n);
			break;
		}
		x++;
	}
	
	if (x%2 == 0) {
		cout << ans << '/' << (x+1) - ans;
	}
	else {
		cout << (x+1) - ans << '/' << ans;
	}
	
	return 0;
}
