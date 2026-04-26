minutes = input("Enter minutes: ")
minutes = int(minutes)
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours} години {remaining_minutes} хвилин")
