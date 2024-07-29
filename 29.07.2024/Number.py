string = input("Enter a string: ").lower()
vowels = "aeiou"
count = {vowel: 0 for vowel in vowels}

for char in string:
    if char in vowels:
        count[char] += 1

print("Vowel counts:", count)
