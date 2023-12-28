from selenium import webdriver
import pyautogui as auto
import time
import keyboard

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://elgoog.im/dinosaur-game/')
time.sleep(3)

auto.click(984, 23, button='left')
time.sleep(2)
auto.press('space')
time.sleep(3)



# (left=49, top=541, width=119, height=130)


while True:  
    # print(auto.position())
    # time.sleep(3)
    for i in range(180, 500, 30):
        if auto.pixelMatchesColor(i, 540, (83, 83, 83)) or auto.pixelMatchesColor(i, 620, (83, 83, 83)):
            # print('Cactus detected at:', i)
            auto.press('space')  
            # break
            
    if keyboard.is_pressed('s'):
         driver.quit()
         break
    

    
# 404, 543

