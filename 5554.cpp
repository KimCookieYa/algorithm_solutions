#include <iostream>

using namespace std;

int main(void) {
	int a[4];
	int ans = 0;
	for (int i = 0; i < 4; i++) {
		cin >> a[i];
		ans += a[i];
	}
	
	cout << ans/60 << '\n' << ans%60;
	
	return 0;
}
