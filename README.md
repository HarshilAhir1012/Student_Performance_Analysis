# 📊 Student Performance Analysis (EDA Project)

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a student performance dataset to understand how different academic, social, and personal factors influence students’ final grades.

The analysis is done using **Python**, focusing on data cleaning, statistical analysis, and data visualization.

---

## 🎯 Objectives
- Analyze students’ academic performance
- Study the effect of factors like:
  - Gender
  - Study time
  - Absences
  - Past failures
  - Family educational support
- Visualize patterns and relationships in the data
- Extract meaningful insights from the dataset

---

## 🛠 Tools & Libraries Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Dataset Information
- Dataset: Student Performance (Math course)
- File used: `student_data.csv`
- Target Variable: `G3` (Final Grade)

The dataset contains information about:
- Demographics (gender, age, address)
- Study habits (study time, failures)
- Family & social background
- Academic performance (G1, G2, G3)

---

## 🔍 Steps Performed

### 1. Data Loading & Understanding
- Loaded CSV data using Pandas
- Checked shape, columns, data types
- Identified missing values and duplicates

### 2. Data Cleaning
- Handled missing values
- Removed duplicate entries
- Ensured correct data types

### 3. Exploratory Data Analysis (EDA)
- Descriptive statistics
- Group-based analysis using `groupby()`
- Correlation analysis
- Visualization using bar plots, box plots, scatter plots, and heatmaps

## Detailed Steps :

# 📊 Student Performance Analysis

## 🔍 Exploratory Data Analysis – Question Set
---

## 🟢 SECTION 1: Understanding the Data

1. How many students are present in the dataset?
2. How many features (columns) does the dataset have?
3. What are the data types of each column?
4. Are there any missing values in the dataset?
5. What is the distribution of students by gender?

---

## 🟢 SECTION 2: Academic Performance Analysis

6. What is the average final grade (G3) of students?
7. What is the average G3 score for male vs female students?
8. Which students scored the highest and lowest final grades?
9. What is the distribution of final grades (G3)?
10. How many students scored above 15 in final grade?

---

## 🟢 SECTION 3: Study Habits & Attendance

11. How does weekly study time affect final grades?
12. Is there a relationship between absences and G3?
13. Do students with fewer failures perform better?
14. What is the average grade of students with extra study support?
15. Does family support influence academic performance?

---

## 🟢 SECTION 4: Lifestyle & Social Factors

16. Does free time after school affect grades?
17. Is alcohol consumption related to student performance?
18. Do students in romantic relationships perform differently?
19. Does internet access at home improve grades?
20. Does going out with friends affect performance?

---

## 🟢 SECTION 5: Visualization-Based Questions

21. Plot the distribution of final grades using a histogram.
22. Create a boxplot comparing G3 scores by gender.
23. Plot absences vs final grade and analyze the trend.
24. Create a heatmap showing correlations between numeric features.
25. Visualize study time vs performance using bar or box plots.

---

## 🟢 SECTION 6: Advanced Analysis (Still EDA – No ML)

26. Identify top 10% performing students.
27. Compare performance of students who want higher education vs those who don’t.
28. Which factor shows the strongest correlation with final grade?
29. Are students with more past failures at higher risk of low grades?
30. What are the key indicators of good academic performance?

---

## 🟢 SECTION 7: Insight & Conclusion Questions

31. What are the 5 most important insights from this dataset?
32. Which factors negatively affect student performance the most?
33. Which factors positively affect student performance the most?
34. What recommendations can be given to improve student results?
35. What limitations does this dataset have?

---

---

## 🔍 Columns Informathion

# Attributes for both student-mat.csv (Math course) and student-por.csv (Portuguese language course) datasets:
1 school - student's school (binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira)
2 sex - student's sex (binary: "F" - female or "M" - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: "U" - urban or "R" - rural)
5 famsize - family size (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3)
6 Pstatus - parent's cohabitation status (binary: "T" - living together or "A" - apart)
7 Medu - mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
8 Fedu - father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
9 Mjob - mother's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
10 Fjob - father's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
11 reason - reason to choose this school (nominal: close to "home", school "reputation", "course" preference or "other")
12 guardian - student's guardian (nominal: "mother", "father" or "other")
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)

# these grades are related with the course subject, Math or Portuguese:
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)

Additional note: there are several (382) students that belong to both datasets . 
These students can be identified by searching for identical attributes
that characterize each student, as shown in the annexed R file.


## 📊 Key Questions Answered
- What is the average final grade (G3) by gender?
- Is there a relationship between absences and final grade?
- Do students with fewer past failures perform better?
- Does family educational support influence academic performance?
- Which factors correlate most with final grades?

---

## 📈 Key Insights
- Female students have a slightly higher average final grade than male students.
- Absences show **very weak negative correlation** with final grades.
- Past failures have a **moderate negative correlation** with performance.
- Family support shows a **positive but weak influence** on grades.
- Academic performance depends on multiple factors, not a single variable.

---

## 📌 Conclusion
The analysis shows that **past academic failures and study-related habits** have a stronger impact on student performance than social factors alone.  
Exploratory data analysis helps identify important trends and risk factors that can support better academic decision-making.

---

## 🚀 Future Work
- Apply Machine Learning models to predict final grades
- Feature selection and model evaluation
- Compare multiple models (Linear Regression, Decision Tree, etc.)

---

## 👤 Author
**Harshil Ahir**  
Data Science Learner | Computer Science Student

