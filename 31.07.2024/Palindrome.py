def is_palindrome(s):
    return s == s[::-1]

input_string = "radar"
print("Is palindrome:", is_palindrome(input_string))
