import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime as dt
import plotly.figure_factory as ff
import plotly
from matplotlib.dates import DateFormatter
import plotly.express as px

day = 3

gantt_file1 = 'SEP_Results/Day/Gantt_compare1' + str(day) + '.png'
gantt_file2 = 'SEP_Results/Day/Gantt_compare2' + str(day) + '.png'
gantt_file3 = 'SEP_Results/Day/Gantt_compare3' + str(day) + '.png'

# load a1 attack file
action_a1_path = 'SEP_Results/Day/Attack_summary_a1' + str(day) + '.txt'
action_a1_coord = open(action_a1_path, "r")
count_a1_coord = 0
# for loop to count the number of lines in file
for line in action_a1_coord:
    if line != "\n":
        count_a1_coord += 1
action_a1_coord.close()
print(count_a1_coord)
# load data line by line
action_a1_coord = open(action_a1_path, "r")
content_a1_coord = action_a1_coord.read()
lines_a1_coord = content_a1_coord.split('\n')

# load a2 attack file
action_a2_path = 'SEP_Results/Day/Attack_summary_a2' + str(day) + '.txt'
action_a2_coord = open(action_a2_path, "r")
count_a2_coord = 0
# for loop to count the number of lines in file
for line in action_a2_coord:
    if line != "\n":
        count_a2_coord += 1
action_a2_coord.close()
print(count_a2_coord)
# load data line by line
action_a2_coord = open(action_a2_path, "r")
content_a2_coord = action_a2_coord.read()
lines_a2_coord = content_a2_coord.split('\n')

# load a3 attack files
action_a3_path = 'SEP_Results/Day/Attack_summary_a3' + str(day) + '.txt'
action_a3_coord = open(action_a3_path, "r")
count_a3_coord = 0
# for loop to count the number of lines in file
for line in action_a3_coord:
    if line != "\n":
        count_a3_coord += 1
action_a3_coord.close()
print(count_a3_coord)
# load data line by line
action_a3_coord = open(action_a3_path, "r")
content_a3_coord = action_a3_coord.read()
lines_a3_coord = content_a3_coord.split('\n')

# load of attacks summary information
attack_path = 'SEP_Results/Day/Argumentation' + str(day) + '.txt'
attack_coord = open(attack_path, "r")
count_attack_coord = 0
# for loop to count the number of lines in file
for line in attack_coord:
    if line != "\n":
        count_attack_coord += 1
attack_coord.close()
print(count_attack_coord)
# load data line by line
attack_coord = open(attack_path, "r")
attack_cp_coord = attack_coord.read()
lines_attack_coord = attack_cp_coord.split('\n')

a1_attack = []
for i in range(1, count_a1_coord):
    a1_data = lines_a1_coord[i].split()

    start_time = int(a1_data[1])
    end_time = start_time + 5
    if a1_data[3] == '-' and a1_data[5] == 'Exceeded':
        Status = 'a\u2081_Infeasible'
        # Status = 'Image_taking_Infeasible'
        memory_final_a1 = a1_data[7]
        final_objective_a1 = a1_data[8]
    elif a1_data[3] == '-' and a1_data[5] == 'Not_exceeded' and a1_data[9] == 'Feasible_better_objective':
        memory_final_a1 = a1_data[7]
        final_objective_a1 = a1_data[8]
        Status = 'a\u2081_FBO'
        # Status = 'Image_taking_Feasible<br>better_objective'
        # used to print objective value
        #Status = 'Image_taking Feasible<br> better objective<br>obj- '+final_objective_a1

    elif a1_data[3] == '-' and a1_data[5] == 'Not_exceeded' and a1_data[9] == 'Feasible_worse_objective':
        memory_final_a1 = a1_data[7]
        final_objective_a1 = a1_data[8]
        Status = 'a\u2081_FWO'
        # Status = 'Image_taking_Feasible<br>worse_objective'
        #Status = 'Image_taking Feasible<br> worse objective<br>obj- '+final_objective_a1

    else:
        Status = 'a\u2081_no_attack'
        memory_final_a1 = 0
        final_objective_a1 = 0

    a1_attack.append([(dt.timedelta(seconds=(int(start_time)))), (dt.timedelta(seconds=(int(end_time)))), Status, memory_final_a1, final_objective_a1])
    #print((dt.timedelta(seconds=(int(start_time)))))

dc = pd.DataFrame({'Task': [(a1_attack[i][2]) for i in range(0, len(a1_attack))], 'Start': ['1970-01-01 ' + str(a1_attack[i][0]) for i in range(0, len(a1_attack))],
                   'Finish': ['1970-01-01 ' + str(a1_attack[i][1]) for i in range(0, len(a1_attack))], 'Resource': [(a1_attack[i][2]) for i in range(0, len(a1_attack))]})


a2_attack = []
for i in range(1, count_a2_coord):
    a2_data = lines_a2_coord[i].split()

    start_time = int(a2_data[1])
    end_time = start_time + 5
    if a2_data[3] == '-' and a2_data[5] == 'Exceeded':
        Status = 'a\u2082_Infeasible'
        # Status = 'Process_Infeasible'
        memory_final_a2 = a2_data[7]
        final_objective_a2 = a2_data[8]
    elif a2_data[3] == '-' and a2_data[5] == 'Not_exceeded' and a2_data[9] == 'Feasible_better_objective':
        memory_final_a2 = a2_data[7]
        final_objective_a2 = a2_data[8]
        Status = 'a\u2082_FBO'
        # Status = 'Process_Feasible<br>better_objective'

    elif a2_data[3] == '-' and a2_data[5] == 'Not_exceeded' and a2_data[9] == 'Feasible_worse_objective':
        memory_final_a2 = a2_data[7]
        final_objective_a2 = a2_data[8]
        Status = 'a\u2082_FWO'
        # Status = 'Process_Feasible<br>worse_objective'

    else:
        Status = 'a\u2082_no_attack'
        memory_final_a2 = 0
        final_objective_a2 = 0

    a2_attack.append([(dt.timedelta(seconds=(int(start_time)))), (dt.timedelta(seconds=(int(end_time)))), Status, memory_final_a2, final_objective_a2])
    #print((dt.timedelta(seconds=(int(start_time)))))

dl = pd.DataFrame({'Task': [(a2_attack[i][2]) for i in range(0, len(a2_attack))], 'Start': ['1970-01-01 ' + str(a2_attack[i][0]) for i in range(0, len(a2_attack))],
                   'Finish': ['1970-01-01 ' + str(a2_attack[i][1]) for i in range(0, len(a2_attack))], 'Resource': [(a2_attack[i][2]) for i in range(0, len(a2_attack))]})



a3_attack = []
for i in range(1, count_a3_coord):
    a3_data = lines_a3_coord[i].split()
    #print(int(a3_data[1]))
    start_time = int(a3_data[1])
    end_time = start_time + 5
    if a3_data[3] == '-' and a3_data[5] == 'Exceeded':
        memory_final_a3 = a3_data[7]
        final_objective_a3 = a3_data[8]
        Status = 'a\u2083_Infeasible'
        # Status = 'Down-linking_Infeasible'
    elif a3_data[3] == '-' and a3_data[5] == 'Not_exceeded' and a3_data[9] == 'Feasible_better_objective':
        memory_final_a3 = a3_data[7]
        final_objective_a3 = a3_data[8]
        Status = 'a\u2083_FBO'
        # Status = 'Down-linking_Feasible<br>better_objective'
        #Status = 'Down-linking Feasible<br> better objective<br>obj- '+final_objective_a3
    elif a3_data[3] == '-' and a3_data[5] == 'Not_exceeded' and a3_data[9] == 'Feasible_worse_objective':
        memory_final_a3 = a3_data[7]
        final_objective_a3 = a3_data[8]
        Status = 'a\u2083_FWO'
        # Status = 'Down-linking_Feasible<br>worse_objective'
        #Status = 'Down-linking_Feasible<br> worse objective<br>obj- '+final_objective_a3
    else:
        Status = 'a\u2083_no_attack'
        memory_final_a3 = 0
        final_objective_a3 = 0

    a3_attack.append([(dt.timedelta(seconds=(int(start_time)))), (dt.timedelta(seconds=(int(end_time)))), Status, memory_final_a3, final_objective_a3])
    #print((dt.timedelta(seconds=(int(start_time)))))
a3_attack.append([(dt.timedelta(seconds=(int(0)))), (dt.timedelta(seconds=(int(0)))), 'a\u2083_FWO', 0, 0])
a3_attack.append([(dt.timedelta(seconds=(int(0)))), (dt.timedelta(seconds=(int(0)))), 'a\u2083_Infeasible', 0, 0])
dj = pd.DataFrame({'Task': [(a3_attack[i][2]) for i in range(0, len(a3_attack))], 'Start': ['1970-01-01 ' + str(a3_attack[i][0]) for i in range(0, len(a3_attack))],
                   'Finish': ['1970-01-01 ' + str(a3_attack[i][1]) for i in range(0, len(a3_attack))], 'Resource': [(a3_attack[i][2]) for i in range(0, len(a3_attack))]})



attack_summary = []
#for i in range(1, count_attack_coord):
for i in range(15000, count_attack_coord-800):
    all_data = lines_attack_coord[i].split()
    #a2_data = lines_a2_coord[i].split()

    start_time = int(all_data[0])
    end_time = start_time + 5
    S = all_data[4]
    if S == '0':
        Status = 'Take'#_Images'
    elif S == '1':
        Status = 'Process'#_Images'
    elif S == '2':
        Status = 'Down-link'#_Images'
    else:
        Status ='Idle'

    # if start_time == int(a2_data[1]):
    #     a2_start_time = int(a2_data[1])
    #     end_time = start_time + 5
    #     if a2_data[3] == '-' and a2_data[5] == 'Exceeded':
    #         Status = 'Process_Infeasible'
    #     elif a2_data[3] == '-' and a2_data[5] == 'Not_exceeded':
    #         Status = 'a2_Feasible'
    #     else:
    #         Status = 'a2_no_attack'
    attack_summary.append([(dt.timedelta(seconds=(int(start_time)))), (dt.timedelta(seconds=(int(end_time)))), Status,S])
    #print((dt.timedelta(seconds=(int(start_time)))))

df = pd.DataFrame({'Task': ['Schedule' for i in range(0, len(attack_summary))], 'Start': ['1970-01-01 ' + str(attack_summary[i][0]) for i in range(0, len(attack_summary))],
                   'Finish': ['1970-01-01 ' + str(attack_summary[i][1]) for i in range(0, len(attack_summary))], 'Resource': [(attack_summary[i][2]) for i in range(0, len(attack_summary))]})#,'Schedule': ['Schedule' for i in range(0, len(attack_summary))]})


# df = pd.DataFrame({'Task': ['Job_%i' for i in range(0, len(attack_summary))], 'Start': ['1970-01-01 ' + str(attack_summary[i][0]) for i in range(0, len(attack_summary))],
#                    'Finish': ['1970-01-01 ' + str(attack_summary[i][1]) for i in range(0, len(attack_summary))], 'Resource': [(attack_summary[i][2]) for i in range(0, len(attack_summary))]})

# color = ['#000ff','#1e90ff','#6495ed','#00bff','#87cefa','#add8e6','#b0e0e6','#afeeee','#e0ffff','#00ffff','#40e0d0']
#
# fig = ff.create_gantt(df, colors=color, index_col='Resource',
#                       show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True, group_tasks=True)

# plot for action 1
# matches=[]
# matches2 =[]
# for i in range(0,len(a1_attack)):
#     #print((a1_attack[i][2]))
#     if 'Image_taking Feasible<br> better' in  a1_attack[i][2]:
#         matches.append(a1_attack[i][2])
#     elif 'Image_taking Feasible<br> worse' in  a1_attack[i][2]:
#         matches2.append(a1_attack[i][2])
#
# #print(matches[0])
#         #print(a3_attack[i][2])
# #print(matches)
# DN_FW_O = matches[0]
# DN_FW_1 = matches2[0]

df2 = pd.concat([df.sort_values('Resource', ascending=True), dc.sort_values('Resource', ascending=True)])# df.sort_values('Resource', ascending=True), dc.sort_values('Resource', ascending=True), dl.sort_values('Resource', ascending=True), dj.sort_values('Resource', ascending=True)])

discrete_map_resource = { 'Take': '#FF6103', 'Process': '#FFD700', 'Down-link': '#0000EE', 'Idle': '#000000', 'a\u2081_FWO': '#8B4513', 'a\u2081_Infeasible': '#FF0000','a\u2081_FBO': '#008000'}#, 'AAW': '#fb9f3a'}

# discrete_map_resource = { 'Take_Images': '#FF6103', 'Process_Images': '#FFD700', 'Down-link_Images': '#0000EE', 'Idle': '#000000', 'Image_taking_Feasible<br>worse_objective': '#8B4513', 'Image_taking_Infeasible': '#FF0000','Image_taking_Feasible<br>better_objective': '#008000'}#, 'AAW': '#fb9f3a'}

fig1 = px.timeline(df2, x_start="Start", x_end="Finish", y="Resource", color="Resource",color_discrete_map=discrete_map_resource, hover_name="Task", color_discrete_sequence=px.colors.qualitative.Prism, opacity=.7, range_x=None, range_y=None,
                        template='plotly_white', height=1200, title="<b>Day</b>" + str(day))

fig1.update_layout(bargap=0.5, bargroupgap=0.1, xaxis_range=[df.Start.min(), df.Finish.max()],
                   xaxis=dict(showgrid=True,gridcolor ='rgb(0,0,0)', side="bottom", tickmode='array', dtick="M1", tickformat="'%H:%M' \n", ticklabelmode="period", ticks="outside", tickson="boundaries", tickwidth=.1, ticklen=20,
                              tickfont=dict(family='Arial', size=40, color='black'), ),
                   yaxis=dict(title="", automargin=True, ticklen=5, showgrid=True,gridcolor ='rgb(0,0,0)', showticklabels=True, tickfont=dict(family="Arial", size=50, color='black')),
                   legend=dict(orientation="h", yanchor="bottom", y=1, title="", xanchor="right", x=.9, font=dict(family="Arial", size=40, color="black")),
                   title = dict(font=dict(family="Arial", size=50, color="black")))


fig1.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=0.2, opacity=1)

#plotly.offline.plot(fig1, filename=gantt_file)
fig1.write_image(file = gantt_file1, format='png', scale=1, width=1800, height=800)
#fig1.show()


# plot for action 2
# matches=[]
# matches2 =[]
# for i in range(0,len(a2_attack)):
#     print((a2_attack[i][2]))
#     if 'Process Feasible<br> better' in  a2_attack[i][2]:
#         matches.append(a2_attack[i][2])
#     elif 'Process Feasible<br> worse' in  a2_attack[i][2]:
#         matches2.append(a2_attack[i][2])
#
# #print(matches[0])
#         #print(a3_attack[i][2])
# print(matches)
# DN_FW_O = matches[0]
# DN_FW_1 = matches2[0]

df2 = pd.concat([df.sort_values('Resource', ascending=True), dl.sort_values('Resource', ascending=True)])# df.sort_values('Resource', ascending=True), dc.sort_values('Resource', ascending=True), dl.sort_values('Resource', ascending=True), dj.sort_values('Resource', ascending=True)])


discrete_map_resource = {  'Take': '#FF6103', 'Process': '#FFD700', 'Down-link': '#0000EE', 'Idle': '#000000', 'a\u2082_FWO': '#8B4513', 'a\u2082_Infeasible': '#FF0000', 'a\u2082_FBO': '#008000'}#, 'AAW': '#fb9f3a'}

# discrete_map_resource = {  'Take_Images': '#FF6103', 'Process_Images': '#FFD700', 'Down-link_Images': '#0000EE', 'Idle': '#000000', 'Process_Feasible<br>worse_objective': '#8B4513', 'Process_Infeasible': '#FF0000', 'Process_Feasible<br>better_objective': '#008000'}#, 'AAW': '#fb9f3a'}

fig1 = px.timeline(df2, x_start="Start", x_end="Finish", y="Resource", color="Resource",color_discrete_map=discrete_map_resource, hover_name="Task", color_discrete_sequence=px.colors.qualitative.Prism, opacity=.7, range_x=None, range_y=None,
                        template='plotly_white', height=1200, title="<b>Day</b>" + str(day))

fig1.update_layout(bargap=0.5, bargroupgap=0.1, xaxis_range=[df.Start.min(), df.Finish.max()],
                   xaxis=dict(showgrid=True, gridcolor ='rgb(0,0,0)',  side="bottom", tickmode='array', dtick="M1", tickformat="'%H:%M' \n", ticklabelmode="period", ticks="outside", tickson="boundaries", tickwidth=.1, ticklen=20,
                              tickfont=dict(family='Arial', size=50, color='black'), ),
                   yaxis=dict(title="", automargin=True, ticklen=5, showgrid=True,gridcolor ='rgb(0,0,0)', showticklabels=True, tickfont=dict(family="Arial", size=50, color='black')),
                   legend=dict(orientation="h", yanchor="bottom", y=1.05, title="", xanchor="right", x=0.95, font=dict(family="Arial", size=43, color="black")),
                   title=dict(font=dict(family="Arial", size=50, color="black")))

fig1.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=0.2, opacity=1)

# plotly.offline.plot(fig1, filename=gantt_file)
fig1.write_image(file=gantt_file2, format='png', scale=1, width=1800, height=800)

# plot for action 3
df2 = pd.concat([df.sort_values('Resource', ascending=True), dj.sort_values('Resource', ascending=True)])# df.sort_values('Resource', ascending=True), dc.sort_values('Resource', ascending=True), dl.sort_values('Resource', ascending=True), dj.sort_values('Resource', ascending=True)])


# matches=[]
# matches2 =[]
# for i in range(0,len(a3_attack[0])):
#     if 'Down-linking Feasible<br> better' in  a3_attack[0][2]:
#         matches.append(a3_attack[0][i])
#     elif 'Down-linking Feasible<br> worse' in  a3_attack[0][2]:
#         matches2.append(a3_attack[0][i])
#         #print(a3_attack[i][2])
# #print(matches)
# DN_FW_O = matches[2]
# #DN_FW_1 = matches2[2]


discrete_map_resource = { 'Take': '#FF6103', 'Process': '#FFD700', 'Down-link': '#0000EE', 'Idle': '#000000','a\u2083_FWO': '#8B4513', 'a\u2083_Infeasible': '#FF0000', 'a\u2083_FBO': '#008000'}#, 'AAW': '#fb9f3a'}

# discrete_map_resource = { 'Take_Images': '#FF6103', 'Process_Images': '#FFD700', 'Down-link_Images': '#0000EE', 'Idle': '#000000','Down-linking_Feasible<br>worse_objective': '#8B4513', 'Down-linking_Infeasible': '#FF0000', 'Down-linking_Feasible<br>better_objective': '#008000'}#, 'AAW': '#fb9f3a'}

fig1 = px.timeline(df2, x_start="Start", x_end="Finish", y="Resource", color="Resource",color_discrete_map=discrete_map_resource, hover_name="Task", color_discrete_sequence=px.colors.qualitative.Prism, opacity=.7, range_x=None, range_y=None,
                        template='plotly_white', height=1200, title="<b>Day</b>" + str(day))

fig1.update_layout(bargap=0.5, bargroupgap=0.1, xaxis_range=[df.Start.min(), df.Finish.max()],
                   xaxis=dict(showgrid=True,gridcolor ='rgb(0,0,0)', side="bottom", tickmode='array', dtick="M1", tickformat="'%H:%M' \n", ticklabelmode="period", ticks="outside", tickson="boundaries", tickwidth=.1, ticklen=20,
                              tickfont=dict(family='Arial', size=40, color='black'), ),
                   yaxis=dict(title="", automargin=True, ticklen=5, showgrid=True,gridcolor ='rgb(0,0,0)', showticklabels=True, tickfont=dict(family="Arial", size=50, color='black')),
                   legend=dict(orientation="h", yanchor="bottom", y=1, title="", xanchor="right", x=.9, font=dict(family="Arial", size=40, color="black")),
                   title=dict(font=dict(family="Arial", size=50, color="black")))

fig1.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=0.2, opacity=1)

# plotly.offline.plot(fig1, filename=gantt_file)
fig1.write_image(file=gantt_file3, format='png', scale=1, width=1800, height=800)