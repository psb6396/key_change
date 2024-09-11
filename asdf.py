import keyboard
import time

start_time = None
duration = 3
function_have_been_executed = False

def change_key_option():
    pass

while True:
    if keyboard.is_pressed('ctrl'):
        if start_time is None:
            start_time = time.time()  # Start timing when Ctrl is first pressed
        elif time.time() - start_time >= duration:
            print(f"'Ctrl' has been held for {duration} seconds!")
    else: # ctrl 버튼에서 손 뗐을 때 함수 실행됨.
        change_key_option() 
        print('함수실행됨.')
        start_time = None  # Reset if Ctrl is released
    time.sleep(0.5)  # Check every 500ms