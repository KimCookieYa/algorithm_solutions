#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> dp;

int main() {
	int n, m;
	cin >> n >> m;
	
	for (int i = 0; i <= n; i++) {
		vector<int> v;
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i) {
				v.push_back(1);
			}
			else {
				v.push_back((dp[i-1][j] + dp[i-1][j-1]) % 1000000000);
			}
		}
		
		dp.push_back(v);
	}
	
	int num = dp[n][m];
	int ans = 0;
	while (num%10 == 0) {
		ans++;
		num = num/10;
	}
	
	cout << ans;
	
	return 0;
}
