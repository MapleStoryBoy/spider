1.HTML
	图像标记属性
	<img>称为图像标记
	使用方法：<img src="路径/文件名.图片格式">
	属性：
	width：用来指定图片的宽度，单位为px、em、cm、mm。
	src：用来指定我们要加载的图片的路径、图片的名称以及图片格式
	height：用来指定图片的高度，单位为px、em、cm、mm。
	border：用来指定图片的边框宽度，单位为px、em、cm、mm。
	alt：有三个作用：
		1、当网页上的图片被加载完成后，鼠标移动到上面去，会显示这个图片指定的属性文字
		2、如果图像没有下载或者加载失败，会用文字来替代图像显示
		3、搜索引擎可以通过这个属性的文字来抓取图片

	超链接的使用：
		链接的引用使用的是<a>标记
		<a>标记的基本语法：
			<a href="链接地址" target="打开方式" name="页面锚点名称">链接文字或者图片</a>
		<a>的主要属性：
			href：链接的地址，可以是一个网页，也可以是一个视频、图片、音乐等
			target：用来定义超链接的打开方式。当属性值为_blank时，作用是在一个新的窗口中打开链接；
			当属性值为_self时，作用是在当前窗口中打开链接；当属性值为_parent时，作用是在父窗口中
			打开页面；当属性值为_top时，在顶层窗口中打开文件。
			name：用来指定页面的锚点名称


	表格：
		基本结构：<table>,<caption>,<tr>,<td>和<th>等标记。属性见图片


2、CSS
	指层叠样式表（Cascading Style Sheets），用来定义如何显示HTML元素，一般和HTML配合使用。目的是为
	了解决内容与表现分离的问题，即使同一个HTML文档也能表现出外观多样化。一般在HTML中使用CSS有三种方法：
		内联样式表：CSS代码直接写在现有的HTML标记中，直接使用style属性改变样式。
			例如：<body style="background-color: green; margin:0;padding: 0;"></body>
		嵌入式样式表：CSS样式代码写在<style type="text/css"></style>标记之间。一般情况下嵌入式CSS
		样式写在<head></head>之间。
		外部样式表：CSS代码写在一个单独的外部文件中，这样的CSS样式以".css"为扩展名，在<head>内（不是在
		<style>标记内）使用<link>标记将CSS样式文件链接到HTML文件中。
			例如：<link rel="StyleSheet" type="text/css" href="style.css">
    
    CSS规则由两个主要部分构成：选择器，以及一条或多条声明。
    
3、JavaScript
	轻量级的脚本语言。严格区分大小写，会忽略关键字、变量名、数字、函数名或其它各种元素之间的空格、制表符或换行符
	这个需要时间学习。。。。。。稍等


















