#
# This is my final program to display my charts
#
import os
from bokeh.plotting import figure,show,gridplot
from bokeh.models import BoxAnnotation

# Plots is a dictionary of all "subjects" of this study
plots = {}
# Attribs contains Three attribute we are looking for each subject
attribs = ['HR','TEMP','BVP']
# Array of subjects
subjects = ['S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S13','S14','S15','S16','S17']

# This function collects data for one subject
def prepareDataForSubject(subjectName):
    
    # I'm Initialize a nested dictionary
    plots[subjectName] = {}
    # Add information about the subject from the readme file
    plots[subjectName]['info'] = open('WESAD' + os.sep + subjectName + os.sep + subjectName + '_readme.txt', 'r').read()
    # Add medical data information by looping attributes
    for attrib in attribs:
        # Read CSV file and convert it to a list
        with open('WESAD' + os.sep + subjectName + os.sep + subjectName + '_E4_Data' + os.sep + attrib + '.csv') as f:
            plots[subjectName][attrib] = [float(s) for line in f.readlines() for s in line[:-1].split(',')]
        # For Heart Rate, keep all data from second index
        if attrib == 'HR':
            plots[subjectName][attrib]  = plots[subjectName][attrib][2:]
        # For BVP, keep all data from second index till heart index
        if attrib == 'EDA' or attrib == 'BVP':
            plots[subjectName][attrib]  = plots[subjectName][attrib][2:len(plots[subjectName]['HR'])] 
        # For Temperature, keep all data from sixth index till heart index
        if attrib == 'TEMP':
            plots[subjectName][attrib]  = plots[subjectName][attrib][6:len(plots[subjectName]['HR'])] 
        # Now we're populating the index for the x-axis based on data count               
        plots[subjectName][attrib + 'Index'] = []
        for i in range(0,len(plots[subjectName][attrib])):
            plots[subjectName][attrib + 'Index'].append(i)

# Initialize grid plot as a list with 4 properties
gp = [[],[],[],[]]
# Looping through all subjects
for subject in subjects:
    # Preparing data for the current subject
    prepareDataForSubject(subject)
    # Displaying information about the subject
    p0 = figure(title= 'Subject: '+subject + '\n' + '\n'.join(plots[subject]['info'].split('\n')[0:15]), x_axis_label='x', y_axis_label='y', width=300, height=300)
    p0.line([],[],legend_label='Info', line_width=2,line_color='black')  
    
    # Plotting heart rate data
    p1 = figure(title="Heart Rate (White band = normal)", x_axis_label='x', y_axis_label='y', width=300, height=300, background_fill_color='white')
    p1.line(plots[subject]['HRIndex'],plots[subject]['HR'], line_width=2,line_color='red')
    #
    # Adding a box around abnormal heart rates
    # Heart rates between 60 and 120 are normal and the spikes
    # that go beyond are highlighted in blue
    #
    b1 = BoxAnnotation(top=60, fill_alpha=0.2, fill_color='cornflowerblue')
    b2 = BoxAnnotation(bottom=60, top=120, fill_alpha=0.0, fill_color='white')
    b3 = BoxAnnotation(bottom=120, fill_alpha=0.2, fill_color='cornflowerblue')   
    p1.add_layout(b1)
    p1.add_layout(b2)
    p1.add_layout(b3)   

    # Plotting temperature data
    p2 = figure(title="Temperature in C", x_axis_label='x', y_axis_label='y', width=300, height=300)
    p2.line(plots[subject]['TEMPIndex'],plots[subject]['TEMP'],  line_width=2,line_color='green')
    #
    # Adding box around abnormal temperature
    # A fever is usually when your body temperature is 37.8°C or higher.
    # Normal temperature can vary based on age and fitness level
    # I'm just showing a range between 32.2C and 37.8C as normal
    # 
    b1 = BoxAnnotation(top=32.2, fill_alpha=0.2, fill_color='cornflowerblue')
    b2 = BoxAnnotation(bottom=32.2, top=37.8, fill_alpha=0.0, fill_color='white')
    b3 = BoxAnnotation(bottom=37.8, fill_alpha=0.2, fill_color='cornflowerblue')   
    p2.add_layout(b1)
    #p2.add_layout(b2)
    #p2.add_layout(b3)      
    
    # Plotting BVP data
    p3 = figure(title="Photo-plethysmography (circulation)", x_axis_label='x', y_axis_label='y', width=300, height=300,background_fill_color='white')
    p3.line(plots[subject]['BVPIndex'],plots[subject]['BVP'],line_width=2,line_color='blue')
    # 
    # Adding a box around abnormal BVP (which is Photo-plethysmography)
    #
    # Photoplethysmography, known most commonly as PPG, utilizes 
    # an infrared light to measure the volumetric variations
    # of blood circulation. (Thats why the chart is symmetric; 
    # I looked up normal ranges and decided on -600 to +600)
    # 
    # Detailed analysis of this signal can also help with the timely 
    # identification and diagnose of various cardiovascular diseases
    # including atherosclerosis and arterial stiffness.
    #
    b1 = BoxAnnotation(top=-600, fill_alpha=0.2, fill_color='cornflowerblue')
    b2 = BoxAnnotation(bottom=-600, top=600, fill_alpha=0.0, fill_color='white')
    b3 = BoxAnnotation(bottom=600, fill_alpha=0.2, fill_color='cornflowerblue')   
    p3.add_layout(b1)
    p3.add_layout(b2)
    p3.add_layout(b3)    
    
    # Appending the individual plots to a grid plot
    gp[0].append(p0)
    gp[1].append(p1)
    gp[2].append(p2)
    gp[3].append(p3)

# Setting up the grid plot
p = gridplot(gp)

# Displaying the grid plot
show(p)
