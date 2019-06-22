### logging 模块的使用
- scrapy
  - settings中设置LOG_LEVEL=“WARNING”
  - settings中设置LOG_FILE="./a.log"  #设置日志保存的位置，设置会后终端不会显示日志内容
  - import logging,实例化logger的方式在任何文件中使用logger输出内容

- 普通项目中
  - import logging
  - logging.basicConfig(...) #设置日志输出的样式，格式
  - 实例化一个`logger=logging.getLogger(__name__)`
  - 在任何py文件中调用logger即可
