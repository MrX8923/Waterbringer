from django.core.exceptions import ValidationError
from string import ascii_letters


def name_check(val: str) -> None:
    if val[0].islower():
        raise ValidationError('Должно начинаться с заглавной буквы')
    elif not val.isalpha():
        raise ValidationError('Должно состоят только из букв')


def email_check(val: str) -> None:
    if len(val) > 50:
        raise ValidationError('')
    if '@' not in val:
        raise ValidationError('Нет знака "@" в адресе почты')
    if val.count('@') > 1:
        raise ValidationError('В строке может быть только один знак "@"')

    local_name = val[:val.find('@')]
    domain_name = val[val.find('@') + 1:]
    for i in local_name:
        if i in '<>()[]@,;:\\/"* ':
            raise ValidationError('Локальное имя не должно содержать знаков:'
                                  ' < > ( ) [ ] @ , ; : \\ / " * и пробела')
    if '.' not in domain_name:
        raise ValidationError('Имя домена должно содержать две текстовые строки,'
                              ' разделенные точкой, например, ups.com')
    if domain_name[-1] == '-':
        raise ValidationError('Последний символ не может быть знаком минуса, дефисом или точкой')
    for i in domain_name:
        if i not in ascii_letters and i not in '-0123456789.':
            raise ValidationError('Имя домена может состоять из букв от A до Z (верхний или нижний регистры),'
                                  ' цифры от 0 до 9 и знак минус (-)')


def phone_number_check(val: str) -> None:
    if len(val) != 12:
        raise ValidationError('В строке должно быть 12 символов')
    if val[0] != '+':
        raise ValidationError('Номер должен начинаться с "+"')
    if not val[1:].isnumeric():
        raise ValidationError('Номер должен состоять только из цифр после знака "+"')
