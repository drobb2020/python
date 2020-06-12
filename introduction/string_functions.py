
def first_half(s):
    return s[:len(s)/2]


def last_half(s):
    return s[len(s)/2:]


if __name__ == '__main__':
    print("Testing string functions")
    assert first_half("abcd") == "ab", "First half is failing"
    assert last_half("abcd") == "d", "Last half is failing"
