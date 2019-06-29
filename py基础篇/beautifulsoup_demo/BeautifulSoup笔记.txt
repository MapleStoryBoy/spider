# BeautifulSoup笔记：

## find_all的使用：
1. 在提取标签的时候，第一个参数是标签的名字。然后如果在提取标签的时候想要使用标签属性进行过滤，那么可以在这个方法中通过关键字参数的形式，将属性的名字以及对应的值传进去。或者是使用`attrs`属性，将所有的属性以及对应的值放在一个字典中传给`attrs`属性。
2. 有些时候，在提取标签的时候，不想提取那么多，那么可以使用`limit`参数。限制提取多少个。

## find与find_all的区别：
1. find：找到第一个满足条件的标签就返回。说白了，就是只会返回一个元素。
2. find_all:将所有满足条件的标签都返回。说白了，会返回很多标签（以列表的形式）。

## 使用find和find_all的过滤条件：
1. 关键字参数：将属性的名字作为关键字参数的名字，以及属性的值作为关键字参数的值进行过滤。
2. attrs参数：将属性条件放到一个字典中，传给attrs参数。

## 获取标签的属性：
1. 通过下标获取：通过标签的下标的方式。
    ```python
    href = a['href']
    ```
2. 通过attrs属性获取：示例代码：
    ```python
    href = a.attrs['href']
    ```

## string和strings、stripped_strings属性以及get_text方法：
1. string：获取某个标签下的非标签字符串。返回来的是个字符串。如果这个标签下有多行字符，那么就不能获取到了。
2. strings：获取某个标签下的子孙非标签字符串。返回来的是个生成器。
2. stripped_strings：获取某个标签下的子孙非标签字符串，会去掉空白字符。返回来的是个生成器。
4. get_text：获取某个标签下的子孙非标签字符串。不是以列表的形式返回，是以普通字符串返回。


## CSS选择器：
1. 根据标签的名字选择，示例代码如下：
    ```css
    p{
        background-color: pink;
    }
    ```
2. 根据类名选择，那么要在类的前面加一个点。示例代码如下：
    ```css
    .line{
        background-color: pink;
    }
    ```
3. 根据id名字选择，那么要在id的前面加一个#号。示例代码如下：
    ```css
    #box{
        background-color: pink;
    }
    ```
4. 查找子孙元素。那么要在子孙元素中间有一个空格。示例代码如下：
    ```css
    #box p{
        background-color: pink;
    }
    ```
5. 查找直接子元素。那么要在父子元素中间有一个>。示例代码如下：
    ```css
    #box > p{
        background-color: pink;
    }
    ```
6. 根据属性的名字进行查找。那么应该先写标签名字，然后再在中括号中写属性的值。示例代码如下：
    ```css
    input[name='username']{
        background-color: pink;
    }
    ```
7. 在根据类名或者id进行查找的时候，如果还要根据标签名进行过滤。那么可以在类的前面或者id的前面加上标签名字。示例代码如下：
    ```css
    div#line{
        background-color: pink;
    }
    div.line{
        background-color: pink;
    }
    ```

## BeautifulSop中使用css选择器：
在`BeautifulSoup`中，要使用css选择器，那么应该使用`soup.select()`方法。应该传递一个css选择器的字符串给select方法。


## 常见的四种对象：
1. Tag：BeautifulSoup中所有的标签都是Tag类型，并且BeautifulSoup的对象其实本质上也是一个Tag类型。所以其实一些方法比如find、find_all并不是BeautifulSoup的，而是Tag的。
2. NavigableString：继承自python中的str，用起来就跟使用python的str是一样的。
3. BeautifulSoup：继承自Tag。用来生成BeaufifulSoup树的。对于一些查找方法，比如find、select这些，其实还是Tag的。
4. Comment：这个也没什么好说，就是继承自NavigableString。

## contents和children：
返回某个标签下的直接子元素，其中也包括字符串。他们两的区别是：contents返回来的是一个列表，children返回的是一个迭代器。
