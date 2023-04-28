
# 1
strng = "abcTYFYTD"


def count_lower_upper(string):
    lower_count = 0
    upper_count = 0

    for c in string:
        if c == c.lower():
            lower_count += 1
        else:
            upper_count += 1

    print(
        f"no of uppercase lettter : {upper_count} , no of lowercase letter : {lower_count}")


count_lower_upper(strng)

# 2
palindrome_string = "poop"


def is_palindrome(string):
    reversed_string = string[::-1]
    # [from index: till index: steps(-ve step= go backward)]
    # this will include only every nth char in substring
    # from starting index(from idx) to end index (till idx ) of the string on which we are applying split operator
    if reversed_string == string:
        print(f"yes {string} is a palindrome ")
    else:
        print(f"yes {string} is not a palindrome ")


is_palindrome(palindrome_string)

# 3
pangram_string = "The quick brown fox jumps over the lazy dog"
non_pangram_string = "This is not pangram "


def is_pangram(sentence):
    import string

    sentence = sentence.lower()
    alphabet_set = set(string.ascii_lowercase)
    sentence_letter_set = set(filter(lambda x: x.isalpha(), sentence))

    if alphabet_set == sentence_letter_set:
        print("yes it is a pangram")
        return True
    else:
        print("no, it si not a pangram")
        return False


is_pangram(pangram_string)
is_pangram(non_pangram_string)

# 4
def add(*numbers):
    sm = 0
    for n in numbers:
        sm = sm+n
    print(sm)
    return len(locals())


def count_no_of_var(func):
    count = func(1, 2, 3, 4)
    print(f"no of local variable in passed function is/are: {count} ")


count_no_of_var(add)
