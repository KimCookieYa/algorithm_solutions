#include <bits/stdc++.h>

using namespace std;

int main(void) {
	string num;
	getline(cin, num);
	
	int ans = 0;
	int n = num.length();
	for (int i = 0; i < n; i++) {
		int c = num[i] - '0';
		
		if (0 <= c && c < 10) {
			ans += (c) * pow(16, n-i-1);
		}
		else {
			ans += (c - 'A' + '0' + 10) * pow(16, n-i-1);
		}
	}
	
	cout << ans;
	
	return 0;
}
