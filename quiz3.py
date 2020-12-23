'''
Make a program that make password for each sites

ex> https://naver.com
1. remove https:// => naver.com
2. remove from frist . => naver
3. in remaining string first 3(nav) + length of string(5) + number of e(1) + "!"

password : nav51!

'''

site = "https://naver.com"
word = site[8:site.find(".")]
password = word[:3] + str(len(word)) + str(word.count("e")) + "!"
print(f"site : {site} | password : {password}")

'''
solution
url = "https://naver.com"
my_str = url.replace("https://", "")
my_str = my_str[:mystr.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}'s password is {1}".format(url, password))

'''