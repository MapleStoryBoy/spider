# coding=utf-8
import logging

#设置日志的输出样式
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s [%(filename)s:%(lineno)d] '
                           ':  %(message)s'
                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]',
                    )

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is a info log")
    logger.info("this is a info log 1")