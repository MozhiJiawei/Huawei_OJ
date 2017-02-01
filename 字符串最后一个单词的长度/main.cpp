#include <string>
#include <iostream>
using namespace std;

int main() {
    string str;
    getline(cin, str);
    for (int i = str.length() - 1; i>=0; i--) {
        if (str[i] == ' ') {
            str.erase(i, 1);
        }
        else {
            break;
        }
    }
    size_t found = str.rfind(' ');
    if (found != string::npos) {
        cout << str.length() - found - 1 << endl;
    }
    else {
        cout << str.length() << endl;
    }
    return 0;
}