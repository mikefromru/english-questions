import re
kak = 'When parents When youWhy begin dating. After you goWhat a while. Only when isWhat the atEnglish is youWould seriousx Why Why'
back = 'Is your stress With caused Explain relationships With other Do people At work At school At home. With best Do friends With partners Can you think of some examples'

words = ['Would', 'With', 'What', 'Did', 'Do', 'When', 'Where', 'Who', 'Have',
        'Why', 'Will', 'Were', 'Was', 'Are', 'Am', 'Does', 'Has', 'How', 'Is', 'Shy', 'Or', 'Can', 'Could',
        'There', 'Whom', 'If', 'So', 'Describe', 'Explain', 'For', "What's", 'Tell']


var = 'Why parents goWhat do they listen toWhy How isWhen How When Why'

def foo(a):
    return re.sub(r'(?<=[a-z])(?=%s)' % '|'.join(words), '. ', a)

def edit_string(a):
    first = a.split()[0]
    a = a.split()[1:]
    for counter, x in enumerate(a):
        if x in words:
            t = counter -1
            if not a[t].endswith('.'):
                a[t] = a[t] + '.'
            else:
                pass
        else:
            pass
    a.insert(0, first)
    return ' '.join(a)
