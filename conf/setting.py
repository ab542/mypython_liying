import os
import sys
import logging

DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH)
print(DIR_PATH) #当前目录

#log日志的输出级别
LOG_LEVEL = logging.DEBUG #日志输入到文件的级别
STREAM_LOG_LEVEL = logging.DEBUG #输出日志到控制台

#文件路径
FILE_PATH = {
    'extract' : os.path.join(DIR_PATH,'extract.yaml').replace('\\','/'),
    'conf' : os.path.join(DIR_PATH,'conf','config.ini').replace('\\','/'),
    'LOG' : os.path.join(DIR_PATH,'log').replace('\\','/')
}
print(FILE_PATH['extract'])
print(FILE_PATH['LOG'])