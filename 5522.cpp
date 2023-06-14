#include <iostream>

using namespace std;

int main(void) {
	int a[5];
	int ans = 0;
	for (int i = 0; i < 5; i++) {
		cin >> a[i];
		ans += a[i];
	}
	
	cout << ans;
	
	return 0;
}
