## python内置类型性能分析
- timeit模块
	- timeit模块可以用来测试一段python代码的执行速度
- class timeit.Time(stmt='pass',steup='pass',timer=<timer function>)
	- Timer是测量小段代码执行速度的类
	- stmt参数是要测试的代码语句（statment）
	- steup参数是运行代码时需要的设置
	- timer参数是一个定时器函数，与平台有关
- timeit.Timer.timeit(number=1000000)
	- Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。方法返回执行代码的平均耗时，一个float类型的秒数
