
# coding: utf-8

# In[11]:


import requests

API_KEY = 'trnsl.1.1.20180924T214001Z.9171962a8a083c49.9851360cd6f35133247689788a7c562a05961e1b'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

f = input('Укажите полный путь к .txt файлу: ')
f2 = input('Укажите полный путь в директорию, куда будет записан результат, с названием файла: ')
lang1 = input('C какого языка переводим?(Формат ввода 2 буквы "ru", "de")')
lang2 = input('На какой язык переводим?(Формат ввода 2 буквы "ru", "de")')
file = open(f, 'rb').read()


def translate_it(text, to_lang1, to_lang2):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(to_lang1, to_lang2),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    print(json_)
    return ''.join(json_['text'])


with open(f2, 'w') as f:
    f.write(translate_it(file, lang1, lang2))

