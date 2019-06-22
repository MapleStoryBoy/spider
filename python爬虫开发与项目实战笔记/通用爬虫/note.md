## 处理cookies、session请求
- requests提供一个叫做session类，来实现客户端和服务端的会话保持
- 使用方法：
	- 1，实例化一个session对象
	- 2，让session发送get或者post请求
		- session = requests.session()
		- response = session.get(url,headers)
	