# encoding=utf-8
# file = open('data\Python_Introduction')
# readme_txt = file.read()
# # 要記得關檔
# file.close()
# 這樣可以不用關檔，在scope中可以用，出scope就會自動關掉
with open('data\Python_Introduction') as file1:
    readme_txt = file1.read().decode('UTF-8')


print type(readme_txt)
print readme_txt

# with open('data\p2_write', 'w') as file2:
#     file2.write(readme_txt)


with open('data\p2_write_utf-8', 'w') as file3:
    file3.write(readme_txt.encode('UTF-8'))
