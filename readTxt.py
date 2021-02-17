# -*- coding: utf-8 -*-
import re
import os
import traceback
import logging.handlers
import datetime

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)
name_pattern = r"^(第.*章) (.*)"


def read_txt(txt_name):
    count = 0
    n = 0
    txt_node_no = ""
    txt_node_name = ""
    with open(txt_name, "r+", encoding="utf-8") as txt_input:
        for txt_line in txt_input.readlines():
            txt_line_strip = txt_line.strip()
            match = re.match(name_pattern, txt_line_strip)

            with open() as txt:
                if match:
                    txt_node_no = match.group(1)
                    txt_node_name = match.group(2)
                    print(txt_node_no)
                    print(txt_node_name)
                    count += 1
                    print(count)
                else:
                    try:
                        # print(txt_line_strip)
                        logger.info("1")
                    except UnicodeEncodeError as e:
                        logger.error(traceback.format_exc())
                        # logger.error(txt_line_strip)

    print(count)


if __name__ == '__main__':
    read_txt(r"D:\src\tmp\txt\遮天u.txt")
