#encoding: utf-8

import threading


def write_file(fp,value):
    fp.write(str(value))


def main():
    fp = open('test.txt','a')
    for x in range(10):
        write_file(fp,x)

if __name__ == '__main__':
    main()