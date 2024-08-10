import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        return False


def check():
    if not is_admin():
        print('This script is not running with administrator privileges.')
        exit(0)


if __name__ == '__main__':
    check()
