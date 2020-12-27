#!/usr/bin/env python
# coding: utf-8

# In[10]:


###### print("---------Simple Student Management System------------")

name="Seda"
surname="Bicer"


AllCourses=['1-python','2-java' ,'3-c++' ,'4-c#', '5-html']

def calculate_score(a1,b1,c1):
    point=(a1*30/100)+(b1*50/100)+(c1*20/100)
    if point>=90:
        print(f"Your grade is {point} :AA")
        return "AA"
    elif point<90 and point>=70:
        print(f"Your grade is {point} :BB ")
        return "BB"
    elif point<70 and point>=50:
        print(f"Your grade is {point} :CC ")  
        return "CC"
    elif point<50 and point>=30:
        print(f"Your grade is {point} :DD ")
        return "DD"
    else:
        print(f"Your grade is {point} :FF\nYou did not pass this lesson.")
        return "FF"
        
courseList=[]
gradeList=[]
count=0
flag=0
while flag<3:
    UserName=input("Please enter your name:")
    UserSurname=input("Please enter your name:")
    if name==UserName and surname==UserSurname:
        print("Welcome "+name+" "+surname)
        print("\n")
        courseNum=int(input("How many lessons would you like to take:"))
        
        if courseNum>=3 and courseNum<=5:
            print(AllCourses)
            
            for h in range(courseNum):
                lessonNum = int(input("Choose your lesson number:"))
                if lessonNum==1:
                    courseList.append("python")
                    a=int (input("Enter Midterm Grade:"))
                    b=int (input("Enter Final Grade:"))
                    c=int (input("Enter Project Grade:"))
                    gradeList.append(calculate_score(a,b,c))
                    
                elif lessonNum==2:
                    courseList.append("java")
                    a=int (input("Enter Midterm Grade:"))
                    b=int (input("Enter Final Grade:"))
                    c=int (input("Enter Project Grade:"))
                    gradeList.append(calculate_score(a,b,c))
                    
                elif lessonNum==3:
                    courseList.append("c++")
                    a=int (input("Enter Midterm Grade:"))
                    b=int (input("Enter Final Grade:"))
                    c=int (input("Enter Project Grade:"))
                    gradeList.append(calculate_score(a,b,c))
                    
                elif lessonNum==4:
                    courseList.append("html")
                    a=int (input("Enter Midterm Grade:"))
                    b=int (input("Enter Final Grade:"))
                    c=int (input("Enter Project Grade:"))
                    gradeList.append(calculate_score(a,b,c))
                    
                else:
                    print("wrong input")
            
            print("Complete succesfully!")
            grade_dic=dict(zip(courseList, gradeList))
            print(grade_dic)
            break
            
                
        elif courseNum<3:
            print("You Failed In Class")
            break    
                
        else:
            print("Enter Less Than 5")
           
           
    else:
        print("You entered incorrectly !")
        flag = flag+1
    break

if flag==3:
    print("Please try again later")


# In[ ]:





# In[ ]:





# In[ ]:




