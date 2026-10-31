name="Somphors"
age="22"
major="Data science"
gpa= 3.59
is_scholar=True

print("=" * 30)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("=" * 30)
for value in (name, age, major, gpa, is_scholar):
    print(f"{repr(value):15}", "->", type(value).__name__)

# (C)
age="20"
print (type(age))