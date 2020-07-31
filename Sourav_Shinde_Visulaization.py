import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from fpdf import FPDF
import sys


def differenttechnologies(students_data):
    # a. The number of students applied to different technologies.
    plt.subplots(figsize=(25, 17))
    sns.countplot(x="Areas of interest", data=students_data)
    plt.xlabel('Different Technologies.')
    plt.ylabel('count')
    plt.xticks(rotation=45)
    plt.savefig("2A-A.png")


def python(stud_cpy):
   # b.The number of students applied for Data Science who knew ‘’Python” and who didn’t.
    data_science = students_data[students_data['Areas of interest']=='Data Science ']
    python = data_science[data_science['Programming Language Known other than Java (one major)']=='Python']
    dk_python = data_science[data_science['Programming Language Known other than Java (one major)']!='Python']


    index_p = python.index
    index_n = dk_python.index
    py = len(index_p)
    dkpy = len(index_n)
    print(dkpy)
    print(py)


    plt.subplots(figsize=(25, 12))
    Label = "Knows Python", "Did'nt Know Python"
    d_count = [py, dkpy]
    piecolor = ["blue", "red"]
    explode = (0.1, 0.1)
    plt.pie(d_count, explode=explode, labels=Label, colors=piecolor, autopct='%1.1f%%', shadow=True, startangle=0)
    plt.axis('equal')
    plt.savefig("2B.png")


def internship(students_data):
   # c.The different ways students learned about this program.
    plt.subplots(figsize=(25, 12))
    ways = students_data['How Did You Hear About This Internship?'].value_counts()
    sns.barplot(x=ways.index, y=ways.values)
    plt.xlabel('Different ways.')
    plt.ylabel('count')
    plt.savefig("2C.png")


def fourthyear(students_data):
    # d. Students who are in the fourth year and have a CGPA greater than 8.0.
    fourth = students_data[(students_data['Which-year are you studying in?'] == 'Fourth-year')]
    d = fourth[fourth['CGPA/ percentage']> 8.0]

    plt.subplots(figsize=(20, 10))
    sns.countplot(x="Major/Area of Study", data=d)
    plt.xlabel('Fourth Year students scoring greater then 8 ptr, Branch Wise')
    plt.ylabel('count')
    plt.savefig("2D.png")


def communicate(students_data):
   # e. Students who applied for Digital Marketing with verbal and written communication score greater than 8.
    digital = students_data[(students_data['Areas of interest'] == 'Digital Marketing ')]
    skills = digital[digital['Rate your written communication skills [1-10]'] > 8]
    skills = skills[skills['Rate your verbal communication skills [1-10]'] > 8]

    fig, ax = plt.subplots(figsize=(25, 12))
    ax.set_ylabel('Number of students')
    ax.set_xlabel('Ratings')
    communication = skills['Rate your written communication skills [1-10]'].value_counts()
    verbal = skills['Rate your verbal communication skills [1-10]'].value_counts()
    sns.lineplot(x=communication.index, y=communication.values, ax=ax, label='Written')
    sns.lineplot(x=verbal.index, y=verbal.values, ax=ax, label='Verbal')
    plt.savefig("2E.png")


def classification(students_data):
   # f. Year-wise and area of study wise classification of students.
    plt.subplots(figsize=(25, 15))
    sns.countplot(x='Which-year are you studying in?', hue='Major/Area of Study', data=students_data)
    plt.xlabel('Year and Area of study')
    plt.ylabel('count')
    plt.savefig("2F.png")


def citycol(students_data):
   # g. City and college wise classification of students.
    plt.subplots(figsize=(35, 20))
    sns.countplot(x='City', hue='College name', data=students_data)
    plt.savefig("2G-A.png")


def relation(students_data):
    rel = students_data.filter(['CGPA/ percentage', 'Label'])
    eli = rel[rel['Label'] == 'eligible']
    s1 = len([x for x in eli['CGPA/ percentage'] if (x < 8 and x >= 7)])
    s2 = len([x for x in eli['CGPA/ percentage'] if (x < 9 and x >= 8)])
    s3 = len([x for x in eli['CGPA/ percentage'] if (x >= 9)])

    s1t = len([x for x in rel['CGPA/ percentage'] if (x < 8 and x >= 7)])
    s2t = len([x for x in rel['CGPA/ percentage'] if (x < 9 and x >= 8)])
    s3t = len([x for x in rel['CGPA/ percentage'] if (x >= 9)])
    df7 = pd.DataFrame({'eligible': [s1, s2, s3], 'ineligible': [s1t - s1, s2t - s2, s3t - s3]})
    plt.figure(9)
    plt.figure(figsize=(10, 5))
    h = df7.plot(kind='bar')
    plt.title("Relationship between CGPA and eligibility", fontsize=20)
    h.set_ylabel("Number of Students")
    h.set_xlabel("Range of CGPA")
    h.set_xticklabels(["7 - 8", "8 - 9", "9 - 10"], rotation=0)
    plt.savefig("2H.png")


def target(students_data):
    # i. Plot Relationship between Area of interest and Target variable
    plt.subplots(figsize=(35, 15))
    sns.countplot(x="Label", hue="Areas of interest", data=students_data)
    plt.xlabel('Year and Area of study')
    plt.ylabel('count')
    plt.savefig("2I.png")


def last(students_data):
    # j. Plot the  Relationship between year of study,major and Target variable
    students =  students_data.rename(columns = {'Major/Area of Study' : 'Major'})
    relation = students.groupby(['Which-year are you studying in?', 'Major', 'Label']).Major.size()[lambda x: x < 1000]
    fig, ax = plt.subplots(figsize=(35, 25))
    relation.unstack().plot.bar(ax=ax)
    plt.xlabel('Year and Area of study')
    plt.ylabel('count')
    plt.savefig("2J.png")



if __name__ == "__main__":
    students_data = pd.read_csv(sys.argv[1])
    students_data.head()
    students_data.tail(10)
    students_data.describe()
    students_data.shape
    students_data.info()

    students_data.isnull().sum()

    students_data.drop(['Certifications/Achievement/ Research papers'], axis=1, inplace=True)
    students_data.drop(['Link to updated Resume (Google/ One Drive link preferred)'], axis=1, inplace = True)
    students_data.drop("link to Linkedin profile", axis=1, inplace=True)

    students_data.isnull().sum()

    differenttechnologies(students_data)
    python(students_data)
    internship(students_data)
    fourthyear(students_data)
    communicate(students_data)
    classification(students_data)
    citycol(students_data)
    target(students_data)
    relation(students_data)
    last(students_data)


    pdf_g = FPDF(orientation='L', unit='mm', format='letter')
    imagelist = ['2A-A.png', '2B.png', '2C.png', '2D.png', '2E.png', '2F.png', '2G-A.png', '2H.png', '2I.png', '2J.png']
    textlist = ['Applied to different technologies', 'Applied for Data Science who knew Python & who did not',
                'Different ways students learned about this program',
                'Students who are in 4th year & have a CGPA > 8.0',
                'Students who applied for Digital Marketing with verbal & written communication score > 8',
                'Year-wise & area of study wise classification', 'City and college wise classification',
                'Relationship between CGPA & target variable',
                'Relationship between Area of Interest & target variable',
                'Relationship between year of study, major, & target variable']
    for (image, text) in zip(imagelist, textlist):
        pdf_g.add_page()
        pdf_g.set_font("Arial", size=14)
        pdf_g.cell(0, 0, txt=text, ln=1, align="C")
        pdf_g.ln(50)
        pdf_g.image(image, x=5, y=15, w=280, h=190)
    pdf_g.output("visualization-output.pdf")