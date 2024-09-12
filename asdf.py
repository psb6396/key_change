import keyboard
import time

start_time = None
duration = 3
function_have_been_executed = False

def change_key_option():
    pass

while True:
    if keyboard.is_pressed('ctrl') and function_have_been_executed == False:
        if start_time is None:
            start_time = time.time()  # Start timing when Ctrl is first pressed
        elif time.time() - start_time >= duration:
            print(f"'Ctrl' 버튼이 {time.time() - start_time} 초 동안 눌려짐.")

            function_have_been_executed = True
    elif(keyboard.is_pressed('ctrl') == False):
        print('.')
        start_time = None  # Reset if Ctrl is released
        function_have_been_executed = False
    time.sleep(0.5)  # Check every 500ms
