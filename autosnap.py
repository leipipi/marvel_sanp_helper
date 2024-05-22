from main_function import find_and_click_continuous
from main_function import find_and_click
from main_function import gap
from main_function import find
import time
import pyautogui

def autosnap():
    time.sleep(3)
    if find_and_click_continuous('SNAP', 'snap-start2.png', threshold=0.6, duration=10):
        gap(20)
    else:
        find_and_click_continuous('SNAP', 'snap-x.png', threshold=0.7, duration=1)
        gap(2)
        find_and_click_continuous('SNAP', 'snap-restart.png', threshold=0.7, duration=3)
        gap(2)
        find_and_click_continuous('SNAP', 'snap-start.png', threshold=0.6, duration=3)
        gap(20)
    for i in range(5):
        pyautogui.click() # 防止遇到新卡
        #循环7次完赛，6次撤退
        find_and_click_continuous('SNAP', 'snap-endturn.png', threshold=0.6, duration=16)
        gap(17)
    find_and_click_continuous('SNAP', 'snap-escape.png', threshold=0.6, duration=4)
    gap(2)
    find_and_click_continuous('SNAP', 'snap-escapeconfirm.png', threshold=0.5, duration=4)
    gap(4)
    find_and_click_continuous('SNAP', 'snap-award.png', threshold=0.60, duration=18,x_offset=10)
    gap(1)
    find_and_click_continuous('SNAP', 'snap-award.png', threshold=0.60, duration=3, x_offset=10)
    gap(1)
    find_and_click_continuous('SNAP', 'snap-next.png', threshold=0.6, duration=8)
    gap(1)
    find_and_click_continuous('SNAP', 'snap-next.png', threshold=0.6, duration=1)
    autosnap()

def escape():
    find_and_click_continuous('SNAP', 'snap-escape.png', threshold=0.6, duration=4)
    gap(1)
    find_and_click_continuous('SNAP', 'snap-escapeconfirm.png', threshold=0.5, duration=4)
    gap(1)

def autoget_award():
    time.sleep(1)
    pyautogui.click(860, 600)
    #pyautogui.click(1080, 700)
    #两列的值分别为左(860, 600)和右(1080, 700)
    time.sleep(1)
    find_and_click_continuous('SNAP', 'snap-get.png', threshold=0.6, duration=10)
    gap(1)
    pyautogui.scroll(240)
    autoget_award()

def autoconquer():
        time.sleep(3)
        pyautogui.click(764+1920, 139)#点进征服模式
        gap(3)
        #修改拖动次数
        enterconquer(dragcount=2)
        gap(17)
        while True:
            find_and_click_continuous('SNAP', 'conquer-confirm.png', threshold=0.63, duration=1)
            gap(1)
            #控制6回合自动撤退
            #if find('SNAP', 'snap-6.png', threshold=0.5, duration=1):
                #escape()
            pyautogui.click(1689+1920, 967)
             #控制是否自动snap
            if find('SNAP', '1.png', threshold=0.69, duration=1):
                autosnap_and_image()
                gap(14)
            gap(4)
            if find('SNAP', 'snap-finish.png', threshold=0.6, duration=2):
                break
        gap(1)
        find_and_click_continuous('SNAP', 'snap-next.png', threshold=0.6, duration=5)
        if find('SNAP', 'snap-win.png', threshold=0.6, duration=5):
            gap(2)
            pyautogui.click(1689+1920, 967)
            gap(1)
            pyautogui.click(1689+1920, 967)
            gap(8)
            find_and_click_continuous('SNAP', 'snap-next2.png', threshold=0.6, duration=5)
            gap(1)
            find_and_click_continuous('SNAP', 'snap-get.png', threshold=0.58, duration=5)
            gap(1)
            pyautogui.click(1689+1920, 967)
            gap(1)
            find_and_click_continuous('SNAP', 'snap-exit.png', threshold=0.65, duration=3)
            autoconquer()
        if find('SNAP', 'snap-lose.png', threshold=0.6, duration=5):
            gap(2)
            pyautogui.click(1689+1920, 967)
            gap(3)
            pyautogui.click(1689+1920, 967)
            gap(1)
            find_and_click_continuous('SNAP', 'snap-exit.png', threshold=0.65, duration=3)
            autoconquer()



def autosnap_and_image():
    # 自动snap与发表情
    pyautogui.click(1483+1920, 695)
    gap(1)
    pyautogui.click(146+1920, 146)
    gap(1)
    pyautogui.click(195+1920, 396)
    gap(1)

def enterconquer(dragcount):
    # 水平拖动鼠标200像素，
    for i in range(dragcount):
        gap(1)
        pyautogui.drag(200, duration=0.5)
    gap(1)
    #更改票的类型
    find_and_click_continuous('SNAP', 'conquer-enter.png', threshold=0.6, duration=2)
    find_and_click_continuous('SNAP', 'snap-sliver.png', threshold=0.6, duration=2)
    gap(10)
    find_and_click_continuous('SNAP', 'conquer-start.png', threshold=0.6, duration=7)
    gap(1)
    find_and_click_continuous('SNAP', 'conquer-confirm.png', threshold=0.63, duration=3)
    gap(1)



def main():
    #autoget_award()
    autosnap()
    #autoconquer()
    pass

if __name__ == "__main__":
    main()
