#include <string>
#include <iostream>
using namespace std;

enum CharType {
    EnglishChar, BlankChar, NumberChar, OtherChar
};

CharType getCharType(char c) {
    if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z') {
        return CharType::EnglishChar;
    }
    else if (c == ' ') {
        return CharType::BlankChar;
    }
    else if (c >= '0' && c <= '9') {
        return CharType::NumberChar;
    }
    else {
        return CharType::OtherChar;
    }
}

int main() {
    string str;
    getline(cin, str);
    int englishCount = 0, blankCount = 0, numberCount = 0, otherCount = 0;
    for (char c : str) { 
        switch (getCharType(c)) {
        case CharType::EnglishChar:
            englishCount++;
            break;
        case CharType::BlankChar:
            blankCount++;
            break;
        case CharType::NumberChar:
            numberCount++;
            break;
        case CharType::OtherChar:
            otherCount++;
            break;
        default:
            break;
        }
    }
    cout << englishCount << endl << blankCount << endl << numberCount << endl << otherCount << endl;
    return 0;
}