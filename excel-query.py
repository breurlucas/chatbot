import pandas as pd

df = pd.read_excel(r'raw.xlsx')

# Keys necessary to locate data: 'group' and 'day'
# Group is defined by BCCCAS1NA which can be broken down the following way:
# BCC: Course
# CAS: Campus
# 1: Semester
# N: Nocturnal
# A: Subgroup

# Within the same course and campus (For now, BCCCAS), we can thus define which group a student is part of by using only the terms '1-8' and subgroups 'A', 'B' and 'A/2'.

# Example 1: If a student is from the 1st semester, we will find two possible groups: BCCCASS1NA and BCCCASS1NB. In this case, we need to ask if he is from subgroup 'A' or 'B' to retrieve an answer.

# Example 2: If a student is from the 3rd semester, we won't need to ask any follow up questions to define his group, there is only one option: BCCCASS1NA (The group is small enough to avoid the need for subgroups)

# 
# GROUP AND DAY FOUND: QUERYING

# We managed to find these two datapoints from the conversation
group = 'BCCCAS3NA'
day = '2/7/2022'

# Query the dataframe to find which subjects this group has on this day
df_selection = (df.loc[(df['Turma'] == group) & (df['Dia'] == '2/7/2022'), ['Aula', 'Horário']])

# All subjects
subject_1st_hour = df_selection.iloc[0,0]
subject_2nd_hour = df_selection.iloc[1,0]
subject_3rd_hour = df_selection.iloc[2,0]
subject_4th_hour = df_selection.iloc[3,0]

# All schedules
_1st_hour = df_selection.iloc[0,1]
_2nd_hour = df_selection.iloc[1,1]
_3rd_hour = df_selection.iloc[2,1]
_4th_hour = df_selection.iloc[3,1]

# 
# Example

# Question: "Hoje a aula é de que?"
print("No primeiro horário, às {1} e {2} você tem aula de {0}. No segundo horário, às {4} e {5}, você tem aula de {3}.".format(subject_1st_hour, _1st_hour, _2nd_hour, subject_3rd_hour, _3rd_hour, _4th_hour))

