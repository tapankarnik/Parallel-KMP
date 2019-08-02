import textwrap
with open('string.txt', 'r') as myfile:
	txt=myfile.read().replace('\n', '')
length = len(txt)
percorenum = length / 4
txt = textwrap.wrap(txt,percorenum)
# print(txt)
print(txt[1])
x <= 