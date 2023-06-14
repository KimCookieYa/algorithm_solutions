#include <iostream>

using namespace std;

int dp[21] = {0, 1, };	

int fibonacci(int n) {
	if (n == 0 || n == 1)
		return dp[n];
	if (dp[n] != 0)
		dp[n];
	
	return dp[n] = fibonacci(n-1) + fibonacci(n-2);
}

int main(void) {
	int n;
	cin >> n;
	
	cout << fibonacci(n);
	
	return 0;
}
