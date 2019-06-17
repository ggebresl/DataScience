# Regular expression
'''
Identifiers
1. \d - any number.
2. \D - anything but a number
3. \s - space
4. \S - anything but a space
5. \w - any Character
6. \W - anything but a Character
7.  . - any character, except for newline(\n)
8. \b = The whitespaces around data(word)
9. \. - a period

Modifiers

1. {1-3} were expecting 1-3
2. +  -> match one or more
3. *  -> match zero or more
4. ?  -> zero or one
5. $  -> match end of the string
6. ^  -> match beginning of the string
7. |  -> either or
8. [] -> range or 'variance'
   {x} -> expecting 'x' amount


White space Characters

1. \n -> New line
2. \s -> Space
3. \t -> tab space
4. \e -> escape
5. \f -> form feed
6. \r -> return


Don't forget
. + * ? [ ] $ ^ ( ) { } | \

Note :- we have escape them by \(back slash)

'''
#Example-1
'''
import re
ex_str = "John is 15 years old, and
Deniel is 27 years old"

ages = re.findall(r'\d{1,3}',ex_str)
names = re.findall(r'[A-Z][a-z]*',ex_str)
print(ages)
print(names)

ageDict ={}
i=0
for eachname in names:
    ageDict[eachname]=ages[i]
    i+=1
print(ageDict)
'''

#Example-2
import re

f = open('re_text.txt','r')
data = f.read()
#print(type(data))
paragraph = re.findall(r'<p>(.*?)</p>',data)
f.close()

f = open('re_output.txt','w')
f.write(str(paragraph))
f.close()
#print(paragraph)






