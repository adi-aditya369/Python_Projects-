import time

my_time= int(input("enter the time in seconds: "))

for a in range (my_time,0,-1):
    seconds = a % 60 
    minutes = int(a/60)%60
    hours = int(a /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
  
    time.sleep(1)
print("times up")