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
password = word[0:3] + str(len(word)) + str(word.count("e")) + "!"
print(f"password : {password}")