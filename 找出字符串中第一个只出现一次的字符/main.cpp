#include <iostream>
#include <vector>
#include <string>
using namespace std;

class MyChar {
public:
    MyChar(int position, int n) :position_(position), n_(n) {}
    int position_, n_;
};

int main() {
    vector<MyChar> mark(255, MyChar(0, 0)); 
    string str;
    getline(cin, str);
    for (int i = 0; i < str.length(); i++) {
        int ascii = str[i];
        if (mark[ascii].n_ == 0) {
            mark[ascii].position_ = i;
        }
        mark[ascii].n_++;
    }
    int first_position = str.length();
    for (MyChar my_char : mark) {
        if (my_char.n_ == 1) {
            first_position = my_char.position_ < first_position ? my_char.position_ : first_position;
        }
    }
    if (first_position == str.length()) {
        cout << '.' << endl;
    }
    else {
        cout << str[first_position] << endl;
    }
    return 0;
}