import struct
import time

BOTTOM = "bottom"
TOP = "top"
RIGHT = "right"
LEFT = "left"

# Emit a touch event to the input device using struct
def emit_event(device, event_type, event_code, event_value):
    event = struct.pack('llHHi', int(time.time()), int((time.time() % 1) * 1e6), event_type, event_code, event_value)
    device.write(event)
    device.flush()



def swipe(direction: str) -> None:
    loweredDirection = direction.lower()
    if loweredDirection == BOTTOM:
        return swipe_from_bottom()
    elif loweredDirection == TOP:
        return swipe_from_top()
    elif loweredDirection == RIGHT:
        return swipe_right()
    elif loweredDirection == LEFT:
        return swipe_left()
    else:
        print(f"{direction} not supported. Supported directions are: {BOTTOM}, {TOP}, {LEFT}, {RIGHT}.")
        return

# Swipe left function
def swipe_from_bottom():
    with open("/dev/input/event2", "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 1500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 0)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 54, 300)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 54, 600)   # Move to X = 900
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 54, 900)   # Move to X = 500 (left side of the screen)
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # # Short delay before lifting the finger
            # time.sleep(0.05)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()    

def swipe_from_top():
    with open("/dev/input/event2", "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 1800)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 54, 1500)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 54, 1200)   # Move to X = 900
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 54, 600)   # Move to X = 500 (left side of the screen)
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay before lifting the finger
            # time.sleep(0.05)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()               

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

            # time.sleep(0.05)

            # emit_event(device, 3, 53, 900)   # Move to X = 900
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 53, 500)   # Move to X = 500 (left side of the screen)
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # # Short delay before lifting the finger
            # time.sleep(0.05)

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

            # time.sleep(0.05)

            # emit_event(device, 3, 53, 1200)  # Move to X = 1200
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # time.sleep(0.05)

            # emit_event(device, 3, 53, 1500)  # Move to X = 1500 (right side of the screen)
            # emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # # Short delay before lifting the finger
            # time.sleep(0.05)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()