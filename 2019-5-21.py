# file = open('c:/Users/dell/desktop/file.txt','w')
# file.write('hello world!')
# what_he_does = ' plays'
# his_instrument = ' guitar'
# his_name = 'jarvis'
# artist_intro = his_name  +  what_he_does  +  his_instrument
# print(artist_intro)
# num = 1
# string = '1'
# num2 = int(string)
# print(num + num2)

# word = 'jidkldjgoi ksjdid '
# num = 12
# string = 'jarvis'
# total = string*(len(word)-num)
# print(total)
#
# a = 'my name is jarvis'
# print(a[5])
# print(a[0:9])
# print(a[6:])
# print(a[7:10])
# print(a[-11])


# phone = '158-6902-7164'
# hiding_phone = phone.replace(phone[:9],'*'*9)
# print(hiding_phone)


# print('{} a word she can get what she {} for.'.format('with','came'))
# print('{preposition} a word she can get what she {verb} for.'.format(preposition='with',verb='came'))
# print('{0} a word she can get what she {1} for.'.format('with','came'))

# city = input('write down your city\n')
# url = 'http://apistore.baidu.com/microservice/weather?citypinyin={}'.format(city)
# print(url)

# def F2C_conveter(C):
#     temprature = C*9/5 + 32
#     return str(temprature) + 'F'
#
# F2C = F2C_conveter(35)
# print(F2C)
#
# def weight_conveter(a):
#     b = a/1000
#     return str(b) + 'kgs'
# c = int(input('请输入克数\n'))
# print(weight_conveter(c))

# def trazip_area(a,b,c,):
#     return 1/2*(a+b)*c
# print(trazip_area(1,2,3))

#文本过滤器
def create_text(name,desc):
    desk_addr = "C:/Users/dell/Desktop/"
    full_addr = desk_addr + name + ".txt"
    file = open(full_addr,"w")
    file.write(desc)
    file.close
    print("done")

def text_filter(word,concerd_word = "lame",change_word = "awesome"):
    return word.replace(concerd_word,change_word)

def consered_text_filter(name,desc):
    filter_desc = text_filter(desc)
    create_text(name,filter_desc)
consered_text_filter("new","go,go,lame,lame")



