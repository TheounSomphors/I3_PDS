def letter_grade(score):
      
     if score < 0 or score > 100:
          return "Invalid"
     elif score >=97 :
          return "A+"
     elif score >= 90:
          return "A"
     elif score >=80:
          return "B"
     elif score >= 70:
          return "C"
     elif score >= 60:
          return "D"
     elif score< 50:
          return "F"
sc=[99,38,-34,45,90,87,69,101]
for m in sc:
     #print(m,"-->", letter_grade(m))
     print(f"{m:>6}-->{letter_grade(m)}")
print(m,"-->", letter_grade(m))