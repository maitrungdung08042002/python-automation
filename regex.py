import  re
regex1 = re.compile(r'anh (.*?) dep')
chuoi ='anh mtd dep trai'
kq = regex1.search(chuoi)
name = kq.group(1)
print(name)

#demo 2


ndung='''nhat ky cua nang
hom nay la ngay dep troi, mk gap anh dung rat la dep trai
mk fall in love with him rui
'''

regex1=re.compile(r'anh(.*?)rat');
kq=regex1.search(ndung)
print(kq.group(1))


#demo 3

import re
ndung='''nhat ky cua nang
hom nay la ngay dep troi, mk gap anh dung rat la dep trai
mk fall in love with him rui
sau do cuoi ngay mk lai gap duoc anh minh rat dep trai nua
'''

regex1=re.compile(r'anh(.*?)rat');
kq=regex1.findall(ndung)
print(kq) #=> 1 list danh sach thoa man