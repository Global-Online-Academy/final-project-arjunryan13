# FINAL PROJECT

This repository is for all of the programs and files needed for your final project.

Include any program files or data files that are needed for your visualizations when submitting to this assignment.

If you are pulling data from an API, please put the data into a file in this repository.

THANK YOU FOR A GREAT SEMESTER! :)

---
# Arjun's Final Project

This project attempts to measure stress levels (or the opposite, calmness) and try to see what triggers a person to be stressed or calm
The dataset that I am using is as follows – I looked into the UC Irvine Machine Learning Repository to get a dataset for my project: WESAD (Wearable Stress and Affect Detection) – which contains data from 15 subjects during a stress-affect lab study while wearing physiological and motion sensors. Philip Schmidt, Attila Reiss, Robert Duerichen, Claus Marberger, and Kristof Van Laerhoven, "Introducing WESAD, a multimodal dataset for Wearable Stress and Affect Detection," ICMI 2018, Boulder, USA, 2018. https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection

![HRV-Chart-300x225](https://github.com/Global-Online-Academy/final-project-arjunryan13/assets/156986193/bca0c5ca-4f3a-49c6-a336-371e630d8b4b)

I created three charts per person (subject) for each of the subjects in the study.

For each person I decided to see:
1. Information about the person - like age weight etc.
2. Heart Rate - the normal range is 60-120 and I left this band white and highlighted peaks and valleys in blue.
3. Temperature in C -  Normal temperature can vary based on age and fitness level. I'm just showing a range between 32.2C and 37.8C as normal. A fever is usually when your body temperature is 37.8°C or higher.
4. Photo-plethysmography - This is a measure the volumetric variations of blood circulation.Detailed analysis of this measure can also help with the timely identification and diagnose of various cardiovascular diseases including atherosclerosis and arterial stiffness. Normal range could vary but I used -600 to 600.

I created a comprehensive view for all subjects. From the chart, we can see that when heart rate goes up, sometimes temperature also goes up indicating perhaps exercise but at other times temperature is normal or goes down possibly indicating stress.


## SPECIAL INSTRUCTIONS FOR API USERS

Add a file named `config.py` and store your API keys in variables within this file. `config.py` has already been added to the `.gitignore` file.

Add an `import config` to the top of your programs in order to use the API key. This will prevent the API key from being published to the web. You can then use the API key in your file by accessing the variable inside the config module, for example `config.my_api_key`.


When using the requests library, you might need to `pip install requests`. If your computer complains about permissions, try installing for the user using `python -m pip install -user requests` on Windows or `pip install --user requests` on Mac.

---

### Tips
- Start the project early!
    - The earlier you start, the more time you have to get help if you run into any 
    problems.
- Test your code. 
    - Find good stopping points to test out bits of code and
    functions even when your program is only partially finished. 
    - Try out different inputs and see if you expect the outputs that you get.
- Ask for help on Twist. 
    - Remember that we are traveling together on this 
    learning journey and you don't have to struggle alone!
    - It is way more important that you get your questions answered than it is
    for you to have a perfectly working program
- Try some [rubber duck debugging](https://rubberduckdebugging.com/).
    - Find a rubber duck, or a pet rock, a stuffed animal, a figurine, a patient dog.
    - Explain your program, line by line, to the victim of your choice.
    - Sometimes this helps you think through your code and how it works, and 
    can help you find bugs and errors in your code.
- DO NOT COPY/PASTE CODE unless otherwise instructed to.
    - The purpose of these exercises is for you to practice your programming skills.
    - You will only harm yourself if you do not make the effort to understand the
    programming concepts we are covering.
    
