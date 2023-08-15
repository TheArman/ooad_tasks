print('1. Email')
print('2. Website URL (please input full address)')
print('3. Date (please input such as "mm/dd/yyyy)"')
print('4. Number')
print('5. Credit Card Number (please input such as "**** **** **** ****")')
print('6. Mobile Phone Number (please input without county code)')

option = int(input('Choose an option (1-6): '))
if option not in range(1, 7):
    raise ValueError('GAME OVER')

data = input('Enter the data you want to check: ')


def is_valid_email(email):
    if email.count('@') == 1 and '.' in email and len(email) > 4 and '.' in email[email.index(
            '@'):]:  # last condition for example lemver.valesyan@mail.ru
        print('Valid email')
        return
    print('Invalid email')


def is_valid_website_url(url):
    if (url.startswith('https://www.') or url.startswith('http://www.') and url.endswith('.com') and
            url.endswith('.org') or url.endswith('.am') or
            url.endswith('.ru')):  # but if you write https://wwww.com, output will valid))
        print('Valid website URL')
        return
    print('Invalid website URL')


def is_valid_date(date):
    day, month, year = map(int, date.split("/"))
    if day in range(1, 32) and month in range(1, 13) and year > 0:
        print('Valid date')
        return
    print('Invalid date')


def is_valid_number(number):
    try:
        float(number)
        print('Valid number')
    # except ValueError('Invalid number') as e:
    except (ValueError, TypeError):
        print('Invalid number')


def is_valid_credit_card_number(card_number):
    result = card_number.replace(' ', '')  # for removes all ' ' (spaces)
    if result.isdigit() and len(result) == 16:
        print('Valid credit card number')
        return
    print('Invalid credit card number')


def is_valid_mobile_phone_number(phone_number):
    if len(phone_number) == 9 and phone_number.isdigit():  # for armenian phone numbers
        print('Valid mobile phone number')
        return
    print('Invalid mobile phone number')


if option == 1:
    is_valid_email(data)
elif option == 2:
    is_valid_website_url(data)
elif option == 3:
    is_valid_date(data)
elif option == 4:
    is_valid_number(data)
elif option == 5:
    is_valid_credit_card_number(data)
elif option == 6:
    is_valid_mobile_phone_number(data)
