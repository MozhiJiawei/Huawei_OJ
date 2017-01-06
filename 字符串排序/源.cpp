#include <iostream>
#include <string>
using namespace std;

char Capitalization(char s);
bool IsLetter(char s);

int main() {
    string s_input;
    getline(cin, s_input); 
    for (int i = 0; i < s_input.length(); i++) {
        int j = 0;
        while (j < s_input.length() && !IsLetter(s_input[j])) {
            j++;
        }
        int next_j = j + 1;
        while (j < s_input.length()) {
            while (next_j < s_input.length() && !IsLetter(s_input[next_j])) {
                next_j++;
            }
            if (next_j < s_input.length() && IsLetter(s_input[next_j])) {
                if (Capitalization(s_input[j]) > Capitalization(s_input[next_j])) { 
                    swap(s_input[j], s_input[next_j]);
                }
            }
            j = next_j;
            next_j++;
        }
    }
    cout << s_input << endl;
}

char Capitalization(char s) {
    if (s >= 'a' && s <= 'z') {
        s = s + 'A' - 'a';
    }
    return s;
}

bool IsLetter(char s) {
    if (s >= 'A' && s <= 'Z') return true;
    if (s >= 'a' && s <= 'z') return true;
    return false;
}
