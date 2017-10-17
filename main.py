import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import layout, widgetbox
from bokeh.models.widgets import PreText


file_counter = 0
file_list = ["Test1_noHeader.csv",
            "Test2_noHeader.csv",
            "Test3_noHeader.csv",
            "Test4_noHeader.csv",
            "Test5_noHeader.csv",
            "Test6_noHeader.csv",
            "Test7_noHeader.csv",
            "Test8_noHeader.csv"]

file_notes = ["19k.kv 615mm 205mah",
              "19k.kv 615mm 205mah",
              "19k.kv 615mm 255mah",
              "19k.kv 615mm 255mah",
              "25k.kv 617mm 255mah",
              "18k.kv 615mm 205mah",
              "18k.kv 615mm 205mah",
              "17k.kv 716mm 255mah"]

best_dict = {}
best_data = {}


for filename in file_list:
    file_counter +=1
    first =pd.read_csv(filename)
    output_file("plot_" + str(file_counter) + ".html")

    # second.columns.names=['Marker','Coord']
    # print first
    # print second
    # print "no idea"

    # So the pandas tutorials are garbage. All I want is a new column title, but if I do:
    # second = pd.DataFrame(first.iloc[4:],columns=[first.iloc[1],first.iloc[3]])
    # I get good column labels, but it drops ALL the data. Obviously undesired behaviour.

    # Workaround:
    # df.iloc[1] = Marker
    # df.iloc[3] = X/Y/Z/Frame/Time
    # df.iloc[4:] = data
    # Data at marker:
    # data = df[marker_series[marker_series == marker].index]

    df  = first
    marker_series = df.iloc[1]
    frame = df['Unnamed: 0']
    frame = np.float64(frame.iloc[4:].as_matrix())
    time = df['Unnamed: 1']
    time = np.float64(time.iloc[4:].as_matrix())
    frametime = np.average(np.diff(time))
    framerate = 1.0/frametime

    figure_list = []

    for marker in df.iloc[1].unique():

        if marker is np.NaN:
            continue
        #print marker
        # select the columns where df.marker = marker
        data = df[marker_series[marker_series == marker].index]
        data = np.float64(data.iloc[4:].as_matrix())
        NaNs = np.isnan(data[:,0])
        above_min = data[:,1] > 0.07
        below_max = data[:, 1] < 4.2
        # Split on NaN: any (or all, it should be all or nothing here)
        # look for continuous data that passes through Y: [0.1 : 3] m
        # Add it to a set of valid tracks
        # get velocity, acceleration, plot.
        # Okay, here is the data as x,y,z tuples. I now need to import time as an axis.

        track_list = []

        valid_data = ~NaNs & above_min & below_max
        # Find all start and end indicies that are lengths of real (not NaN) data
        first = None
        second = None
        for i in range(len(valid_data)):
            #First data
            if i == 0:
                if valid_data[i]:
                    first = i
                continue
                # opening segment in middle of data
            if not valid_data[i - 1] and valid_data[i]:
                first = i
                # closing in middle
            if valid_data[i-1] and not valid_data[i]:
                second = i
                #End
            if i == len(valid_data) - 1:
                second = i
            if first is not None and second is not None:
                track_list.append((first, second))
                first = None
                second = None
        #print max(data[:,1])


        for segment in track_list:
            segment_data = data[segment[0]:segment[1],:]
            segment_time = time[segment[0]:segment[1]]
            if max(segment_data[:,1]) < 4 or min(segment_data[:,1]) > 0.5:
                continue
            if segment[1] - segment[0] < 20: # its noise
                continue
            if segment_data[0,1] > 2: # its on the way down
                continue


            v_vel = [0]
            v_vel.extend(np.diff(segment_data[:,1]))
            v_vel = v_vel / frametime # move to metres per second
            v_acc = [0]
            v_acc.extend((np.diff(v_vel)))
            v_acc = np.array(v_acc)
            v_acc = v_acc / (9.6*frametime)

            #vel_at_3m
            for j in range(len(segment_data)):
                if segment_data[j,1] > 3:
                    vel_at_3m = v_vel[j]
                    break
            for k in range(len(segment_data)):
                if v_acc[k] < 0 and segment_data[j,1] > 1:
                    cutoff = segment_data[k,1]
                    break

            p = figure(title=file_notes[file_counter-1] + " Vel@3m: " + str(vel_at_3m) + " m/s Cutoff Alt:" + str(cutoff) + 'm')
            p.line(segment_time,segment_data[:,1],line_color='red',legend="Dis")
            p.line(segment_time, v_vel, line_color='green',legend='Vel')
            p.line(segment_time, v_acc, line_color='blue',legend='Acc')
            p.legend.location = "bottom_right"
            figure_list.append(p)

            # Add to best:
            best = False
            try:
                if vel_at_3m > best_dict[file_notes[file_counter-1]]:
                    best = True
            except KeyError:
                # First!
                best = True
            if best:
                best_dict[file_notes[file_counter - 1]] = vel_at_3m
                #create data dict:
                data_dict = {
                    'time' : segment_time,
                    "dis" : segment_data[:,1],
                    'vel' : v_vel,
                    'acc' : v_acc,
                             }
                best_data[file_notes[file_counter - 1]] = data_dict


    show(layout([figure_list]))


output_file("summary.html")
p_dis = figure(title="Altitude Plots", x_axis_label='Time (seconds)', y_axis_label='Altitude (metres)',)
p_vel = figure(title="Velocity Plots", x_axis_label='Time (seconds)', y_axis_label='Vertical Speed (m/s)',)
plot_colors = ['#1f77b4',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf']
color_idx = 0
for key, data_dict in best_data.iteritems():
    time = data_dict['time']
    time -= time[0]
    p_dis.line(time,data_dict['dis'],legend=key,line_color=plot_colors[color_idx])
    p_vel.line(time,data_dict['vel'],legend=key,line_color=plot_colors[color_idx])
    color_idx +=1
p_vel.legend.location = "bottom_right"
p_dis.legend.location = "bottom_right"

label_str = "Best Velocity at 3m Altitude:\r\n"
for key, value in best_dict.iteritems():
    label_str += str(key) + ': ' + str(value) + " m/s \r\n"
summary_box = PreText(text=label_str)

show(layout([[p_vel,p_dis],[widgetbox(summary_box, width=800)]]))

ideas = None



