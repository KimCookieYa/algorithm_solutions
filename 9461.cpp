#include <iostream>

using namespace std;

long long dp[101] = {0, 1, 1, 1, 2, 2, 3, };

long long P(int n) {
	if (dp[n] > 0) {
		return dp[n];
	}
	
	dp[n] = P(n-1) + P(n-5);
	return dp[n];
}

int main(void) {
	int t;
	cin >> t;
	
	int n;
	while (t--) {
		cin >> n;
		
		cout << P(n) << '\n';
	}
	
	return 0;
}
