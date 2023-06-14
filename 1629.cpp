#include <bits/stdc++.h>

using namespace std;

int a,b,c;

int power(int n, int k) {
	if (k == 0) {
		return 1;
	}
	
	int temp = power(n, k/2);
	int ans = 1LL * temp * temp % c;
	
	if (k%2)
		ans = 1LL * ans * n % c;
	
	return ans;
}

int main(void) {
	cin >> a >> b >> c;
	
	cout << power(a, b);
	return 0;
}
