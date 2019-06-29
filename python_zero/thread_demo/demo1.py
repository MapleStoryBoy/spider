
import threading
import time

def coding():
	for x in range(3):
		print('正在写代码%s' % x)
		time.sleep(1)

def drawing():
	for i in range(3):
		print('正在画图%s' % i)
		time.sleep(1)

def main():
	coding()
	drawing()

if __name__ == "__main__":
	main()









