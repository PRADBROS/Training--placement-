def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

input_string = "OpenAI"
print("Number of vowels:", count_vowels(input_string))
