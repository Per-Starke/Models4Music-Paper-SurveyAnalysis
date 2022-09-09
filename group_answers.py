"""Use the cleaned data from load_and_clean, and group it into person groups we are interested in analyzing"""
__author__ = "Per Starke"

from load_and_clean import df

# create one df for each gender
df_males = df[df.Gender == 'Male']
df_females = df[df.Gender == 'Female']
df_other_gender = df[df.Gender == 'Something else']


# create one df for each profession
df_work = df[df.Profession == 'I work']
df_study = df[df.Profession == 'I study']
df_school = df[df.Profession == 'I go to school']
df_other_profession = df[df.Profession == 'Something else']


# create one df for each age-group: <20, 20-40, 40-60, >60
df_agegroup_1 = df[df.Age < 20]

df_agegroup_2 = df[df.Age >= 20]
df_agegroup_2 = df_agegroup_2[df_agegroup_2.Age < 40]

df_agegroup_3 = df[df.Age >= 40]
df_agegroup_3 = df_agegroup_3[df_agegroup_3.Age < 60]

df_agegroup_4 = df[df.Age >= 60]


# create one df for each level of it-expertise (yes/no)
df_it = df[df.IT_expertise == 'Yes']
df_no_it = df[df.IT_expertise == 'No']
