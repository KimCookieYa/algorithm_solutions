#include <bits/stdc++.h>

using namespace std;

int dp[31][31];

int func(int a, int b) {
	if (dp[a][b] != 0) {
		return dp[a][b];
	}
	
	if (a == 1) {
		dp[a][b] = b;
		return dp[a][b];
	}
	else if (a == b) {
		dp[a][b] = 1;
		return dp[a][b];
	}
	
	int ans = 0;
	for (int i = b-1; i >= a-1; i--) {
		ans += func(a-1, i);
		//cout << a-1 << ' ' << i << ": " << ans << endl;
	}
	
	dp[a][b] = ans;
	return ans;
}

int main(void) {
	int t;
	cin >> t;
	
	while (t--) {
		int a, b;
		cin >> a >> b;
		
		cout << func(a, b) << endl;
	}
	
	return 0;
}
