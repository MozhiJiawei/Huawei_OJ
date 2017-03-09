"""
密码强度等级（100分）
"""


def get_password_strength(password):
    element = {'len': len(password), 'letter_lower': 0, 'letter_upper': 0, 'num': 0, 'symbol': 0}
    for c in password:
        if str.isdigit(c):
            element['num'] += 1
        elif str.islower(c):
            element['letter_lower'] += 1
        elif str.isupper(c):
            element['letter_upper'] += 1
        else:
            element['symbol'] += 1

    grade = 0
    if element['len'] <= 4:
        grade += 5
    elif element['len'] <= 7:
        grade += 10
    else:
        grade += 25

    if element['letter_lower'] == 0 and element['letter_upper'] == 0:
        grade += 0
    elif element['letter_lower'] == 0 or element['letter_upper'] == 0:
        grade += 10
    else:
        grade += 20

    if element['num'] == 0:
        grade += 0
    elif element['num'] == 1:
        grade += 10
    else:
        grade += 20

    if element['symbol'] == 0:
        grade += 0
    elif element['symbol'] == 1:
        grade += 10
    else:
        grade += 25

    if element['letter_lower'] != 0 and element['letter_upper'] != 0 and \
                    element['num'] != 0 and element['symbol'] != 0:
        grade += 5
    elif element['letter_upper'] != 0 and element['num'] != 0 and element['symbol'] != 0:
        grade += 3
    elif element['letter_lower'] != 0 and element['num'] != 0 and element['symbol'] != 0:
        grade += 3
    elif element['num'] != 0 and element['symbol'] != 0:
        grade += 2

    if grade >= 90:
        return "VERY_SECURE"
    elif grade >= 80:
        return "SECURE"
    elif grade >= 70:
        return "VERY_STRONG"
    elif grade >= 60:
        return "STRONG"
    elif grade >= 50:
        return "AVERAGE"
    elif grade >= 25:
        return "WEAK"
    else:
        return "VERY_WEAK"


if __name__ == "__main__":
    print(get_password_strength(input()))
