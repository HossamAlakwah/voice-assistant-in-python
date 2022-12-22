from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time



ser = Service("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
class play():
    def __init__(self):
        self.driver = webdriver.Chrome(options=option, service=ser)

    def play_video(self,query):
        self.query=query
        #bonus one
        self.driver.maximize_window()
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        video = self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()
# #
# img1=pyautogui.locateCenterOnScreen("play.png", confidence=0.99, region=(1208, 0, 1585, 1079))
# img2=pyautogui.locateCenterOnScreen("bannerad.png", confidence=0.99, region=(931, 0, 1100, 1079))
# img3=pyautogui.locateCenterOnScreen("black banner.png", confidence=0.99,region=(931, 0, 1100, 1079))
# def bot():
#     def findAndClick():
#         while True:
#             videoAdCords = pyautogui.locateCenterOnScreen("play.png", confidence=0.99, region=(1208, 0, 1585, 1079))
#             bannerCords = pyautogui.locateCenterOnScreen("bannerad.png", confidence=0.99, region=(931, 0, 1100, 1079))
#             blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png", confidence=0.99,
#                                                               region=(931, 0, 1100, 1079))
#             print(videoAdCords)
#             print(bannerCords)
#             print(blackBannerCords)
#
#             if videoAdCords or bannerCords or blackBannerCords is not None:
#                 break
#
#         if videoAdCords is not None:
#             pyautogui.click(videoAdCords)
#         elif bannerCords is not None:
#             pyautogui.click(bannerCords)
#         elif blackBannerCords is not None:
#             pyautogui.click(blackBannerCords)
#
#         time.sleep(2)
#         findAndClick()
#
#     findAndClick()

# test=bot().findAndClick()


"""for i in range (20):
    print(pyautogui.position())
    time.sleep(1)"""
#Point(x=1047, y=645)

