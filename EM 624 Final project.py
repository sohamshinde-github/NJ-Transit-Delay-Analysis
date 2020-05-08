#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:48:17 2019
@author: Soham Shinde
"""

#                                 Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib import style
import matplotlib.cm as cm, matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from datetime import datetime, timedelta
 

#                               - Read csv file -

df = pd.read_csv('2018_03.csv', sep = ',', encoding='utf-8-sig')
df = df[df['type'] == 'NJ Transit']

df_july=pd.read_csv('2018_07.csv', index_col = False)
df_july = df_july[df_july['type'] == 'NJ Transit']

df.dropna()  
df_july = df_july.dropna()

##############################################################################

#                         Displaying statistics Dataset data

print('\n Each columns statistical data for july is given below:')
print('\n')
print(df_july.describe())  


##############################################################################
#       Converting the "scheduled_time" and "actual_time" columns to datetimes

df_july['scheduled_time'] = pd.to_datetime(df_july['scheduled_time']) 
df_july['actual_time'] = pd.to_datetime(df_july['actual_time'])
df_july.head(2)

df_july['scheduled_time'] = pd.to_datetime(df_july['scheduled_time']) 
df_july['actual_time'] = pd.to_datetime(df_july['actual_time'])
df_july.head(2)



################################################################################
#                -  Grouping the train according to train Id and date -


cumu_delay_july = df_july.groupby(['date' , 'train_id']).last() 
cumu_delay_july .head(2)

#Analysis of july month
ontime_trains_july = cumu_delay_july[(cumu_delay_july['delay_minutes']<=0)]
ontime_trains_count_july = ontime_trains_july['delay_minutes'].count()

cancelled_trains = df_july[(df_july['status'] == 'cancelled')]
cancelled_trains_count = cancelled_trains['train_id'].count()

delayed_trains_july = cumu_delay_july[(cumu_delay_july['delay_minutes']>0)]
delayed_trains_count_july = delayed_trains_july['delay_minutes'].count()



##############################################################################
#          - function to produce more beautiful pie charts with matplotlib -

def pie_chart(fractions, #values for the wedges
              labels, #labels for the wedges
              title='', #title of the pie chart
              cm_name = 'Pastel1', #name of the matplotlib colormap to use
              #autopct = lambda x: str(round(x, 1)) + '%', #format the value text on each pie wedge
              labeldistance = 1.05, #where to place wedge labels in relation to pie wedges
              shadow = True, #shadow around the pie
              startangle = 90, 
              edgecolor = 'y', #color of pie wedge edges
              width = 8, #width of the figure in inches
              height = 8, #height of the figure in inches
              grouping_threshold = None, 
              grouping_label = None): 
    
    # if the user passed a threshold value, group all fractions lower than it into one 'misc' pie wedge
    if not grouping_threshold==None:
        
        # if user didn't pass a label, apply a default text
        if grouping_label == None:
            grouping_label = 'Others'
        # group all other rows below the cut-off value
        #all_others = pd.Series(fractions[row_mask].sum())
        #all_others.index = [grouping_label]
        
    # get the color map then pull 1 color from it for each pie wedge we'll draw
    color_map = cm.get_cmap(cm_name)
    num_of_colors = len(fractions)
    colors = color_map([x/float(num_of_colors) for x in range(num_of_colors)])
    
    # create the figure and an axis to plot on
    fig, ax = plt.subplots(figsize=[width, height])
    
    # plot the pie
    wedges = ax.pie(fractions, 
                    labels = labels, 
                    labeldistance = labeldistance,
                    #autopct=autopct,
                    colors = colors,
                    shadow = shadow, 
                    startangle = startangle)
    
    # change the edgecolor for each wedge
    for wedge in wedges[0]:
        wedge.set_edgecolor(edgecolor)
    
    # set the title and show the plot
    ax.set_title(title)
    plt.show()
    
    
##############################################################################

#                  Drop all the Amtrak values in each month 
    

df_march = pd.read_csv('2018_03.csv', index_col = False)
df_march = df_march[df_march['type'] == 'NJ Transit']
df_march = df_march.dropna()

df_april = pd.read_csv('2018_04.csv', index_col = False)
df_april = df_april[df_april['type'] == 'NJ Transit']
df_april = df_april.dropna()

df_may = pd.read_csv('2018_05.csv', index_col = False)
df_may = df_may[df_may['type'] == 'NJ Transit']
df_may = df_may.dropna()

df_june = pd.read_csv('2018_06.csv', index_col = False)
df_june = df_june[df_june['type'] == 'NJ Transit']
df_june = df_june.dropna()

df_july = pd.read_csv('2018_07.csv', index_col = False)
df_july = df_july[df_july['type'] == 'NJ Transit']
df_july = df_july.dropna()

df_august = pd.read_csv('2018_08.csv', index_col = False)
df_august = df_august[df_august['type'] == 'NJ Transit']
df_august = df_august.dropna()

df_september = pd.read_csv('2018_09.csv', index_col = False)
df_september = df_september[df_september['type'] == 'NJ Transit']
df_september = df_september.dropna()

df_october = pd.read_csv('2018_10.csv', index_col = False)
df_october = df_october[df_october['type'] == 'NJ Transit']
df_october = df_october.dropna()

df_november = pd.read_csv('2018_11.csv', index_col = False)
df_november = df_november[df_november['type'] == 'NJ Transit']
df_november = df_november.dropna()

df_december = pd.read_csv('2018_12.csv', index_col = False)
df_december = df_december[df_december['type'] == 'NJ Transit']
df_december = df_december.dropna()

#                    - Group by Train Id and date -

cumu_delay_march = df_march.groupby(['date' , 'train_id']).last()
cumu_delay_april = df_april.groupby(['date' , 'train_id']).last()
cumu_delay_may = df_may.groupby(['date' , 'train_id']).last()
cumu_delay_june = df_june.groupby(['date' , 'train_id']).last()
cumu_delay_july = df_july.groupby(['date' , 'train_id']).last()
cumu_delay_august = df_august.groupby(['date' , 'train_id']).last()
cumu_delay_september = df_september.groupby(['date' , 'train_id']).last()
cumu_delay_october = df_october.groupby(['date' , 'train_id']).last()
cumu_delay_november = df_november.groupby(['date' , 'train_id']).last()
cumu_delay_december = df_december.groupby(['date' , 'train_id']).last()


#             - Counting the  delay minutes from data greater than zero -

delayed_trains_march = cumu_delay_march[(cumu_delay_march['delay_minutes']>0)]
delayed_trains_count_march = delayed_trains_march['delay_minutes'].count()

delayed_trains_april = cumu_delay_april[(cumu_delay_april['delay_minutes']>0)]
delayed_trains_count_april = delayed_trains_april['delay_minutes'].count()

delayed_trains_may = cumu_delay_may[(cumu_delay_may['delay_minutes']>0)]
delayed_trains_count_may = delayed_trains_may['delay_minutes'].count()

delayed_trains_june = cumu_delay_june[(cumu_delay_june['delay_minutes']>0)]
delayed_trains_count_june = delayed_trains_june['delay_minutes'].count()

delayed_trains_july = cumu_delay_july[(cumu_delay_july['delay_minutes']>0)]
delayed_trains_count_july = delayed_trains_july['delay_minutes'].count()

delayed_trains_august = cumu_delay_august[(cumu_delay_august['delay_minutes']>0)]
delayed_trains_count_august = delayed_trains_august['delay_minutes'].count()

delayed_trains_september = cumu_delay_september[(cumu_delay_september['delay_minutes']>0)]
delayed_trains_count_september = delayed_trains_september['delay_minutes'].count()

delayed_trains_october = cumu_delay_october[(cumu_delay_october['delay_minutes']>0)]
delayed_trains_count_october = delayed_trains_october['delay_minutes'].count()

delayed_trains_november = cumu_delay_november[(cumu_delay_november['delay_minutes']>0)]
delayed_trains_count_november = delayed_trains_november['delay_minutes'].count()

delayed_trains_december = cumu_delay_december[(cumu_delay_december['delay_minutes']>0)]
delayed_trains_count_december = delayed_trains_december['delay_minutes'].count()


#                     - Converting the delay minutes into list -


delay_data_per_month = [delayed_trains_count_march , delayed_trains_count_april ,
                        delayed_trains_count_may, delayed_trains_count_june ,
                        delayed_trains_count_july, delayed_trains_count_august , 
                        delayed_trains_count_september,delayed_trains_count_october,
                        delayed_trains_count_november,delayed_trains_count_december]
labels = ['March', 'April' , 'May' , 'June' , 'July' , 'August' , 'September','October',
'November','December']


##############################################################################

#                             - Displays per month delays -

print('\n')
print("The Delayed trains per month is:")
print('\n')
print('Delayed trains in march= ',int(delayed_trains_count_march))
print('Delayed trains in april= ',int(delayed_trains_count_april))
print('Delayed trains in may= ',int(delayed_trains_count_may))
print('Delayed trains in june= ',int(delayed_trains_count_june))
print('Delayed trains in july= ',int(delayed_trains_count_july))
print('Delayed trains in august =',int(delayed_trains_count_august))
print('Delayed trains in september =',int(delayed_trains_count_september))
print('Delayed trains in october= ',int(delayed_trains_count_october))
print('Delayed trains in november= ',int(delayed_trains_count_november))
print('Delayed trains in december= ',int(delayed_trains_count_december))
print('\n')

 #                       - Displays pie chart -
pie_chart(fractions = delay_data_per_month,
          labels = labels,
          title = 'Delay Report Per Month')

##############################################################################
#                          - Displays July delays -

delay_data = [ontime_trains_count_july, delayed_trains_count_july , 
              cancelled_trains_count]
labels = ['OnTime', 'Delayed', 'Cancelled']

print('\n')
print('Pie chart shows July month detailed/ Cancelled/ Ontime data:')
print('\n')
print("Ontime trains in july= ", int(ontime_trains_count_july))
print("Delayed trains in july= ", int(delayed_trains_count_july))
print("Cancelled trains in july= ", int(cancelled_trains_count))
print('\n')


pie_chart(fractions = delay_data,
          labels = labels,
          title = 'July')
print('\n')

##############################################################################
#                   - Status of trains in july - 

print('Graph shows value of status of lines in july')
print('\n')
departed = df_july[df_july['status'] == 'departed'].status.count()
estimated = df_july[df_july['status'] == 'estimated'].status.count()
cancelled = df_july[df_july['status'] == 'cancelled'].status.count()
sum_status = departed+estimated+cancelled
statuses = df_july['status'].value_counts()/sum_status
statuses
print(statuses)

ay = statuses.plot(kind='bar', figsize=[9,4],width=0.6,alpha=0.6,edgecolor='k', grid=False, ylim=[0, 1])

ay.set_xticklabels(statuses.index, rotation=0, rotation_mode='anchor')
ay.yaxis.grid(True)
ay.yaxis.grid(True)
   
ay.set_ylabel('Status Rate')

plt.show()

##############################################################################

#                           - Most Delayed Lines in july - 
#                           - Number of trips for each line - 
error_config = {'ecolor': '0.3'}
lines = df_july.groupby(['train_id']).last()
lines.head(2)

line_usage = lines['line'].value_counts()
line_usage

lines_cumu_delay_july = lines.groupby('line')['delay_minutes'].sum().sort_values(ascending=False)
lines_cumu_delay_july
print('The below data shows the delay in minute for each line in July')
print('\n')
print(lines_cumu_delay_july)

lines_stop_sequence = lines.groupby('line')['stop_sequence'].sum().sort_values(ascending=False)
lines_stop_sequence

print('\n')
print('Number of Trips in each Line And Delay in each line')


ax = line_usage.plot(kind = 'bar', figsize=[9, 4], width = 0.25, position=1 , alpha=0.6, 
                    color='b', edgecolor='k', grid=False, ylim=[0, 225],error_kw=error_config,
                 label='Number of Trips')

ax.set_xticklabels(line_usage.index, rotation=45, rotation_mode='anchor', ha='right')
ax.yaxis.grid(True)
   


ax.set_ylabel('Number of Train records for Each Line',  color='b')
ax.tick_params('y', colors='b')
ax.legend()


ax2 = ax.twinx()

ax2 =lines_cumu_delay_july.plot( kind = 'bar' , figsize=[9, 4], width= 0.25, position = 0, alpha=0.6, 
                    color='r', edgecolor='k', grid=False, ylim=[0, 700] ,error_kw=error_config, 
                 label='Delay (min)')

ax2.set_xticklabels(lines_cumu_delay_july.index, rotation=45, rotation_mode='anchor', ha='right')



ax2.set_ylabel('Delay (min)' , color='r')
ax2.tick_params('y', colors='r')

print('\n')

















