# description: Determines BMI
# author: Aziz, Muhammad
# date: 9.13.2018

print("Enter Height in Feet and Inches")
feet_height = int(input("Enter Feet: ")) #get height in feet
inches_height = int(input("Enter Inches: ")) #get height in inches
raw_weight = int(input("Enter weight in pounds: ")) #get weight in pounds

total_height = (feet_height*12) + inches_height #adds up total height in inches

print ("Height is",total_height,"inches") #presents user with their total height


weight_kg = raw_weight / 2.205 #BMI calculations
height_m = total_height / 39.37
height_m_squared = height_m**2
bmi = weight_kg / height_m_squared

print("('Your Body Mass Index is',"+ str(round(bmi,1)) +")") #I did it this way because
                                                 #it's exactly how it's presented
                                                  #on the hw prompt, looks weird
if bmi < 18.5: #presents user with bmi info
      print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
      print("Normal Weight")
elif bmi >= 25 and bmi <= 29.9:
      print("Overweight")
else:
      print("Obese")
      
      
    
      
