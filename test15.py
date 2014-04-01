# -*- coding: utf-8 -*-

# [B반][게임공학과][2009182022][류웅국]

from sys import argv

script, filename = argv
# 프롬프트창에서 파일 이름 매개변수값으로 받아옴
txt = open(filename)
# 파일 이름을 받아서 파일열기 정보를 txt에 넣어줌
print "Here's your file %r:" % filename
print txt.read()
# 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()