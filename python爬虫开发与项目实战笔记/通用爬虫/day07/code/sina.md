#### 数据的例子
```json
{
  "content_url": "https://weibo.cn/comment/Fvwy2F35h",
  "poster_name": "北北北漂儿",
  "poster_url": "https://weibo.cn/210120796",
  "post_date": "2017-11-16 17:58",
  "content": "魏公村附近最新的楼盘，悦园07年房子，顶层 带超大露台业主已经框起来，可以做两居室，面积接近100平，朝南卧室待阳台，价格8500，已经远低于小区这个面积的同等房子，小区独门独院，24小时门卫把守，还有个小花园，周边北京外国语大学、中央民族大学、北京理工大学、舞蹈学院适合长期居住。",
  "current_forword_times": 0,
  "current_comment_num": 0,
  "if_forward": false,
  "origin_poster_name": "嘀滴哒嗒小丸子",
  "origin_poster_url": "https://weibo.cn/u/2967240684",
  "origin_forword_times": 0,
  "origin_comment_num": 0,
  "at_info_list": [
    {
      "at_name": "@北京租房子",
      "at_href": "https://weibo.cn/n/%E5%8C%97%E4%BA%AC%E7%A7%9F%E6%88%BF%E5%AD%90"
    },
    {
      "at_name": "@新浪北京租房",
      "at_href": "https://weibo.cn/n/%E6%96%B0%E6%B5%AA%E5%8C%97%E4%BA%AC%E7%A7%9F%E6%88%BF"
    },
    {
      "at_name": "@海淀租房",
      "at_href": "https://weibo.cn/n/%E6%B5%B7%E6%B7%80%E7%A7%9F%E6%88%BF"
    }
  ],
  "tag_list": [
    {
      "tag_name": "#泊寓吃喝玩乐pa#",
      "tag_href": "http://weibo.cn/pages/100808topic?extparam=%E6%B3%8A%E5%AF%93%E5%90%83%E5%96%9D%E7%8E%A9%E4%B9%90pa&from=feed"
    },
    {
      "tag_name": "#北京租房#",
      "tag_href": "http://weibo.cn/pages/100808topic?extparam=%E5%8C%97%E4%BA%AC%E7%A7%9F%E6%88%BF&from=feed"
    }
  ],
  "location": "北京·清上园",
  "pic_list": [
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8ep9zjwj20m80gomy2&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epak6pj20m80go0tt&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epamxgj20m80go0te&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epezaaj20m80go0un&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epar6aj20m80go3zg&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epayxjj20m80godgz&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epdtppj20m80goq3n&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8epf3fmj20m80gowff&rl=1",
    "https://weibo.cn/mblog/oripic?id=Fvwy2F35h&u=ad69225fly1fll8exsrjkj20xc0nm0ug&rl=1"
  ],
  "comment_list":[
    {
      "comment_poster_name":"hello,world",
      "comment_to_name":"hello,world1",
      "comment_to_url":"https://weibo.cn/220110786",
      "comment_poster_url":"https://weibo.cn/210120796",
      "comment_date":"2017-11-17 14:30",
      "comment_content":"XXXXXXX"
    },
    {
      "comment_poster_name":"hello,world2",
      "comment_to_name":"hello,world1",
      "comment_to_url":"https://weibo.cn/220110786",
      "comment_poster_url":"https://weibo.cn/210120796",
      "comment_date":"2017-11-17 14:30",
      "comment_content":"XXXXXXX"
    }

  ]
}
```

#### 字段的含义
```json
{
  "content_url": "帖子的地址",
  "poster_name": "发帖人的姓名",
  "poster_url": "发帖人的地址",
  "post_date": "发布日期，后学会调整为具体的时间",
  "content": "内容，后续会调整为字符串",
  "current_forword_times": "转发数量",
  "current_comment_num": "评论数量",
  "current_like_num": "点赞数量",
  "if_forward": "是否为转发",
  "origin_poster_name": "原始发帖人的名称",
  "origin_poster_url": "原始发帖人的url地址",
  "origin_forword_times": "原贴转发次数",
  "origin_comment_num": "原贴评论数",
  "at_info_list": "微博@的内容",
  "pic_list": "贴图的地址",
  "comment_list":"评论的内容",
  "tag_list": "#xxx#这种内容"
}
```
