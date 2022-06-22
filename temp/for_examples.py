import string



def pass_strength(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    if len(value) < 8:
        return 'Too Weak'
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return 'Weak'
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Very Good'
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or any(e in digits for e in value) and any(e in uppers for e in value) or any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Good'

if __name__ == '__main__':
    assert pass_strength('') == 'Too Weak'
    assert pass_strength('1234567') == 'Too Weak'
    assert pass_strength('qwerty') == 'Too Weak'
    assert pass_strength('QWERTY') == 'Too Weak'
    assert pass_strength('QWErt3') == 'Too Weak'
    assert pass_strength('12345678') == 'Weak'
    assert pass_strength('qwertyui') == 'Weak'
    assert pass_strength('qwertyuip') == 'Weak'
    assert pass_strength('QWERTYUI') == 'Weak'
    assert pass_strength('QWERTYUIP') == 'Weak'
    assert pass_strength('12345qwerty') == 'Good'
    assert pass_strength('12345QWERTY') == 'Good'
    assert pass_strength('123qweQWE') == 'Very Good'
    assert pass_strength('123435qweQWE') == 'Very Good'
    assert pass_strength('QWEEw23423') == 'Very Good'
    assert pass_strength('QWEEw23423@') == 'Very Good'
    assert pass_strength('Qweew234343223@') == 'Very Good'
