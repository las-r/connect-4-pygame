from cx_Freeze import setup, Executable

setup(
    name="connect-4",
    executables=[Executable("connect-4.py", base="Win32GUI")],
)
