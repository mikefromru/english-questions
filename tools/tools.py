from bs4 import BeautifulSoup
import requests
import requests, random, re
import os

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20191010T193218Z.1db2849f475fb04d.c597498fbdf1b4e06f3026999c6199d9295c09e5" 

def translate_me(text):

    params = {
        "key": KEY,     
        "text": text,
        "lang": 'en-ru' #Здесь мы указываем с какого языка на какой мы делаем переводим 
    }
    response = requests.get(URL ,params=params)
    return response.json()

def make_russian_name(text):
    json = translate_me(text) 
    return ''.join(json["text"])

#print(make_russian_name('hello world'))

def check_file(filename):
    filepath = 'questions/' + filename 
    if os.path.isfile(filepath):
        return 'True'
    else:
        return 'False'

#for x in os.listdir('questions'):
    #print(check_file(x), end = ' ')

def get_questions_from_file(filename):
    filepath = 'tools/questions/' + filename 
    if not os.path.isfile(filepath):
        print('File Not Found')
        raise SystemExit 

    f_list = []
    f = open('tools/questions/' + filename, 'r').readlines()
    for x in f:
        f_list.append(x.lstrip())

    new_f_list = list(filter(None, f_list))
    done_list = []
    for x in new_f_list:
        done_list.append(x.replace('\n', '').replace('?', ''))

    list_questions = []
    for x in done_list:
        j = x.split(' ')
        del j[0]
        list_questions.append(' '.join(j))

    return list_questions

#print(get_questions_from_file(filename))





#name = 'I, l.o...[ve)?!..'
def format_str(name):
    s = "?!,.[]{}()$#"
    new_name = ''

    for x in name:
        if not x in s:
            new_name += x
        else:
            pass
    return new_name


def get_questions_from_site():
    page_number = list(range(1, 11))
    LINKS = []
    while len(page_number) > 0:
        page = requests.get('http://iammike.pythonanywhere.com/?page={}'.format(page_number[0]))
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.find_all('div', class_='simple-card')
        for x in links:
            links_name = x.findAll('a')
            for j in links_name:
                LINKS.append('http://iammike.pythonanywhere.com' + j['href'])

        del page_number[0]
    
    
    while len(LINKS) > 0:
        level_link = requests.get(LINKS[0])
        filename = LINKS[0].split('/')[-1]

        f = open('questions/'+ filename, 'w')
        soup_ = BeautifulSoup(level_link.text, 'html.parser')

        questions = soup_.find_all('div', class_='modal-body')
        for x in questions:
            f.write(x.get_text())

        f.close() 
        del LINKS[0]
        print('written')
    
    print('DONE')

def get_buttons(name):


    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = requests.get(word_site)
    words = response.content.splitlines()
    new_words = []

    for x in words:
        if not "'" in x.decode():
            new_words.append(x.decode())
        else:
            pass

    tmp_btns = []
    btns = []
    name = format_str(name).split(' ')
    loop = True
    while loop:

        try:
            tmp_btns.append(name[0])
            tmp_btns += random.sample(new_words, 5)
            random.shuffle(tmp_btns)
            btns += tmp_btns

            name.remove(name[0])
            tmp_btns = []

        except IndexError:
            loop = False
    return ' '.join(btns)

def get_all(name):
    print(name.objects.all())

def new_get_all(name):
    for x in name.objects.all():
        return x.id, x.name


# get level names
def get_levels_from_site():
    f = open('title.txt', 'w')
    number = list(range(1, 11))
    while len(number) > 0:
        page = requests.get('http://iammike.pythonanywhere.com/?page={}'.format(number[0]))
        soup = BeautifulSoup(page.text, 'html.parser')
        pages = soup.find_all('div', class_='simple-card')
        for x in pages:
            f.write(x.get_text())

        del number[0]

# 
def get_data_from_file():
    f = open('title.txt', 'r').read().split('\n')
    list_levels = list(filter(None, f))
    return list_levels


