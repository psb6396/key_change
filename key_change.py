# %%
import keyboard
import time
import mouse

start_time = None
duration = 3
change_key_option_have_been_turned_on = False
is_released = False

def press_mouse_button():
    mouse.press(button='left')  # Simulate pressing the left mouse button
    

def release_mouse_button():
    mouse.release(button='left')  # Simulate releasing the left mouse button
    
    
def ctrl_c():
    keyboard.send('ctrl+c')
    
def ctrl_v():
    keyboard.send('ctrl+v')

def change_key_option():
    keyboard.on_press_key('s', lambda _: press_mouse_button(), suppress=True)   # Press 's' to press mouse button
    keyboard.on_release_key('s', lambda _: release_mouse_button(), suppress=True)  # Release 's' to release mouse button
    keyboard.add_hotkey('d', ctrl_c, suppress=True)
    keyboard.add_hotkey('f', ctrl_v, suppress=True)
    
while True:
    while(change_key_option_have_been_turned_on == False):
        if (keyboard.is_pressed('ctrl') == True):
            if start_time is None:
                start_time = time.time()  # Start timing when Ctrl is first pressed
                print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")
            elif time.time() - start_time >= duration:
                print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")
                change_key_option()
                print('핫키 생성')
                change_key_option_have_been_turned_on = True
        elif(keyboard.is_pressed('ctrl') == False):
            print('.')
            start_time = None  # Reset if Ctrl is released
            # break를 여기다 넣으면 안 됨. 안그러면 걍 누르기전에도 손가락 떼있는 상태라 걍 다음 while구문으로 넘어감.
            # 마찬가지로 change_key_option_have_been_turned_on = True 도 여기다 넣으면 안됨 
        time.sleep(0.5)
    while True:  # ctrl에서 손가락 뗐는 지 확인하는 반복문
        if (keyboard.is_pressed('ctrl') == False):
            break
        elif (keyboard.is_pressed('ctrl') == True):
            pass
        time.sleep(0.5)
    while(change_key_option_have_been_turned_on == True):
        if (keyboard.is_pressed('ctrl') == True):
            if start_time is None:
                start_time = time.time()  # Start timing when Ctrl is first pressed
                print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")
            elif time.time() - start_time >= duration:
                print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")
                keyboard.unhook_all()
                print('핫키 해제')
                change_key_option_have_been_turned_on = False
        elif(keyboard.is_pressed('ctrl') == False):
            print('.')
            start_time = None  # Reset if Ctrl is released
            change_key_option_have_been_turned_on = True
        time.sleep(0.5)
    while True:  # ctrl에서 손가락 뗐는 지 확인하는 반복문
        if (keyboard.is_pressed('ctrl') == False):
            break
        elif (keyboard.is_pressed('ctrl') == True):
            pass
        time.sleep(0.5)
    time.sleep(0.5)  # Check every 500ms
    
    



# %%
# keyboard.unhook_all()


