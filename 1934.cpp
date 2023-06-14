#include <iostream>

using namespace std;

int get_gcd(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int get_lcm(int a, int b) {
	return a*b/get_gcd(a, b);
}

int main(void) {
    int t;
    cin >> t;
    
    while (t--) {
        int a, b;
        cin >> a >> b;
        
        cout << get_lcm(a, b) << endl;
    }
    
    return 0;
}
