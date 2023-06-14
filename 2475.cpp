#include <iostream>

using namespace std;

int main(void) {
	int n = 5;
	int ans = 0;
	int a[n];
	while (n--) {
		cin >> a[n];
		a[n] = a[n] * a[n];
		ans += a[n];
	}
	
	cout << ans % 10;
	
	return 0;
}
