import os
import cv2
import numpy as np
import mss
import pygetwindow as gw
import pyautogui
import time


def find_and_click_continuous(window_name, filename, threshold=0.7, duration=10, x_offset=0, y_offset=0):
    # (窗口名称，图片文件全名，相似度阈值，检测时间，x坐标偏移，y坐标偏移)
    start_time = time.time()  # 记录开始时间
    template_image_path = os.path.join('image', filename)

    if not os.path.exists(template_image_path):
        print("文件不存在:", template_image_path)
        return False

    template = cv2.imread(template_image_path)
    if template is None:
        print("无法加载模板图像")
        return False

    window_title = window_name  # 根据需要更改窗口标题
    window = gw.getWindowsWithTitle(window_title)[0]
    if not window:
        print("未找到", window_title)
        return False

    while time.time() - start_time < duration:  # 持续执行直到达到指定时间
        with mss.mss() as sct:
            monitor = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}
            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if loc[0].size > 0:
            pt = loc[1][0], loc[0][0]
            screen_x = window.left + pt[0] + template.shape[1] // 2
            screen_y = window.top + pt[1] + template.shape[0] // 2
            pyautogui.moveTo(screen_x + x_offset, screen_y + y_offset)
            pyautogui.click()
            print("找到", filename)
            return True  # 找到匹配后退出函数
    print(duration, "秒内未找到", filename)  # 给定时间内未找到匹配
    return False


def find(window_name, filename, threshold=0.7, duration=10):
    # (窗口名称，图片文件全名，相似度阈值，检测时间，x坐标偏移，y坐标偏移)
    start_time = time.time()  # 记录开始时间
    template_image_path = os.path.join('image', filename)

    if not os.path.exists(template_image_path):
        print("文件不存在:", template_image_path)
        return False

    template = cv2.imread(template_image_path)
    if template is None:
        print("无法加载模板图像")
        return False

    window_title = window_name  # 根据需要更改窗口标题
    window = gw.getWindowsWithTitle(window_title)[0]
    if not window:
        print("未找到", window_title)
        return False

    while time.time() - start_time < duration:  # 持续执行直到达到指定时间
        with mss.mss() as sct:
            monitor = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}
            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if loc[0].size > 0:
            print("找到", filename)
            return True  # 找到匹配后退出函数
    print(duration, "秒内未找到", filename)  # 给定时间内未找到匹配
    return False


def gap(seconds):
    pyautogui.moveTo(960 + 1920, 540)
    time.sleep(seconds)


def print_mouse_position(interval=0.3):
    """
    定期打印当前鼠标位置。
    :param interval: 打印间隔时间（秒）。
    """
    try:
        while True:
            x, y = pyautogui.position()
            print(f"鼠标位置：({x}, {y})")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n程序已停止")


def find_and_click(filename, x_offset=0, y_offset=0, duration=5):
    # 构建图像文件的完整路径
    image_path = os.path.join('image', filename)

    start_time = time.time()

    while time.time() - start_time < duration:
        image = pyautogui.locateOnScreen(image_path)
        if image:
            center_x, center_y = pyautogui.center(image)
            click_x = center_x + x_offset
            click_y = center_y + y_offset
            pyautogui.click(click_x, click_y)
            return True
        time.sleep(0.1)

    print(f"{duration}秒内未找到图像")
    return False


def main():
    print_mouse_position()
    pass


if __name__ == "__main__":
    main()
