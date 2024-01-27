import logging
import os.path
import time
from logging.handlers import RotatingFileHandler



from conf import setting

log_path = setting.FILE_PATH['LOG']
print(log_path)
if not os.path.exists(log_path):
    os.mkdir(log_path)

logfile_name = log_path+'/test.{}.log'.format(time.strftime("%Y%m%d"))
print(logfile_name)

class RecordLog:
    """封装日志"""
    def output_logging(self):
        """获取logger对象"""
        logger = logging.getLogger(__name__)
        #防止打印重复的log日志
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL)
            log_format = logging.Formatter(
                '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d -[%(module)s:%(funcName)s] - %(message)s')
            # 日志输出到指定文件，滚动备份日志
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880,
                                backupCount=7,
                                encoding='utf-8')  # maxBytes:控制单个日志文件的大小，单位是字节,backupCount:用于控制日志文件的数量
            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(log_format)

            #再将相应的handler添加到logger对象中去
            logger.addHandler(fh)

        return logger

apilog = RecordLog()
logs = apilog.output_logging()

