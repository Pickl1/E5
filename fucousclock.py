import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        time.sleep(1)

    print("Time's up! Take a break.")

# Set the duration of the focus timer in seconds, e.g., 25 * 60 for 25 minutes
duration = 25 * 60
focus_timer(duration)
