#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string alp;
    cin >> alp;

    int nums[26];
    fill_n(nums, 26, -1);

    for (int i = 0; i < alp.size(); i++) {
        char c = alp[i];
        if (nums[c - 'a'] == -1)
        	nums[c - 'a'] = i;
    }

    for (int i = 0; i < 26; i++) {
        cout << nums[i] << ' ';
    }

    return 0;
}
