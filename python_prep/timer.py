import time

def set_timer():
    try:
        # Get the number of minutes from the user
        minutes = int(input("Set timer to: "))
        
        # Convert minutes to seconds
        seconds = minutes * 60
        
        # Start the timer
        print(f"Timer set for {minutes} minutes. Starting now!")
        
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02}:{secs:02}'
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
            
        print("Time's up!")
        
    except ValueError:
        print("Please enter a valid number of minutes.")

# Call the function to set and start the timer
set_timer()
