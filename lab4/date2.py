from datetime import datetime, timedelta

print(f"Yesterday{datetime.now() - timedelta(days=1) : %y-%m-%d}")
print(f"Today{datetime.now() : %y-%m-%d}")
print(f"Tomorrow{datetime.now() + timedelta(days=1) : %y-%m-%d}")
