'''
'write only code'
top article:
https://habr.com/ru/articles/349860/
'''


import re
def check_email(addr):
    res = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', addr)
    print(res)

def find_start_abv(name):
    res = re.match(r'abv', name)
    print(res)

def find_abv(name):
    res = re.search(r'abv', name)
    print(res)

def find_all_abv(name):
    res = re.findall(r'abv', name)
    print(res)

def split_abv(name):
    res = re.split(r'abv', name, maxsplit=1)
    print(res)

def split_any(text):
    res = re.split(r'[;,\s]', text)
    print(res)

def sub_abv(name):
    res = re.sub(r'abv', '***', name)
    print(res)

def compile_pattern():
    pattern = re.compile('AV')
    res = pattern.findall('AV Analytics Vidhya AV')
    print(res)

def get_first_2_symbol_of_all_words(text):
    res = re.findall(r'\b\w.', text)
    return res

def get_domains(text):
    res = re.findall(r'@\w+.\w+', text)
    return res

def get_top_level_domain(text):
    res = re.findall(r'@\w+.(\w+)', text)
    return res

def get_date(text):
    res = re.findall(r'\d{2}-\d{2}-\d{4}', text)
    return res

def get_date_year(text):
    res = re.findall(r'\d{2}-\d{2}-(\d{4})', text)
    return res

def get_words(text):
    res = re.findall(r'\w+', text)
    return res

def get_words_with_firsr_a(text):
    res = re.findall(r'\b[aA]\w+', text)
    return res

if __name__ == '__main__':
    check_email('vrevt@gmail.com')

    find_start_abv('abv_cava_abv_xxx_q')
    find_abv('cava_abv_xxx_q_abvdwwlrnw')
    find_all_abv('cava_abv_xxx_q_abvdwwlrnw')

    split_abv('cava_abv_xxx_q_abvdwwlrnw')
    split_any('asdf fjdk;afed,fjek,asdf,foo')

    sub_abv('cava_abv_xxx_q_abvdwwlrnw')

    compile_pattern()

    print(get_first_2_symbol_of_all_words('AV is largest Analytics community of India'))

    text = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
    print(get_domains(text))
    print(get_top_level_domain(text))

    text_with_date = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
    print(get_date(text_with_date))
    print(get_date_year(text_with_date))

    text = 'AV is largest Analytics community of India'
    print(get_words(text))
    print(get_words_with_firsr_a(text))