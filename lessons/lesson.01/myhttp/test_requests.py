import requests
import random
from bs4 import BeautifulSoup


def abs_url(url, port=8000):
    return f'http://127.0.0.1:{port}{url}'


def test_http_get_index():
    url = '/'
    response = requests.get(abs_url(url))
    assert response.status_code == 200


def test_http_get_params_detail():
    url = '/person/'
    response = requests.get(abs_url(url), params={'id': '1'})
    assert response.status_code == 200
    response = requests.get(abs_url(url), params={'id': '10000'})
    assert response.status_code == 404
    response = requests.get(abs_url(url))
    assert response.status_code == 404


def test_post_not_auth():
    url = '/create/'
    response = requests.get(abs_url(url))
    assert response.status_code == 200
    response == requests.post(abs_url(url), data={'name': 'Mark', 'age': random.randint(1, 100)})
    assert response.status_code == 200


def test_post_auth():
    url = '/create-auth/'
    response = requests.get(abs_url(url))
    assert response.status_code == 404

    # response = requests.get(abs_url(url), auth=('admin', 'admin123456'))
    # assert response.status_code == 200

    # session = requests.Session()
    # session.auth = ('admin', 'admin123456')
    #
    # response = session.get(abs_url(url))
    # assert response.status_code == 200

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    #            'Cookie': 'csrftoken=esXp1bCa9zsLQjznqo1w688nIJohppsg5XsJ1jabihNpgbfIi62jZqlWBDif9PB4; sessionid=8ykujv76stb5vsw47q5h2lygvyj0m7hk'}
    # response = requests.get(abs_url(url), headers=headers)
    # assert response.status_code == 200
    #
    # response == requests.post(abs_url(url), data={'name': 'Bob', 'age': random.randint(1, 100)}, headers=headers)
    # assert response.status_code == 200


def test_bs4_class():
    url = '/'
    response = requests.get(abs_url(url))
    soup = BeautifulSoup(response.text, "html.parser")
    buttons = soup.findAll('a', {'class': 'btn-primary'})
    href = buttons[0].get('href')
    assert href == '/create/'


def test_bs4_js():
    url = '/person/'
    response = requests.get(abs_url(url), params={'id': '1'})
    soup = BeautifulSoup(response.text, "html.parser")
    texts = soup.findAll('text', {'class': 'text-danger'})
    assert texts == []
