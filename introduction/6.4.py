
def reverse(s):
    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s) - i - 1]
    return new_str


print(reverse("123"))
print(reverse("abcde"))
print(reverse("11121"))


def is_palindrome(p):
    for i in range(len(p)//2):
        if p[i] != p[len(p) - i - 1]:
            print("No this word is not a palindrome")
            return

    print("Yes this word is a palindrome")


is_palindrome("1")
is_palindrome("1221")
is_palindrome("abba")
is_palindrome("david")
