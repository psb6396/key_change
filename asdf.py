# %%
import keyboard
import time
import mouse

start_time = None
duration = 3
function_have_been_executed = False

def press_mouse_button():
    mouse.press(button='left')  # Simulate pressing the left mouse button
    print("Mouse button pressed")

def release_mouse_button():
    mouse.release(button='left')  # Simulate releasing the left mouse button
    print("Mouse button released")
    
def ctrl_c():
    keyboard.send('ctrl+c')

def change_key_option():
    keyboard.on_press_key('s', lambda _: press_mouse_button(), suppress=True)   # Press 's' to press mouse button
    keyboard.on_release_key('s', lambda _: release_mouse_button(), suppress=True)  # Release 's' to release mouse button
    keyboard.add_hotkey('d', ctrl_c, suppress=True)

while True:
    if keyboard.is_pressed('ctrl') and function_have_been_executed == False:
        if start_time is None:
            start_time = time.time()  # Start timing when Ctrl is first pressed
        elif time.time() - start_time >= duration:
            print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")
            change_key_option()
            function_have_been_executed = True
    elif(keyboard.is_pressed('ctrl') == False):
        print('.')
        start_time = None  # Reset if Ctrl is released
        function_have_been_executed = False
    time.sleep(0.5)  # Check every 500ms


# %%
keyboard.unhook_all()


