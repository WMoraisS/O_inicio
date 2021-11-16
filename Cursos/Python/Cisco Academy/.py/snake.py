import platform

print(platform.python_implementation())

for atr in platform.python_version_tuple():
    print(atr)