import requests
from bs4 import BeautifulSoup


def get_url(path: str, port=8000):
    return f"http://localhost:{port}{path}"


def get_root():
    path = "/"
    url = get_url(path)
    response = requests.get(url)
    print(response)
    print(response.status_code)
    return response


def get_person_list():
    path = "/person/"
    url = get_url(path)
    response = requests.get(url)
    print(response)
    print(response.status_code)


def get_person(person_id):
    path = "/person/"
    url = get_url(path)
    response = requests.get(url, params={"id": person_id})
    print(response)
    print(response.status_code)
    print(response.request.url)
    return response


def create_person(name: str, age: int, path="/create/", headers=None, auth=None):
    url = get_url(path)
    form = {
        "name": name,
        "age": age,
    }
    response = requests.post(url, data=form, headers=headers, auth=auth)
    print(response)
    print(response.status_code)
    print(response.url)
    print(response.request.url)
    print(response.history)
    print("-- history:")
    for resp in response.history:
        print("*", resp.status_code)
        print(resp.request.url)
        print(resp.url)
        print(resp.headers)


def demo_soup_persons_list():
    response = get_root()
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)

    one_a = soup.find("a")
    print(one_a)

    all_a = soup.find_all("a")
    print(len(all_a), all_a)

    buttons = soup.find_all("a", {"class": "btn"})
    print(buttons)
    buttons_danger = soup.find_all("a", {"class": "btn-danger"})
    print(buttons_danger)
    button_danger = soup.find("a", {"class": "btn-danger"})
    print(button_danger)
    print(button_danger.text)
    print(button_danger.get("href"))
    print(button_danger.get("class"))

    # div = soup.find("div")
    # print(div)

    div = soup.find("div", {"class": "row"})
    print(div)


def demo_soup_person():
    response = get_person(7)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    text = soup.find("text")
    print(text)
    link = soup.find("a", {"class": "card-link"})
    print(link)
    print(link.text)
    print(link.get("href"))
    print(link.get("class"))


def main():
    # get_root()
    # get_person_list()
    # get_person(7)
    # get_person(777)
    # create_person("Leo", 345)
    # create_person("Sam", 567)
    # create_person("Jack", 678)
    # create_person("Ann", 890)
    # create_person("Clark", 1234)
    # create_person("Kate", 432, "/create-auth/")
    # create_person("Kate", 432, "/create-auth/", auth=("admin", "admin123456"))

    # headers_auth = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
    #     "Cookie": "csrftoken=OwY1safjhF4dHhjg4EmJaaAbdqe8Kaw6AVMRTpEPL4HDzc3OYL86jzEVRSRi6vQV; sessionid=5hx24pk3yedjb5908ng0fitpxazx7q8x;",
    # }
    # create_person("Kate", 432, "/create-auth/", headers=headers_auth)

    demo_soup_persons_list()
    demo_soup_person()


if __name__ == "__main__":
    main()
