import pandas as pd
import matplotlib.pyplot as plt

#Reading the CSV file into a DataFrame
data = pd.read_csv('students.csv')

#Displaying the first 5 rows of the DataFrame
print(data.head())

#Displaying the dataset metrics
data.describe()

#Calculate the average score of the students
average_score = data['score'].mean()

#Calculate the highest and lowest scores
highest_score = data['score'].max()
lowest_score = data['score'].min()

#Filtering students scored at least 90
high_performers = data[data['score'] >= 90]

#Find students who studies above 5 hours
frequent_studiers = data[data ['study_hours'] > 5]

#Find students who study more than 5 hours and have an attendance rate above 95%
students = data[
   ( data['study_hours'] > 5) & (data['attendance'] > 95)
    ]

#Finding the top student index based on the score
top_student_index = data['score'].idxmax()
top_student = data.loc[top_student_index]

#Calculate average score by grade
average_score_by_grade = data.groupby('grade')['score'].mean()

#Calculating the average score by grade
average_score_by_grade = (
    data.groupby('grade')['score']
    .mean()
    .round(2)
) 

#Calculating multiple statistics at once
grade_summary = (
    data.groupby('grade')['score']
    .agg(['mean', 'median', 'max', 'min'])
    .round(2)
) 

#Finding the correlation between the study_hours and score
correlation = data['study_hours'].corr(data['score'])

#Creating Scatter plot to visualize the relationship between study hours and score
plt.scatter(data['study_hours'], data['score'])
plt.xlabel('\n Study Hours')
plt.ylabel('Score')
plt.title('Study Hours vs Test Score \n')
plt.show()

#Creating a bar graph to compare the average scores of students in different grades
average_score_by_grade.plot(kind = 'bar', color = 'blue')
plt.xlabel('\n Grade')
plt.ylabel('Average Score')
plt.title('Average Score by Grade \n')
plt.show()
