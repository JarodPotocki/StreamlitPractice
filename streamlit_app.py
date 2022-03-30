
##### This app is just an extremely simple example.
##### See the Streamlit documentation for how to create more complex apps.

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.title( 'Top 20 Baseball Players based on Stat' )
st.write( '''
This app helps to show different batting statistics of the top 20 players per statistic
''' )


df_batting = pd.read_csv('player-batting-stats-1988-2016.csv')

df_batting_top_20 = df_batting[df_batting['Rk'] < 21]

Team = st.sidebar.selectbox('Choose a team', df_batting_top_20['Tm'].unique())
batting_team_20 = df_batting_top_20[df_batting_top_20['Tm'] == Team]
Statistic = st.sidebar.selectbox('Choose a statistic',(
 'G',
 'PA',
 'AB',
 'R',
 'H',
 '2B',
 '3B',
 'HR',
 'RBI',
 'SB',
 'CS',
 'BB',
 'SO',
 'BA',
 'OBP',
 'SLG',
 'OPS',
 'OPS+',
 'TB',
 'GDP',
 'HBP',
 'SH',
 'SF',
 'IBB'))

fig, ax = plt.subplots()
ax.hist(batting_team_20[Statistic])
st.pyplot(fig)
