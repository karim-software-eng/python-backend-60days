temps=[70,75,95,80,100,72]
for temp in temps:
    if temp>=90:
        print(f"Warning: Temperature {temp} is too high, skipping...")
        continue
    elif temp<90:
        print(f"Temperature {temp} is safe.")    



  






