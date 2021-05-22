import sys
import time


if __name__ == '__main__':
    sys.stdout = 'hello world'
    print('hello world')
    time.sleep(600)
    print('bey')
    sys.exit(0)
