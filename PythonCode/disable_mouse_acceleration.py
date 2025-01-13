import ctypes
from ctypes import wintypes

# Define constants for SPI actions
SPI_GETMOUSE = 0x0003
SPI_SETMOUSE = 0x0004
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

# Define the SystemParametersInfo function
SystemParametersInfo = ctypes.windll.user32.SystemParametersInfoW
SystemParametersInfo.argtypes = [wintypes.UINT, wintypes.UINT, ctypes.c_void_p, wintypes.UINT]
SystemParametersInfo.restype = wintypes.BOOL


def disable_enhanced_pointer_precision():
    # Create an integer array to store mouse parameters
    mouse_params = (3 * ctypes.c_int)()

    # Get the current mouse parameters
    result = SystemParametersInfo(SPI_GETMOUSE, 0, mouse_params, 0)
    if not result:
        return False

    # Set the acceleration value to 0 to disable enhanced pointer precision
    mouse_params[2] = 0

    # Update the system settings
    return SystemParametersInfo(SPI_SETMOUSE, 0, mouse_params, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


if __name__ == "__main__":
    print("Disabling enhanced pointer precision...")
    result = disable_enhanced_pointer_precision()
    if result:
        print("Enhanced pointer precision disabled successfully.")
    else:
        print("Failed to disable enhanced pointer precision.")
