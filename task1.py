import requests

TOKEN = ''
urls = [
    f'https://akabab.github.io/superhero-api/api/id/332.json',
    f'https://akabab.github.io/superhero-api/api/id/655.json',
    f'https://akabab.github.io/superhero-api/api/id/149.json',
]  # список адресов


def requests_get(url_all):
    # принимает список адресов
    r = (requests.get(url) for url in url_all)
    return r


def parser():
    # функция парсинга интелекта
    super_man = {}
    names = []
    intelligences = []

    for item in requests_get(urls):
        name = item.json()['name']
        intelligence = item.json()['powerstats']['intelligence']
        names.append(name)
        intelligences.append(intelligence)
        super_man[name] = intelligence
    # print((super_man))

    # for key, value in super_man.items():
    #   print(key, value)

    max_val = max(super_man.values())
    final_dict = {k: v for k, v in super_man.items() if v == max_val}
    print(final_dict)
    for key, value in final_dict.items():
        print(f"Самый интеллектуальный: {key}, интеллект: {value}")


parser()
