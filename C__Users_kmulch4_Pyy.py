#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from numpy import sqrt 


# In[2]:


pwd


# In[5]:


# Loading dataset
df = pd.read_csv('shots_data.csv')
df.head()


# In[6]:


# Determine the shotzones(2PT, NC3 or C3)
df.loc[(df.y <= 7.8) & (abs(df.x) <= 22) , 'Shot Distribution'] = '2PT'
df.loc[(df.y <= 7.8) & (abs(df.x) > 22) , 'Shot Distribution'] = 'C3'
df.loc[(df.y > 7.8) & (sqrt(df.x ** 2 + df.y ** 2) <= 23.75) , 'Shot Distribution'] = '2PT'
df.loc[(df.y > 7.8) & (sqrt(df.x ** 2 + df.y ** 2) > 23.75) , 'Shot Distribution'] = 'NC3'
df.loc[(df.y > 7.8) & (abs(df.x) > 22) , 'Shot Distribution'] = 'NC3'


# In[7]:


df.head()


# In[9]:


# Team A FGs
team_a_shots = df[df["team"] == "Team A"]

# Team B FGs
team_b_shots = df[df["team"] == "Team B"]


# In[10]:


# The amount of team A shots attempted within a zone
team_a_shots_dist = team_a_shots['Shot Distribution'].value_counts()
team_a_shots_dist


# In[11]:


# calculate Shot Distribution: the percentage of team A shots attempted within a zone
teamA_FGA = team_a_shots.shape[0]
team_a_shots_attempted_2PT = team_a_shots_dist["2PT"] / teamA_FGA
team_a_shots_attempted_C3 = team_a_shots_dist["C3"] / teamA_FGA
team_a_shots_attempted_NC3 = team_a_shots_dist["NC3"] / teamA_FGA
print (f'The percentage of team A shots attempted within 2PT: {(team_a_shots_attempted_2PT):.2%}')
print (f'The percentage of team A shots attempted within C3: {(team_a_shots_attempted_C3):.2%}')
print (f'The percentage of team A shots attempted within NC3: {(team_a_shots_attempted_NC3):.2%}')


# In[12]:


# show Shot Distribution in DataFrame
data_a = [['Two Point', f'{(team_a_shots_attempted_2PT):.2%}'], ['Corner 3', f'{(team_a_shots_attempted_C3):.2%}'],  
        ['Non Corner 3', f'{(team_a_shots_attempted_NC3):.2%}']]
dfa = pd.DataFrame(data_a, columns = ['Team A Distribution', 'Percentage of Shots Attempted'])
dfa


# In[13]:


# The amount of team B shots attempted within a zone
team_b_shots_dist = team_b_shots['Shot Distribution'].value_counts()
team_b_shots_dist


# In[14]:


# calculate Shot Distribution: the percentage of team B shots attempted within a zone
teamB_FGA = team_b_shots.shape[0]
team_b_shots_attempted_2PT = team_b_shots_dist["2PT"] / teamB_FGA
team_b_shots_attempted_C3 = team_b_shots_dist["C3"] / teamB_FGA
team_b_shots_attempted_NC3 = team_b_shots_dist["NC3"] / teamB_FGA
print (f'The percentage of team B shots attempted within 2PT: {(team_b_shots_attempted_2PT):.2%}')
print (f'The percentage of team B shots attempted within C3: {(team_b_shots_attempted_C3):.2%}')
print (f'The percentage of team B shots attempted within NC3: {(team_b_shots_attempted_NC3):.2%}')


# In[15]:


# show Shot Distribution in DataFrame
data_b = [['Two Point', f'{(team_b_shots_attempted_2PT):.2%}'], ['Corner 3', f'{(team_b_shots_attempted_C3):.2%}'],  
        ['Non Corner 3', f'{(team_b_shots_attempted_NC3):.2%}']]
dfb = pd.DataFrame(data_b, columns = ['Team B Distribution', 'Percentage of Shots Attempted'])
dfb


# In[16]:


# data of teamA in each zone
df_teamA_2PT = team_a_shots.loc[team_a_shots['Shot Distribution'] == '2PT']
df_teamA_NC3 = team_a_shots.loc[team_a_shots['Shot Distribution'] == 'NC3']
df_teamA_C3 = team_a_shots.loc[team_a_shots['Shot Distribution'] == 'C3']

# data of teamB in each zone
df_teamB_2PT = team_b_shots.loc[team_b_shots['Shot Distribution'] == '2PT']
df_teamB_NC3 = team_b_shots.loc[team_b_shots['Shot Distribution'] == 'NC3']
df_teamB_C3 = team_b_shots.loc[team_b_shots['Shot Distribution'] == 'C3']


# In[17]:


teamA_FGA_2PT = df_teamA_2PT.shape[0]
teamA_FGA_NC3 = df_teamA_NC3.shape[0]
teamA_FGA_C3 = df_teamA_C3.shape[0]
print (f'FGA of team A within 2PT: {teamA_FGA_2PT}')
print (f'FGA of team A within NC3: {teamA_FGA_NC3}')
print (f'FGA of team A within C3: {teamA_FGA_C3}')

teamB_FGA_2PT = df_teamB_2PT.shape[0]
teamB_FGA_NC3 = df_teamB_NC3.shape[0]
teamB_FGA_C3 = df_teamB_C3.shape[0]
print (f'\nFGA of team B within 2PT: {teamB_FGA_2PT}')
print (f'FGA of team B within NC3: {teamB_FGA_NC3}')
print (f'FGA of team B within C3: {teamB_FGA_C3}')


# In[18]:


# FGs Attempted - Team A (0 = Miss, 1 = Make)
team_a_shots_made = team_a_shots['fgmade'].value_counts()
team_a_shots_made_2PT = df_teamA_2PT['fgmade'].value_counts()
team_a_shots_made_NC3 = df_teamA_NC3['fgmade'].value_counts()
team_a_shots_made_C3 = df_teamA_C3['fgmade'].value_counts()

# FGs Attempted - Team B (0 = Miss, 1 = Make)
team_b_shots_made = team_b_shots['fgmade'].value_counts()
team_b_shots_made_2PT = df_teamB_2PT['fgmade'].value_counts()
team_b_shots_made_NC3 = df_teamB_NC3['fgmade'].value_counts()
team_b_shots_made_C3 = df_teamB_C3['fgmade'].value_counts()

print ('FGs Attempted (0 = Miss, 1 = Make):')
print (f'\n=== All Zone === \nTeamA:\n{team_a_shots_made}\n\nTeamB:\n{team_b_shots_made}')
print (f'\n=== 2PT Zone === \nTeamA:\n{team_a_shots_made_2PT}\n\nTeamB:\n{team_b_shots_made_2PT}')
print (f'\n=== NC3 Zone === \nTeamA:\n{team_a_shots_made_NC3}\n\nTeamB:\n{team_b_shots_made_NC3}')
print (f'\n=== C3 Zone === \nTeamA:\n{team_a_shots_made_C3}\n\nTeamB:\n{team_b_shots_made_C3}')


# In[22]:


# FG Made
teamA_FGM = team_a_shots_made[1]
teamA_FGM_2PT = team_a_shots_made_2PT[1]
teamA_FGM_NC3 = team_a_shots_made_NC3[1]
teamA_FGM_C3 = team_a_shots_made_C3[1]
teamB_FGM = team_b_shots_made[1]
teamB_FGM_2PT = team_b_shots_made_2PT[1]
teamB_FGM_NC3 = team_b_shots_made_NC3[1]
teamB_FGM_C3 = team_b_shots_made_C3[1]
print(f'FG Made - Team A : {teamA_FGM}\nFG Made(2PT Zone) - Team A : {teamA_FGM_2PT}\nFG Made(NC3 Zone) - Team A : {teamA_FGM_NC3}\nFG Made(C3 Zone) - Team A : {teamA_FGM_C3}\n')
print(f'FG Made - Team B : {teamB_FGM}\nFG Made(2PT Zone) - Team B : {teamB_FGM_2PT}\nFG Made(NC3 Zone) - Team B : {teamB_FGM_NC3}\nFG Made(C3 Zone) - Team B : {teamB_FGM_C3}\n')   


# In[23]:


# 3pt Made - Team A
pt3_made_team_a_shots = team_a_shots[(team_a_shots['fgmade'] == 1) & ((team_a_shots['Shot Distribution'] == "C3") | (team_a_shots['Shot Distribution'] == "NC3"))]
pt3_made_team_b_shots = team_b_shots[(team_b_shots['fgmade'] == 1) & ((team_b_shots['Shot Distribution'] == "C3") | (team_b_shots['Shot Distribution'] == "NC3"))]
teamA_3PM = pt3_made_team_a_shots.shape[0]
teamA_3PM_NC3 = pt3_made_team_a_shots[pt3_made_team_a_shots['Shot Distribution'] == "NC3"].shape[0]
teamA_3PM_C3 = pt3_made_team_a_shots[pt3_made_team_a_shots['Shot Distribution'] == "C3"].shape[0]
try:
    teamA_3PM_2PT = pt3_made_team_a_shots[pt3_made_team_a_shots['Shot Distribution'] == "2PT"].shape[0]
except:
    teamA_3PM_2PT = None
    
# 3pt Made - Team B
teamB_3PM = pt3_made_team_b_shots.shape[0]
teamB_3PM_NC3 = pt3_made_team_b_shots[pt3_made_team_b_shots['Shot Distribution'] == "NC3"].shape[0]
teamB_3PM_C3 = pt3_made_team_b_shots[pt3_made_team_b_shots['Shot Distribution'] == "C3"].shape[0]
try:
    teamB_3PM_2PT = pt3_made_team_b_shots[pt3_made_team_b_shots['Shot Distribution'] == "2PT"].shape[0]
except:
    teamB_3PM_2PT = None
print(f'3pt Made - Team A : {teamA_3PM}')
print(f'3pt Made(2PT Zone) - Team A : {teamA_3PM_2PT}')
print(f'3pt Made(NC3 Zone) - Team A : {teamA_3PM_NC3}')
print(f'3pt Made(C3 Zone) - Team A : {teamA_3PM_C3}')
print(f'\n3pt Made - Team B : {teamB_3PM}')
print(f'3pt Made(2PT Zone) - Team B : {teamB_3PM_2PT}')
print(f'3pt Made(NC3 Zone) - Team B : {teamB_3PM_NC3}')
print(f'3pt Made(C3 Zone) - Team B : {teamB_3PM_C3}')


# In[24]:


# Team An Effective Field Goal Percentage
eFG_a = (teamA_FGM + ((0.5*teamA_3PM))) / teamA_FGA
eFG_a_2PT = (teamA_FGM_2PT + ((0.5*teamA_3PM_2PT))) / teamA_FGA_2PT
eFG_a_NC3 = (teamA_FGM_NC3 + ((0.5*teamA_3PM_NC3))) / teamA_FGA_NC3
eFG_a_C3 = (teamA_FGM_C3 + ((0.5*teamA_3PM_C3))) / teamA_FGA_C3

# Team B Effective Field Goal Percentage
eFG_b = (teamB_FGM + ((0.5*teamB_3PM))) / teamB_FGA
eFG_b_2PT = (teamB_FGM_2PT + ((0.5*teamB_3PM_2PT))) / teamB_FGA_2PT
eFG_b_NC3 = (teamB_FGM_NC3 + ((0.5*teamB_3PM_NC3))) / teamB_FGA_NC3
eFG_b_C3 = (teamB_FGM_C3 + ((0.5*teamB_3PM_C3))) / teamB_FGA_C3
print (f'Team A Effective All Field Goal Percentage: {eFG_a:.2%}')
print (f'Team A Effective 2PT Field Goal Percentage: {eFG_a_2PT:.2%}')
print (f'Team A Effective NC3 Field Goal Percentage: {eFG_a_NC3:.2%}')
print (f'Team A Effective C3 Field Goal Percentage: {eFG_a_C3:.2%}')
print (f'\nTeam B Effective All Field Goal Percentage: {eFG_b:.2%}')
print (f'Team B Effective 2PT Field Goal Percentage: {eFG_b_2PT:.2%}')
print (f'Team B Effective NC3 Field Goal Percentage: {eFG_b_NC3:.2%}')
print (f'Team B Effective C3 Field Goal Percentage: {eFG_b_C3:.2%}')


# In[25]:


# Show Effective Field Goal Percentage in dataFrame
data = [['Team A', f'{(round(eFG_a, 4)):.2%}', f'{(round(eFG_a_2PT, 4)):.2%}', f'{(round(eFG_a_NC3, 4)):.2%}', f'{(round(eFG_a_C3, 4)):.2%}'], 
        ['Team B', f'{(round(eFG_b, 4)):.2%}', f'{(round(eFG_b_2PT, 4)):.2%}', f'{(round(eFG_b_NC3, 4)):.2%}', f'{(round(eFG_b_C3, 4)):.2%}']]
dfefg = pd.DataFrame(data, columns = ['Team', 'eFG%', '2PT eFG%', 'NC3 eFG%', 'C3 eFG%'])
dfefg


# In[ ]:


#End

