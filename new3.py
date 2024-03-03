from translate import Translator
#with open("age/text.txt", 'r', encoding='utf-8') as my:
try:
    a = input("enter what u want to translate : ")
    trans = Translator(to_lang="Ja")
    translation = trans.translate(a)
    #    with open("newtext.txt", 'w',encoding='utf-8') as new:
           # new.write(translation)
    print(translation)
except Exception as e:
        print(f'the error is:  {e}')
