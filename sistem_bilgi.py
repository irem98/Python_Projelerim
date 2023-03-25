import psutil

cpu_usage = psutil.cpu_percent()

memory_usage = psutil.virtual_memory().percent

disk_usage = psutil.disk_usage("/").percent

print(f"CPU usage:{cpu_usage}%")
print(f"memory usage:{memory_usage}%")
print(f"disk usage:{disk_usage}%")

