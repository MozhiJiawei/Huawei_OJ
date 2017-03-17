"""
表示数字（150分）
"""
import re

input_str = input().strip()
print(re.sub(r"(\d+)", r"*\1*", input_str))
