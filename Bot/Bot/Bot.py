#imports
import cv2
import numpy as np
import pyautogui
import time

#image search function
def search_image(standartImage,margin=0.8):
    #screenshot and file conversion
    Vscreenshot = pyautogui.screenshot()
    Vscreen = cv2.cvtColor(np.array(Vscreenshot), cv2.COLOR_BGR2RGB)
    #load model image and convert the image
    Vmodel = cv2.imread(standartImage)
    Vmodel = cv2.cvtColor(Vmodel, cv2.COLOR_BGR2RGB)
    #check the images
    Vresult = cv2.matchTemplate(Vscreen, Vmodel, cv2.TM_CCOEFF_NORMED)
    #check the results
    _, max_val, _, max_loc = cv2.minMaxLoc(Vresult)
    if max_val >= margin:
        return max_loc, max_val #return position and margin
    return None, max_val

#main loop
try:
    while True:
        time.sleep(0.05)
        
        # try match the image with 0.2 of margin
        position_taget1, trust = search_image('target_image', threshold=0.8)
        
        if position_taget1:
            print(f"image match! trust of: {trust}")
            position_btn, trust_btn = search_image('target_btn.png', threshold=0.8)
            if position_btn:
                target1 = pyautogui.locateCenterOnScreen('target_btn.png')
                pyautogui.click(target1.x, target1.y)
                print(f"btn target! trust: {trust_btn}")
                time.sleep(1)
            else:
                print(f"btn not target.")

        else:
            print(f"image not target.")


except KeyboardInterrupt:
    print("\nExecucao interrompida pelo usuario.")