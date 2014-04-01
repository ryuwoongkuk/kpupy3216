from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#타겟에 파일정보 넣어줌
print "Truncating the file.  Goodbye!"
target.truncate()
#텍스트에 입력된 문자모두 삭제
print "Now I'm going to ask you for three lines."
#라인숫자에 맞춰서 입력
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#라인1,2,3에 입력된 문자를 메모장에 넣어주기
print "And finally, we close it."
target.close()
#파일 닫기