def decodekey(test_key):
    if test_key:
        if int(test_key) < 20:
            return True
        else:
            return False
    return False
