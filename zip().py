#ZIP()-->
name=['Piyush','Udoy','Prity']
varsity=['DIU','Bottomly','Sristy']

zipped=list(zip(name,varsity))
print(zipped)

zipped=tuple(zip(name,varsity))
print(zipped)

zipped=dict(zip(name,varsity))
print(zipped)

zipped=set(zip(name,varsity))
print(zipped)

# UNZIP()-->
name1,varsity1=zip(*zipped)
print(name1),print(varsity1)

#--> how to search and replace a text in a file in python-->
search_word='Bercelona'
replace_word='Bayern Munich'

with open(r'text1.txt','r') as file:  #---> Read
    data=file.read()
    data=data.replace(search_word,replace_word)

with open(r'text1.txt','w') as file:  #-->Write
    file.write(data)

    #--> Successfuly Replaced
#--> Alternate way to replace a word-->
text="Manchester shall beat the Liverpool!"
se_word='Manchester'
re_word='Lancaster'
import re
text=re.sub(se_word,re_word,text)
print(text)