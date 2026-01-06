import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
space = "===" * 25


sns.set_theme(
    style="whitegrid",
    context="notebook",
    palette="deep"
)

class DataAnalyzer:
    def __init__(self, student_data):
        self.student_data = student_data
    

    
    


    # ## 🟢 SECTION 1: Understanding the Data

        # 1. How many students are present in the dataset?
        # 2. How many features (columns) does the dataset have?
        # 3. What are the data types of each column?
        # 4. Are there any missing values in the dataset?
        # 5. What is the distribution of students by gender?


    def analyze_data(self): ## Section_1

        print(space)
        Student_count = self.student_data.shape[0]
        print(f" 🤷‍♂️ How many students are present in the dataset? : {Student_count}")
        print(space)

        time.sleep(1)
        coulumn_count = self.student_data.shape[1]
        print(f" 💭 How many features (columns) does the dataset have? : {coulumn_count}")
        print(space)

        time.sleep(1)
        Info_coloumns = self.student_data.info()
        print(f" 🤷 What are the data types of each column? : {Info_coloumns}")
        print(space)

        time.sleep(1)
        missing_values = sum(self.student_data.isnull().sum())
        print(f" 💬 How many missing values are there? : {missing_values}")
        print(space)

        time.sleep(1)
        gender_distribution = self.student_data["sex"].value_counts()
        print(f" 🤷 What is the distribution of students by gender?? : {gender_distribution}")
        print(space)
        time.sleep(1)

        print(f" 📶 Plot the distribution of students by gender : \n")
        gender_distribution.plot.bar(color=['yellow', 'pink'])
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.title('Distribution of Students by Gender')
        plt.show()
        print(space)
        time.sleep(1)

        plt.show()

        print_end(1)
        
        return Student_count , coulumn_count , Info_coloumns , missing_values , gender_distribution
    
     ## 🟢 SECTION 2: Academic Performance Analysis

        # 6. What is the average final grade (G3) of students?
        # 7. What is the average G3 score for male vs female students?
        # 8. Which students scored the highest and lowest final grades?
        # 9. What is the distribution of final grades (G3)?
        # 10. How many students scored above 15 in final grade?

    def Academic_performance(self): ## Section_2

        print(space)
        time.sleep(1)

        avg_final_grade = self.student_data['G3'].mean()
        print(f" 💬 What is the average final grade (G3) of students? : {avg_final_grade}")
        print(space)
        time.sleep(1)

        avg_final_grade_male_female = self.student_data.groupby('sex')['G3'].mean()
        print(f" 🤷‍♂️ What is the average G3 score for male vs female students? : {avg_final_grade_male_female}")
        print(space)
        time.sleep(1)

        highest_final_grade = self.student_data[self.student_data['G3'] == self.student_data['G3'].max()]
        lowest_final_grade = self.student_data[self.student_data['G3'] == self.student_data['G3'].min()]

        print(f" 💭 Which students scored the highest and lowest final grades? : \n Highest one :{highest_final_grade} ")
        print(space)
        print(f" Lowest one :{lowest_final_grade} ")    
        print(space)
        time.sleep(1)

        
        students_above_15 = self.student_data[self.student_data['G3'] > 15].count()['G3']
        print(f" 🤷  How many students scored above 15 in final grade? : {students_above_15}")
        print(space)
        time.sleep(1)

        print(f" 🎦 What is the distribution of final grades (G3)? : ")
        plt.figure(figsize=(8, 6))
        sns.histplot(self.student_data['G3'], bins=20, kde=True, color='skyblue')
        plt.xlabel('Final Grade (G3)')
        plt.ylabel('Frequency')
        plt.title('Distribution of Final Grades (G3)')
        print(space)
        time.sleep(1)

        plt.show()

        print_end(2)

        return avg_final_grade , avg_final_grade_male_female , highest_final_grade , lowest_final_grade , students_above_15
    
    # ## 🟢 SECTION 3: Study Habits & Attendance

    # 11. How does weekly study time affect final grades?
    # 12. Is there a relationship between absences and G3?
    # 13. Do students with fewer failures perform better?
    # 14. What is the average grade of students with extra study support?
    # 15. Does family support influence academic performance?

    def Study_Habits_Attendance(self): ## Section_3
        
        print(space)
        time.sleep(1)

        print(" 💭 How does weekly study time affect final grades?\n")
        corr_of_studytime_G3 = self.student_data['studytime'].corr(self.student_data['G3'])
        corr_reletion(corr_of_studytime_G3,'studytime','G3')
        print(space)
        time.sleep(1)

        print(" 💭 Is there a relationship between absences and G3?\n")
        corr_of_absences_G3 = self.student_data['absences'].corr(self.student_data['G3'])
        corr_reletion(corr_of_absences_G3,'absences','G3')
        print(space)
        time.sleep(1)

        print(" 🤷‍♂️ Do students with fewer failures perform better? \n")
        corr_of_failures_G3 = self.student_data['failures'].corr(self.student_data['G3'])
        corr_reletion(corr_of_failures_G3,'failures','G3')
        print(space)
        time.sleep(1)

        avg_grade_extra_support = self.student_data[self.student_data['schoolsup'] == 'yes']['G3'].mean()
        print(f" 💭 What is the average grade of students with extra study support? : {avg_grade_extra_support}")
        corr_of_extrasup_G3 = self.student_data['schoolsup'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3'])
        corr_reletion(corr_of_extrasup_G3,'schoolsup','G3')
        print(space)
        time.sleep(1)
       

        print(" 🤷‍♂️ Does family support influence academic performance? \n")
        corr_of_famsup_G3 = self.student_data['famsup'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3'])
        corr_reletion(corr_of_famsup_G3,'famsup','G3')
        print(space)
        time.sleep(1)

        print(" 📈 Plots for Study Habits & Attendance Analysis:")
        print(space)
        time.sleep(1)


        print(f" 🎦 Plot showing weekly study time vs G3 : ")
        plt.figure(figsize=(6, 4))
        sns.boxplot(x='studytime', y='G3', data=self.student_data)
        plt.xlabel('Weekly Study Time')
        plt.ylabel('Final Grade (G3)')
        plt.title('Weekly Study Time vs Final Grade With corr = ' + str(round(corr_of_studytime_G3,5)))
        plt.grid(True)
        print(space)
        time.sleep(1)
        plt.show()

        print(f" ▶️ Plot showing family support vs G3 : ")
        # plt.figure(figsize=(6, 4))
        sns.violinplot(x='famsup', y='G3', data=self.student_data)
        plt.xlabel('Family Support')
        plt.ylabel('Final Grade (G3)')
        plt.title('Family Support vs Final Grade With corr =' + str(round(corr_of_famsup_G3,5)))
        plt.grid(True)
        print(space)
        time.sleep(1)
        plt.show()

        print(f" 📶 plot showing extra study support vs G3 : ")
        # plt.figure(figsize=(6, 4))
        sns.boxplot(x='schoolsup', y='G3', data=self.student_data)
        plt.xlabel('Extra Study Support')
        plt.ylabel('Final Grade (G3)')
        plt.title('Extra Study Support vs Final Grade with corr =' + str(round(corr_of_extrasup_G3,5)))
        plt.grid(True)
        print(space)
        time.sleep(1)
        plt.show()

        print_end(3)
        return corr_of_studytime_G3 , corr_of_absences_G3 , corr_of_failures_G3 , avg_grade_extra_support  , corr_of_extrasup_G3 , corr_of_famsup_G3
    
    ## 🟢 SECTION 4: Lifestyle & Social Factors

        # 16. Does free time after school affect grades?
        # 17. Is alcohol consumption related to student performance?
        # 18. Do students in romantic relationships perform differently?
        # 19. Does internet access at home improve grades?
        # 20. Does going out with friends affect performance?

    def Lifestyle_Social_Factors(self): ## Section_4
        
        print(space)
        time.sleep(1)

        print(" 💬 Does free time after school affect grades? \n")
        corr_of_freetime_G3 = self.student_data['freetime'].corr(self.student_data['G3'])
        corr_reletion(corr_of_freetime_G3,'freetime','G3')
        print(space)
        time.sleep(1)

        print(" 🍻 Is alcohol consumption related to student performance? \n")
        corr_of_alcohol_G3 = self.student_data['Dalc'].corr(self.student_data['G3'])
        corr_reletion(corr_of_alcohol_G3,'Dalc','G3')
        print(space)
        time.sleep(1)

        print(" 🫶 Do students in romantic relationships perform differently? \n")
        corr_of_romantic_G3 = self.student_data['romantic'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3']) 
        corr_reletion(corr_of_romantic_G3,'romantic','G3')
        print(space)    
        time.sleep(1)

        print(" 🗼 Does internet access at home improve grades\n")
        corr_of_internet_G3 = self.student_data['internet'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3'])
        corr_reletion(corr_of_internet_G3,'internet','G3')
        print(space)
        time.sleep(1)

        print(" 🐦‍🔥 Does going out with friends affect performance? \n")
        corr_of_goout_G3 = self.student_data['goout'].corr(self.student_data['G3'])
        corr_reletion(corr_of_goout_G3,'goout','G3')
        print(space)
        time.sleep(1)

        print(" 📈 Plots for Lifestyle & Social Factors Analysis:")
        print(space)
        time.sleep(1)

        print(f" 📶 Plot showing free time after school vs G3 : ")
        plt.figure(figsize=(6, 4))  
        sns.violinplot(x='freetime', y='G3', data=self.student_data)
        plt.xlabel('Free Time After School')
        plt.ylabel('Final Grade (G3)')
        plt.title('Free Time After School vs Final Grade with corr = ' + str(round(corr_of_freetime_G3,5)))
        plt.grid(True)  
        print(space)
        time.sleep(1)
        plt.show()

        fig,ax = plt.subplots(2,2,figsize=(16, 10))
        print(f" 🎦 Plot showing going alcohol consumption vs G3 : ")

        sns.violinplot(x='Dalc', y='G3', data=self.student_data, ax=ax[0,0])
        ax[0,0].set_xlabel('Going Alcohol Consumption')
        ax[0,0].set_ylabel('Final Grade (G3)')
        ax[0,0].set_title('Going Alcohol Consumption vs Final Grade with corr = ' + str(round(corr_of_alcohol_G3,5)))
        plt.grid(True)  
        print(space)
        time.sleep(1)

        print(" 📈 Plot showing romantic relationship vs G3 : ")
        # plt.figure(figsize=(6, 4))  
        sns.violinplot(x='romantic', y='G3', data=self.student_data , ax=ax[0,1])
        ax[0,1].set_xlabel('Romantic Relationship')
        ax[0,1].set_ylabel('Final Grade (G3)')
        ax[0,1].set_title('Romantic Relationship vs Final Grade with corr = ' + str(round(corr_of_romantic_G3,5)))
        plt.grid(True)  
        print(space)
        time.sleep(1)

        print(" 📶 plot showing internet access at home vs G3 : ")
        # plt.figure(figsize=(6, 4))
        sns.violinplot(x='internet', y='G3', data=self.student_data, ax=ax[1,0])
        ax[1,0].set_xlabel('Internet Access at Home')
        ax[1,0].set_ylabel('Final Grade (G3)')
        ax[1,0].set_title('Internet Access at Home vs Final Grade with corr = ' + str(round(corr_of_internet_G3,5)))
        plt.grid(True)
        print(space)
        time.sleep(1)

        print(" ▶️ plot showing going out with friends vs G3 : ")
        # plt.figure(figsize=(6, 4))
        sns.boxplot(x='goout', y='G3', data=self.student_data, ax=ax[1,1])
        ax[1,1].set_xlabel('Going Out with Friends')
        ax[1,1].set_ylabel('Final Grade (G3)')
        ax[1,1].set_title('Going Out with Friends vs Final Grade with corr = ' + str(round(corr_of_goout_G3,5)))
        plt.grid(True)
        print(space)
        time.sleep(1)
        plt.tight_layout()
        plt.show()


        print_end(4)
        
    ## 🟢 SECTION 5: Visualization-Based Questions

        # 21. Plot the distribution of final grades using a histogram.
        # 22. Create a boxplot comparing G3 scores by gender.
        # 23. Plot absences vs final grade and analyze the trend.
        # 24. Create a heatmap showing correlations between numeric features.
        # 25. Visualize study time vs performance using bar or box plots.

    def Visualization_Based_Questions(self):
         ## Section_5
        fig = plt.figure()
        fig, ax = plt.subplots(2, 2,figsize=(12, 10))

        print(f" 📶 Plot the distribution of final grades using a histogram : ")
        sns.histplot(self.student_data['G3'], bins=20, kde=True, ax=ax[0,0], color="coral",edgecolor="black")
        ax[0,0].set_xlabel('Final Grade (G3)')
        ax[0,0].set_ylabel('Frequency') 
        ax[0,0].set_title('Distribution of Final Grades (G3)')
        print(space)
        time.sleep(1)

        print(f" 🎦 Create a boxplot comparing G3 scores by gender : ")
        sns.boxplot(x='sex', y='G3', data=self.student_data, ax=ax[0,1])
        ax[0,1].set_xlabel('Gender')
        ax[0,1].set_ylabel('Final Grade (G3)')
        ax[0,1].set_title('G3 Scores by Gender')
        print(space)
        time.sleep(1)

        print(f" ⏩ Plot absences vs final grade and analyze the trend : ")
        sns.lineplot(x='absences', y='G3', data=self.student_data, ax=ax[1,0])
        ax[1,0].set_xlabel('Absences')
        ax[1,0].set_ylabel('Final Grade (G3)')
        ax[1,0].set_title('Absences vs Final Grade (G3)')
        print(space)
        time.sleep(1)


        print(f" 📶 Visualize study time vs performance using bar or box plots : ")
        sns.boxplot(x='studytime', y='G3', data=self.student_data, ax=ax[1,1],color="lightgreen")
        ax[1,1].set_xlabel('Weekly Study Time')
        ax[1,1].set_ylabel('Final Grade (G3)')
        ax[1,1].set_title('Study Time vs Final Grade (G3)')
        print(space)
        time.sleep(1)

        plt.tight_layout()
        plt.show()

        print(f" 📈 Create a heatmap showing correlations between numeric features : ")
        num_columns = self.student_data.select_dtypes(include='number')
        sns.heatmap(num_columns.corr(), annot=False, cmap='coolwarm', center=0,linecolor="black", linewidths=0.2,)
        plt.title('Correlation Heatmap')
        print(space)
        time.sleep(1)
        plt.show()


        print_end(5)
        
    ## 🟢 SECTION 6: Insight & Conclusion Question
        
        # 26. What are the 5 most important insights from this dataset?
        # 27. Which factors negatively affect student performance the most?
        # 28. Which factors positively affect student performance the most?
        # 29. What recommendations can be given to improve student results?
        # 30. What limitations does this dataset have?
        
    def Insight_Conclusion_Questions(self): ## Section_6
        
        print(space)
        print("This section requires subjective analysis and interpretation of the data.")

        print(" 💭 What are the 5 most important insights from this dataset? :\n")
        
        print("1) Past failures have a strong negative impact on final grades.")
        print("2) Early academic performance (G1, G2) strongly predicts final results (G3).")
        print("3) Study time has a positive but limited effect on performance.")
        print("4) Absences show very weak correlation with final grades.")
        print("5) Family and school support have a small positive influence.")

        print(space)
        time.sleep(1)

        print(" 💬 Which factors negatively affect student performance the most? :\n")
        print("1) Past failures with corr = {}".format(round(self.student_data['failures'].corr(self.student_data['G3']),5)))
        print("2) Alcohol consumption with corr = {}".format(round(self.student_data['Dalc'].corr(self.student_data['G3']),5)))
        print("3) Low study time with corr = {}".format(round(self.student_data['studytime'].corr(self.student_data['G3']),5)))
        print("4) poor family support with corr = {}".format(round(self.student_data['famsup'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3']),5)))
        print(space)
        time.sleep(1)

        print(" 🚀 Which factors positively affect student performance the most? :")
        print("1) early grades G1 and G2 with corr = {} and {} respectively".format(round(self.student_data['G1'].corr(self.student_data['G3']),5),round(self.student_data['G2'].corr(self.student_data['G3']),5)))
        print("2) Higher study time with corr = {}".format(round(self.student_data['studytime'].corr(self.student_data['G3']),5)))
        print("3) motivation of higher education with corr = {}".format(round(self.student_data['higher'].map({'yes': 1, 'no': 0}).corr(self.student_data['G3']),5)))

        print(space)
        time.sleep(1)
    
        print("🤷‍♂️💭 What recommendations can be given to improve student results? :")

        print("- Provide early support to students with past failures.")
        print("- Encourage consistent and structured study habits.")
        print("- Reduce negative lifestyle behaviors such as alcohol consumption.")
        print("- Strengthen family and school educational support systems.")
        print("- Motivate students to set higher education goals.")

        print(space)
        time.sleep(1)

        print(" 📉 What limitations does this dataset have? :")

        print("1) Correlation does not imply causation.")
        print("2) Dataset is limited to a small number of schools.")
        print("3) Some variables are self-reported and may contain bias.")
        print("4) Important qualitative factors are not included.")
        print("5) Dataset represents a static snapshot, not long-term trends.")
        print(space)
        time.sleep(1)

        print_end(6)




student_data = pd.read_csv('student_data.csv')

def print_end(n):
    print("-------- End of Section {} Analysis !!! --------".format(n)) 

def corr_reletion(corr,x_name,y_name):
        if corr == 1:
            strength = "Perfect positive correlation btwn " + x_name + " and " + y_name
        elif corr == -1:
            strength = "Perfect negative correlation " + x_name + " and " + y_name
        elif corr > 0.7:
            strength = "Strong positive correlation " + x_name + " and " + y_name
        elif corr > 0.3:
            strength = "Moderate positive correlation " + x_name + " and " + y_name
        elif corr > 0:
            strength = "Weak positive correlation " + x_name + " and " + y_name
        elif corr == 0:
            strength = "No correlation " + x_name + " and " + y_name
        elif corr < -0.7:
            strength = "Strong negative correlation " + x_name + " and " + y_name 
        elif corr < -0.3:
            strength = "Moderate negative correlation " + x_name + " and " + y_name 
        else:
            strength = "Weak negative correlation " + x_name + " and " + y_name 

        print(f"Correlation between {x_name} and {y_name} is : {corr}")
        print(f"Interpretation: {strength}")

def ditaied_description():
   print("Loding ...❄️")
   time.sleep(2)
   print('''\n---------- 🔍 Exploratory Data Analysis – Question Set ----------\n
         
    ---

    1️⃣ SECTION 1: Understanding the Data

    1. How many students are present in the dataset?
    2. How many features (columns) does the dataset have?
    3. What are the data types of each column?
    4. Are there any missing values in the dataset?
    5. What is the distribution of students by gender?

    ---

    2️⃣ SECTION 2: Academic Performance Analysis

    6. What is the average final grade (G3) of students?
    7. What is the average G3 score for male vs female students?
    8. Which students scored the highest and lowest final grades?
    9. What is the distribution of final grades (G3)?
    10. How many students scored above 15 in final grade?

    ---

    3️⃣ SECTION 3: Study Habits & Attendance

    11. How does weekly study time affect final grades?
    12. Is there a relationship between absences and G3?
    13. Do students with fewer failures perform better?
    14. What is the average grade of students with extra study support?
    15. Does family support influence academic performance?

    ---

    4️⃣ SECTION 4: Lifestyle & Social Factors

    16. Does free time after school affect grades?
    17. Is alcohol consumption related to student performance?
    18. Do students in romantic relationships perform differently?
    19. Does internet access at home improve grades?
    20. Does going out with friends affect performance?

    ---

    5️⃣ SECTION 5: Visualization-Based Questions

    21. Plot the distribution of final grades using a histogram.
    22. Create a boxplot comparing G3 scores by gender.
    23. Plot absences vs final grade and analyze the trend.
    24. Create a heatmap showing correlations between numeric features.
    25. Visualize study time vs performance using bar or box plots.

    ---

    6️⃣ SECTION 6: Insight & Conclusion Questions

    26. What are the 5 most important insights from this dataset?
    27. Which factors negatively affect student performance the most?
    28. Which factors positively affect student performance the most?
    29. What recommendations can be given to improve student results?
    30. What limitations does this dataset have?

    ---''')


o1 = DataAnalyzer(student_data)

print("\n------------ Welcome to the Student Performance Data Analysis Tool ! ------------\n")
time.sleep(1)
print(" 1️⃣  SECTION 1: Understanding the Data")
time.sleep(1)
print(" 2️⃣  SECTION 2: Academic Performance Analysis")
time.sleep(1)
print(" 3️⃣  SECTION 3: Study Habits & Attendance")
time.sleep(1)
print(" 4️⃣  SECTION 4: Lifestyle & Social Factors")
time.sleep(1)
print(" 5️⃣  SECTION 5: Visualization-Based Questions")
time.sleep(1)
print(" 6️⃣  SECTION 6: Insight & Conclusion Questions")
time.sleep(1)
print(" 👉 For Detail section, please Enter 7 \n")
time.sleep(1)

while True : 
    choice = int(input(" 👉 Enter the section number you want to analyze (1-7) and 0 for exit: "))
    if choice == 0:
      print("Exiting the analysis tool. Goodbye! 😭 ")
      break

    if choice == 1:
        o1.analyze_data()
        
    elif choice == 2:
        o1.Academic_performance()

    elif choice == 3:
        o1.Study_Habits_Attendance()

    elif choice == 4:
        o1.Lifestyle_Social_Factors()

    elif choice == 5:
        o1.Visualization_Based_Questions()

    elif choice == 6:
        o1.Insight_Conclusion_Questions()  

    elif choice == 7:
        ditaied_description()  

    elif choice < 1 or choice > 7:
        print(" 😏 Invalid choice. Please enter a number between 1 and 7. and 0 for exit.")
        choice = int(input(" 👉 Enter the section number you want to analyze (1-7) and 0 for exit: "))