import struct
import time
import curses

# Emit a touch event to the input device using struct
def emit_event(device, event_type, event_code, event_value):
    event = struct.pack('llHHi', int(time.time()), int((time.time() % 1) * 1e6), event_type, event_code, event_value)
    device.write(event)
    device.flush()

# Swipe left function
def swipe_left():
    with open("/dev/input/event2", "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 1500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 1000)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 53, 1200)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            time.sleep(0.05)

            emit_event(device, 3, 53, 900)   # Move to X = 900
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            time.sleep(0.05)

            emit_event(device, 3, 53, 500)   # Move to X = 500 (left side of the screen)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay before lifting the finger
            time.sleep(0.05)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()

# Swipe right function
def swipe_right():
    with open("/dev/input/event2", "wb") as device:
        try:
            # Simulate touch down at starting position (left side)
            emit_event(device, 3, 53, 500)   # ABS_MT_POSITION_X (X coordinate, starting at the left)
            emit_event(device, 3, 54, 1000)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the right (swipe)
            emit_event(device, 3, 53, 900)   # Move to X = 900
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            time.sleep(0.05)

            emit_event(device, 3, 53, 1200)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            time.sleep(0.05)

            emit_event(device, 3, 53, 1500)  # Move to X = 1500 (right side of the screen)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay before lifting the finger
            time.sleep(0.05)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()

def on_key_event(event):
    if event.name == 'j':
        print("key pressed")

# Main function to listen for keyboard inputs
def main(stdscr):

    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.addstr("Press key")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == ord('j'):
            swipe_right()
        if key == ord('k'):
            swipe_left()
        if key == curses.KEY_LEFT:
            swipe_right()
        if key == curses.KEY_RIGHT:
            swipe_left()

        stdscr.refresh()

    keyboard.wait('esc')

if __name__ == "__main__":
    curses.wrapper(main)

