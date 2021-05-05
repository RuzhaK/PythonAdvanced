# def palindrome(word, index):
#     if len(word)==0:
#         return f"{word} is a palindrome"
#     elif len(word)==1:
#         return f"{word} is a palindrome"
#     is_not_palindrome='not' in palindrome(word[1:-1],index)
#     if word[0]==word[-1] and not is_not_palindrome:
#         return f"{word} is a palindrome"
#     return f"{word} is not a palindrome"

def palindrome(word, index):
    if index>=int(len(word)/2):
        return f"{word} is a palindrome"
    if word[index]==word[len(word)-1-index]:
        return palindrome(word, index+1)
    return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
