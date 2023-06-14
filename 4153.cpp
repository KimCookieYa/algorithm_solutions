#include <iostream>

using namespace std;

int main(void) {
	while (1) {
		int x, y, z;
		cin >> x >> y >> z;
		
		if (!(x || y || z)) {
			break;
		}
		
		x = x*x;
		y = y*y;
		z = z*z;
		
		if (x == y+z || y == x+z || z == x+y) {
			cout << "right\n";
		}
		else {
			cout << "wrong\n";
		}
	}
	
	return 0;
}
