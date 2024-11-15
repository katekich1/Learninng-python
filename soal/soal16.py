from datetime import datetime

now = datetime.now()

formatted_time = now.strftime("%A, %d of %B on %Y, %I:%M:%S %p")

print(formatted_time)