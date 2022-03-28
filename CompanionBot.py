from PIL.ImageOps import grayscale
import pyautogui
import time
import random
import numpy as np


def click_followers():
    def Grade():
        pyautogui.moveTo(x=1128, y=473) # Clicking Drop down
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=1128, y=473)
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1017, y=606)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=1017, y=606)
        time.sleep(np.random.uniform(0.3,1))

        # Point(x=1128, y=473) # clikcking drop down
        # Point(x=1021, y=542) # grade 4
        # Point(x=1018, y=558) # grade 5
        # Point(x=1026, y=577) # grade 6
        # Point(x=1030, y=593) # grade 7
        # Point(x=1017, y=606) # grade 8
        # Point(x=1018, y=622) # grade 9
        # Point(x=1022, y=638) #grade 10

    def Ashara():
        pyautogui.moveTo(x=216, y=649)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=216, y=649) # Ashara
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))
    
    def Khem():
        pyautogui.moveTo(x=221, y=726)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=221, y=726) # Khem
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))

    def Andronikos():
        pyautogui.moveTo(x=216, y=809)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=216, y=809) # Andronikos
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))

    def Talos():
        pyautogui.moveTo(x=216, y=885)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=216, y=885) # Talos
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))

    def Scroll():
        pyautogui.moveTo(x=455, y=927)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=455, y=927)
        time.sleep(np.random.uniform(0.3,1))

    def Xalek():
        pyautogui.moveTo(x=217, y=835)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=217, y=835) # Xalec
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))

    def Robot():
        pyautogui.moveTo(x=218, y=911)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=218, y=911) # Xalec
        time.sleep(np.random.uniform(0.3,1))

        Grade()

        pyautogui.moveTo(x=974, y=539)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=974, y=539) # Top Mission
        time.sleep(np.random.uniform(0.3,1))

        pyautogui.moveTo(x=1132, y=993)
        pyautogui.doubleClick(x=1132, y=993) # Send
        time.sleep(np.random.uniform(0.3,1))
    
    def TopScroll():
        pyautogui.moveTo(x=453, y=605)
        time.sleep(np.random.uniform(0.3,1))
        pyautogui.click(x=453, y=605)
        time.sleep(np.random.uniform(0.3,1))


    Ashara()
    Khem()
    Andronikos()
    Talos()
    Scroll()
    Xalek()
    Robot()
    TopScroll()
    


def click_accept(): 
    x = 0
    while x < 6:
        accept = pyautogui.locateOnScreen(r'C:\Users\shane\Documents\Python Proects\SWTOR\accept.png', grayscale=True, confidence=0.8, region=(0,0, 1280, 1440))
        if accept != None:
            print("Found an Accept!")
            time.sleep(np.random.uniform(0.3,1))
            pyautogui.click(accept) # Clicking accept on rewards
            time.sleep(np.random.uniform(0.3,1))
            pyautogui.click(x=823, y=966) # Clicking back on missions
            time.sleep(np.random.uniform(0.3,1))
            
            x+=1
        else:
            print("Waiting for an Accept..")
            time.sleep(5)


def main():
    time.sleep(2)
    i = 0
    while True:
        click_followers()
        click_accept()
        #i += 1
    print("Program Finished.")
    
    # i = 0
    # while i < 10:
    #     rand = np.random.uniform(0.1,0.5)
    #     print(pyautogui.position())
    #     time.sleep(0.5)
    #     i+= 1
        
if __name__ == '__main__':
    main()
