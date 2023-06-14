#include <bits/stdc++.h>

using namespace std;

int arr[10001];
int dp[10001][2];

int main(void) {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	if (n == 1) {
		cout << arr[0];
		
		return 0;
	}
	
	dp[0][0] = arr[0]; dp[0][1] = arr[0];
	dp[1][0] = arr[1]; dp[1][1] = arr[1] + dp[0][0];
	for (int i = 2; i < n; i++) {
		dp[i][0] = arr[i] + max(dp[i-2][0], dp[i-2][1]);
		dp[i][1] = arr[i] + dp[i-1][0];
		
		//dp[i][0] = max(dp[i][0], dp[i-1][0]);
		cout << dp[i][0] << ' ' << dp[i][1] << endl;
	}
	
	cout << max(max(dp[n-1][0], dp[n-1][1]), dp[n-2][1]);
	
	return 0;
}
