import os
from flask import abort
from polarishub_flask.server.parser import printv
import sqlite3

def has_password(cwd, filename):
    directory = get_directory(cwd)
    directory = ('\啦啦啦啦') # 这行要删掉
    conn = sqlite3.connect(os.path.join(os.getcwd(), 'server', 'passwords.db'))
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM passwords WHERE directory = "{directory}" AND filename = "{filename}";')
    if len(list(cursor)) == 0:
        return False
    else:
        return True

def add_password(cwd, filename, password):
    cwd = cwd.replace("\\\\", "\\") # 这一行是依赖操作系统的
    directory = get_directory(cwd)
    conn = sqlite3.connect(os.path.join(os.getcwd(), 'server', 'passwords.db'))
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO passwords (directory, filename, password) VALUES ("{directory}", "{filename}", "{password}");')
    conn.commit()
    conn.close()

def delete_password(cwd, filename):
    cwd = cwd.replace("\\\\", "\\") # 这一行是依赖操作系统的
    conn = sqlite3.connect(os.path.join(os.getcwd(), 'server', 'passwords.db'))
    directory = get_directory(cwd)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM passwords WHERE directory = "{directory}" AND filename = "{filename}";')
    conn.commit()
    conn.close()

def check_password():
    '''验证是否为双层密码，如果是，否决
    '''
    pass

def verify_password(cwd, filename, password):
    '''验证密码是否正确
    '''
    cwd = cwd.replace("\\\\", "\\") # 这一行是依赖操作系统的
    directory = get_directory(cwd)
    conn = sqlite3.connect(os.path.join(os.getcwd(), 'server', 'passwords.db'))
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM passwords WHERE directory = "{directory}" AND filename = "{filename}" AND password = "{password}";')
    if len(list(cursor)) == 0:
        return False
    else:
        return True

def get_directory(cwd):
    '''获取相对路径
    '''
    main = os.path.join(os.getcwd(), 'files')
    directory = cwd[len(main):]
    if directory == '':
        return '/'
    else: 
        return directory

def refresh_passwords():
    '''更新数据库，剔除已经删除的文件的密码
    '''
    pass
