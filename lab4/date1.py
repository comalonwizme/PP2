from datetime import datetime, timedelta
print(f"Today is{datetime.now() : %y-%m-%d\n} 5 days ago was{datetime.now() - timedelta(days=5) : %y-%m-%d}")
