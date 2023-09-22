FOREGROUND_BLACK = 0x00
FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN = 0x02
FOREGROUND_CYAN = 0x03
FOREGROUND_RED = 0x04
FOREGROUND_MAGENTA = 0x05
FOREGROUND_YELLOW = 0x06
FOREGROUND_GREY = 0x07
FOREGROUND_INTENSITY = 0x08  # Foreground text is bold

# Background colors
BACKGROUND_BLUE = 0x10
BACKGROUND_GREEN = 0x20
BACKGROUND_CYAN = 0x30
BACKGROUND_RED = 0x40
BACKGROUND_MAGENTA = 0x50
BACKGROUND_YELLOW = 0x60
BACKGROUND_GREY = 0x70
BACKGROUND_INTENSITY = 0x80  # Background text is bold

def set_cmd_text_color(color, handle_std_handle=True):
    """Changes the cmd prompt output color"""
    STD_OUTPUT_HANDLE = -11 if handle_std_handle else -12
    h = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetConsoleTextAttribute(h, color)
