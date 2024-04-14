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

I am still thinking about what graphs I should create

I want to visualize all these different pieces of data from 15 different people or “Subjects.”I plan to use only temperature, electrodermal activity, heart rate, and qualitative metrics of how the “Subjects feel. I am mostly thinking of creating a comprehensive view based on a Subject number so that the person running the program can choose the “Subject number.” Another view would be, for example, to see heart rates from all 15 subjects, but I wonder if that's useful.



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
    
