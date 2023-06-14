#include <iostream>

using namespace std;

int main(void) {
	int ans = 0;
	int n;
	cin >> n;
	
	int b,c,d,temp;
	for (int i = 1; i <= n; i++) {
		temp = i;
		b = temp/100; temp = temp%100;
		c = temp/10; temp = temp%10;
		d = temp;
		
		if (b == 0)
			ans++;
		else if (b-c == c-d)
			ans ++;
	}
	
	cout << ans;
	return 0;
}
