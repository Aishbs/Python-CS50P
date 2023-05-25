# Input from user
file = input('File name: ').lower().strip(' ')
#Spliting string into name and extension
name, dot, ext = file.rpartition('.')

match ext:
    case 'jpeg' | 'jpg':
        print('image/jpeg')
    case 'gif' | 'png':
        print('image/' + ext)
    case 'pdf' | 'zip':
        print('application/' + ext)
    case 'txt':
        print('text/' + name)
    case '':
        print('application/octet-stream')
    case _:
        print('application/octet-stream')