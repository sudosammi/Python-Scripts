import time
from plyer import notification

print("🔔 Desktop Notifier start")

#Loop

while True:
    notification.notify(
        title = "Hello!",
        message = "Nothing",
        app_icon = "",
        timeout = 10 # seconds

    )

    time.sleep(10) # Sleep for 10 sec

