# This will help you calculate your percentage of marks in no time!

sub1 = float(input("Enter the scored marks for this subject: "))
sub2 = float(input("Enter the scored marks for this subject: "))
sub3 = float(input("Enter the scored marks for this subject: "))
sub4 = float(input("Enter the scored marks for this subject: "))
sub5 = float(input("Enter the scored marks for this subject: "))
sub6 = float(input("Enter the scored marks for this subject: "))
sub7 = float(input("Enter the scored marks for this subject: "))
sub8 = float(input("Enter the scored marks for this subject: "))
sub9 = float(input("Enter the scored marks for this subject: "))
sub10 = float(input("Enter the scored marks for this subject: "))

tm1 = float(input("Enter the total marks for this sub1: "))
tm2 = float(input("Enter the total marks for this sub2: "))
tm3 = float(input("Enter the total marks for this sub3: "))
tm4 = float(input("Enter the total marks for this sub4: "))
tm5 = float(input("Enter the total marks for this sub5: "))
tm6 = float(input("Enter the total marks for this sub6: "))
tm7 = float(input("Enter the total marks for this sub7: "))
tm8 = float(input("Enter the total marks for this sub8: "))
tm9 = float(input("Enter the total marks for this sub9: "))
tm10 = float(input("Enter the total marks for this sub10: "))

total_scored_marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9 + sub10
final_score = tm1 + tm2 + tm3 + tm4 + tm5 + tm6 + tm7 + tm8 + tm9 + tm10

percentage = (total_scored_marks / final_score) * 100

print("Your percentage is = ", percentage)
