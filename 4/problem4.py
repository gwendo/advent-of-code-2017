
def is_valid_password(password):
    words = []
    password.split(None)
    for word in password.split(None):
        if word in words:
            return False
        else:
            words.append(word)
    return True


def is_anagram_password(password):
    words = []
    password.split(None)
    for word in password.split(None):
        sorted_word = "".join(sorted(word))
        if sorted_word in words:
            return False
        else:
            words.append(sorted_word)
    return True


def find_valid_passwords(file_name, func):
    with open(file_name) as testfile:
        content = testfile.readlines()
    return len(filter(func, content))
