#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string x, y;
	cin >> x >> y;
	
	string ans;
	for (int i = 2; i >= 0; i--) {
		if (x[i] > y[i]) {
			ans = x;
			break;
		}
		else if (x[i] < y[i]) {
			ans = y;
			break;
		}
	}
	
	cout << ans[2] << ans[1] << ans[0] << endl;
	return 0;
}
