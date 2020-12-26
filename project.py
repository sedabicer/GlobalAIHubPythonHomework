#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("---------Simple Student Management System------------")

adi = "Seda"
soyad= "Bicer"

adi1 =input("Please enter your name: ")
soyad1= input("Please enter your surname: ")
i=0
courselist=[]
resultofexams = {"midterm": 38, "final": 66, "project":89}
check = False

def calculate_score():
    score = (resultofexams["midterm"]*30 + resultofexams["final"]*50 + resultofexams["project"]*20)/100
    return score

while i < 3 :
    if i == 3 :
        print("Please try again later")
        break
       
    if (adi != adi1 or soyad != soyad1):
        print("You entered incorrectly !")
        adi1 =input("Please enter your name: ")
        soyad1= input("Please enter your surname: ")
        i += 1
        continue
    else:
        print("")
        print("Welcome "+adi1+" "+soyad1)
        lesson = int(input('How many lessons would you like to take? '))
        j = 0
        if lesson <=5 and lesson >=3:
            while(j<lesson):
                course=input("Course you want to add: ")
                courselist.append(course)
                j += 1
                check = True
                continue
            print(" ")
            print("Lessons you have taken: " ,courselist)
            print(" ")
        elif lesson >=5:
            print("You can take up to 5 lessons!")
            break
        else:
            print("You failed in class.You must take at least 3 lessons!")
            break
        break
        
if check == True:
        
        lessonNum = int(input("Choose your lesson number:"))
      
        while True:    
            if lessonNum < 1 and lessonNum > 5:
                print("You must enter number of list")
            else:
                grade = calculate_score()
                if grade < 30:
                    print(f"Your grade is {grade} :FF\nYou did not pass this lesson.")
                elif grade >= 30 and grade < 50:
                    print(f"Your grade is {grade} :DD ")
                elif grade >= 50 and grade < 70:
                    print(f"Your grade is {grade} :CC ")    
                elif grade >= 70 and grade < 90:
                    print(f"Your grade is {grade} :BB ")
                elif grade > 90:
                    print(f"Your grade is {grade} :AA")
            break


# In[ ]:




