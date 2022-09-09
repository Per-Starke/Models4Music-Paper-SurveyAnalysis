"""Take the person group dataframes from group_answers and visualize what we are interested in"""
__author__ = "Per Starke"

import matplotlib.pyplot as plt
from group_answers import *


def make_plot(df_column, title):
    """
    Make a bar plot of the value counts of the given column
    :param df_column: column of dataframe that we want to plot, in the form df['Column_name']
    :param title: The titel of the plot
    """

    # Count the values and sort by index
    counts = df_column.value_counts()
    counts.sort_index(ascending=True, inplace=True)

    length = len(counts)

    # Make the plot
    fig, ax = plt.subplots()
    ax.bar(range(0, length), counts)

    # Label the axes
    ax.xaxis.set(ticks=range(0, length), ticklabels=counts.index)
    ax.yaxis.set(ticks=range(0, max(counts) + 2, 2))

    ax.set_title(title)


"""
#####
# Plot the general information about the participants
#####

make_plot(df['IT_expertise'], 'IT-Expertise')
make_plot(df['Profession'], 'Profession')
make_plot(df['Gender'], 'Gender')


# Plot the age groups

age_group_counts = [len(df_agegroup_1), len(df_agegroup_2), len(df_agegroup_3), len(df_agegroup_4)]
fig_age, ax_age = plt.subplots()
ax_age.bar(range(0, 4), age_group_counts)
ax_age.xaxis.set(ticks=range(0, 4), ticklabels=['<20', '20-40', '40-60', '>60'])
ax_age.yaxis.set(ticks=range(0, max(age_group_counts)+2, 2))
ax_age.set_title('Agegroups')
"""

#####
# Plot the answers for the questions, for the different person groups
#####

# Plot the answers, by gender

make_plot(df_males['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Males')
make_plot(df_males['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Males')
make_plot(df_males['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - Males')
make_plot(df_males['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Males - After')
make_plot(df_males['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Males- After')

make_plot(df_females['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Females')
make_plot(df_females['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Females')
make_plot(df_females['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                         'Females')
make_plot(df_females['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Females - After')
make_plot(df_females['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Females - After')

make_plot(df_other_gender['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Other gender')
make_plot(df_other_gender['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Other gender')
make_plot(df_other_gender['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? '
                                                              '- Other gender')
make_plot(df_other_gender['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Other gender - After')
make_plot(df_other_gender['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Other gender- After')


# Plot the answers, by age group
"""
make_plot(df_agegroup_1['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Age group 1')
make_plot(df_agegroup_1['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Age group 1')
make_plot(df_agegroup_1['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                            'Age group 1')
make_plot(df_agegroup_1['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Age group 1 - After')
make_plot(df_agegroup_1['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Age group 1 - After')

make_plot(df_agegroup_2['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Age group 2')
make_plot(df_agegroup_2['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Age group 2')
make_plot(df_agegroup_2['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                            'Age group 2')
make_plot(df_agegroup_2['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Age group 2 - After')
make_plot(df_agegroup_2['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Age group 2 - After')

make_plot(df_agegroup_3['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Age group 3')
make_plot(df_agegroup_3['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Age group 3')
make_plot(df_agegroup_3['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                            'Age group 3')
make_plot(df_agegroup_3['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Age group 3 - After')
make_plot(df_agegroup_3['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Age group 3 - After')

make_plot(df_agegroup_4['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Age group 4')
make_plot(df_agegroup_4['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Age group 4')
make_plot(df_agegroup_4['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                            'Age group 4')
make_plot(df_agegroup_4['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Age group 4 - After')
make_plot(df_agegroup_4['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Age group 4 - After')
"""

# Plot the answers, by profession
"""
make_plot(df_school['Amper_creative'], 'Would you call the Amper-AI "Creative"? - School')
make_plot(df_school['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - School')
make_plot(df_school['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                        'School')
make_plot(df_school['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - School - After')
make_plot(df_school['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - School - After')

make_plot(df_study['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Study')
make_plot(df_study['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Study')
make_plot(df_study['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                       'Study')
make_plot(df_study['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Study - After')
make_plot(df_study['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Study - After')

make_plot(df_work['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Work')
make_plot(df_work['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Work')
make_plot(df_work['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                      'Work')
make_plot(df_work['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Work - After')
make_plot(df_work['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Work - After')

make_plot(df_other_profession['Amper_creative'], 'Would you call the Amper-AI "Creative"? - Other profession')
make_plot(df_other_profession['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - Other profession')
make_plot(df_other_profession['Creativity_definition_agreement'], 'Would you agree with this definition of '
                                                                  '"Creativity"? - Other profession')
make_plot(df_other_profession['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - Other profession - After')
make_plot(df_other_profession['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - Other profession '
                                                      '- After') 
"""

# Plot the answers, by IT-Expertise
"""
make_plot(df_it['Amper_creative'], 'Would you call the Amper-AI "Creative"? - IT-Expertise')
make_plot(df_it['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - IT-Expertise')
make_plot(df_it['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                    'IT-Expertise')
make_plot(df_it['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - IT-Expertise - After')
make_plot(df_it['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - IT-Expertise - After')

make_plot(df_no_it['Amper_creative'], 'Would you call the Amper-AI "Creative"? - No IT-Expertise')
make_plot(df_no_it['DeepBach_creative'], 'Would you call the DeepBach-AI "Creative"? - No IT-Expertise')
make_plot(df_no_it['Creativity_definition_agreement'], 'Would you agree with this definition of "Creativity"? - '
                                                       'No IT-Expertise')
make_plot(df_no_it['Amper_creative_2'], 'Would you call the Amper-AI "Creative"? - No IT-Expertise - After')
make_plot(df_no_it['DeepBach_creative_2'], 'Would you call the DeepBach-AI "Creative"? - No IT-Expertise - After')
"""

plt.show()
