first_name = input("Enter your name: ")
std = input("Enter your standard: ")

print("Hello", first_name, "welcome to your marks report for", std, "standard")


math = int(input("Enter Maths marks: "))
sci = int(input("Enter Science marks: "))
eng = int(input("Enter English marks: "))
soc = int(input("Enter Social marks: "))

total = (math + sci + eng + soc)/400*100
print(total)