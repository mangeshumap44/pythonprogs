sub1=input("enter marks of subject 1")
sub2=input("enter marks of subject 2")
sub3=input("enter marks of subject 3")
sub4=input("enter marks of subject 4")
sub5=input("enter marks of subject 5")
total=sub1+sub2+sub3+sub4+sub5
if total > 450:
    print("Grade A")
elif total >=400:
    print("Grade B")
elif total >=350:
    print("Grade C")
elif total >=300:
    print("Grade D")
elif total < 300:
    print("Pass")
else:
    print("Fail")