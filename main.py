

from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice,randint

#downloading file if it isnt already in the folder
if not isfile('words.txt'):
    print('Downloading words.txt...')
    url='https://github.com/dwyl/english-words/raw/master/words.txt'
    with open('words.txt', 'wb') as f:
        f.write(urlopen(url).read())

#open wordlist
words=open('words.txt','r').read().split("\n")
special_chars=['!', '?', '~', '$', '&', '%']


#generating the password
def create_password(num_words=1, num_numbers=4, num_special=3):
    pass_str=''

    for _ in range(num_words):
        pass_str+=choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str+=str(randint(0,9))
    for _ in range(num_special):
        pass_str+=choice(special_chars)

    return pass_str


def main():

    pass1 = input('Enter the password: ')
    strength,_=test(pass1)
    print ('\nPassword: %s' %pass1)
    print ('Strength: %0.5f' %strength)
    if strength<0.7:
        print ('Consider change your password or use the new and strong password that our Generator created for you')
        pass_str=create_password()
        strength,_=test(pass_str)
        print ('\nPassword: %s' %pass_str)
        print ('Strength: %0.5f' %strength)
    

    #SOS ta sxolia sthn main na meinoun alla na dokimasw kai me to input


if __name__=='__main__':
    main()
