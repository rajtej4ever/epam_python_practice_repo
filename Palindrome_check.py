def palindrome_check(string1):
    reverse=string1[::-1]
    return string1==reverse


if palindrome_check("madam")==True:
    print("Palindrome")
else:
    print("Not a Palindrome")