#include <iostream>

using namespace std;

int main(void) {
	int x, y;
	int w, h;
	cin >> x >> y >> w >> h;
	
	if (x > w/2) {
		x = w-x;
	}
	
	if (y > h/2) {
		y = h-y;
	}
	
	int ans = (x < y) ? x : y;
	cout << ans;
	
	return 0;
}
