import pypandoc


file= open('definition25-07.txt','r')

for line in file:
    if line[0]=='[':
        print(line[1:len(line)-1].replace("'",'"').)
        