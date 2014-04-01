from sys import argv
from os.path import exists
#
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
#첫번째 입력한 파일 이름의 정보를 넣어줌.
indata = in_file.read()
#첫번째 입력한 파일의 정보를 읽어서 indata에 넣어줌.
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
#복사할 파일을 열어주는데 쓰기전용으로 만든다.
out_file.write(indata)
#복사할 파일을 열어서 쓰는데 그 내용은 위에 첫번째 연 파일의 내용임.
print "Alright, all done."

out_file.close()
# 복사한파일 닫기
in_file.close()
# 원본 파일 닫기