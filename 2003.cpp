#include <iostream>

using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	int sum = a[0];
	int ans = 0;
	for (int i = 0; i < n; i++) {
		sum = 0;
		
		for (int j = i; j < n; j++) {
			sum += a[j];
			
			if (sum == m) {
				ans++;
				break;
			} else if (sum > m) {
				break;
			}
		}
	}
	
	cout << ans;
	return 0;
}
