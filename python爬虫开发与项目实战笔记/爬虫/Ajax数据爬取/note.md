- 什么是Ajax
    - Asynchronous JavaScript and XML，异步的JavaScript和XML
    - 基本原理：
        - 发送请求
            - JavaScript 对 Ajax 最底层的实现，实际上就是新建了 XMLHttpRequest 对象，
            然后调用 onreadystatechange 属性设置了监昕，然后调用 open()和 send()方法
            向某个链接(也就是服务器 )发送了请求
        - 解析内容
        - 渲染网页
        