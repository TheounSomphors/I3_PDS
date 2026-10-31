total_seconds=9875
hour=total_seconds//3600
minute=(total_seconds % 3600)//60
second=(total_seconds % 3600)%60
print("a. Compute hours, minutes ,and second ")
print(hour,"h",minute,"min",second,"s")
print("b. Check:",(hour*3600)+(minute*60)+second ==total_seconds)

# creat function 
def convert_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{total_seconds} seconds = {hours} h {minutes} min {seconds} s") #(a)
    print("Check:", hours * 3600 + minutes * 60 + seconds == total_seconds) #(b)
    
convert_time(9875)
print("Test code with 3600, 59 and 86899 second ")
for t in (3600, 59, 86399):   # (c) tests
    convert_time(t)

