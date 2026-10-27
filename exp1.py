name=input("Enter student name:")
n=int(input("Enter no of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage>=80:
    grade="A"
    performace="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="Needs improvement"
print("\n---Academic performance---")
print("student name:",name)
print("total marks:",mark)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("performance:",performance)
    
           
    
