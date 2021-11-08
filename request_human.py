import requests


def test_get_call():
    r = requests.get('https://api.github.com', auth=('user', 'pass'))

    print(r.status_code)
    print(r.headers['content-type'])
    assert r.status_code == 200
