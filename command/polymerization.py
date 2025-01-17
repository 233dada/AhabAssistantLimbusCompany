from time import sleep

from command.get_position import get_pic_position
from command.mouse_activity import mouse_click
from my_log.my_log import my_log

def wait_to_click(pic_path):
    wait_time = 0.2
    position = None
    i = 0
    while True or i > 30:
        i = i + 1
        if position := get_pic_position(pic_path):
            break
        sleep(wait_time)
        if wait_time < 1:
            wait_time += 0.1
    mouse_click(position)
    if i > 30:
        my_log("error", f"等待位于{pic_path}的图片超时或未识别成功")
        return 0
