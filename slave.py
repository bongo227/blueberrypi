from bluetooth import *

print("Searching...")
devices = discover_devices(lookup_names = True)

print("Found %d devices", len(devices))

for name, addr in devices:
    print("%s - %s", addr, name)
