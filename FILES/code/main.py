import os
import shutil

d = input('What do you want to do? (rename, delete): ')
if d == 'delete':
    file = input('What do you want to delete? (folder, file): ')

    if file == 'file':
        path = input('Write the path to the file (write without quotes and other things): ')
        os.remove(path)
        print('The operation is completed')

    if file == 'folder':
        path1 = input('Write the path to the folder (write without quotes and other things): ')
        shutil.rmtree(path1)
        print('The operation is completed')

if d == 'rename':
    path2 = input('Write the path to the file or folder (write without quotes, etc.): ')
    path21 = input('Write the path to the file or folder with the new name (write without quotes, etc.): ')
    os.rename(path2, path21)
    print('The operation is completed')
