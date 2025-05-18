# for loops = execute a block of code a fixed number of time 
            #   you can ierate  over a range,string,sequence,etc

# for x in range (1,21):
#     if x == 13:
#         break
#     else:
#         print(x) 
# nested loop = A loop within another loop (outer,inner)
#                outer loop:inner loop 
rows = int(input("enter the of rows: "))
colum = int(input("enter the of column"))
symbol = input("enter a symbol to use")
for x in range(3):
    for y in range(1,10):
        print(y,end=" ")
    print()