Python Tutor Data Analysis Project
=============

Python Tutor is a free web based tool created by Phillip Guo located here http://pythontutor.com/. This tool allows a Python Programmer to obtain a visualization of their Python code, and the ability to step through each line to view Python's internal object structure as the code is executed.

The interesting part that we'll be looking at in this project is the fact that this program stores the code a user executes, allowing us at the backend to do some analysis of the code users submit.

For instance each submission to the site is timestamped and ipaddress logged, allowing us to view a history of each users code submissions. For this project we'll have access to JSON encoded records of the information provided to the site.

Scope of Project
=============

The first goal of the project will be to find the interesting datapoints, what we're looking for here are users who submit non working code (either compile or run time errors) and then end up submitting a working version. This will give us view of students as they work through a problem.

- Need to develop an object model to represent the user and their code submissions.
- Processing of the JSON data into the object model for further analysis.
- Analysis of the objects to determine whether they fit our datapoints or not, and to find out how much of the data actually conforms to this use case.


The second goal of the project will be to undertake some visualization of these users, we'd like to integrate UbiView to view the AST for compilable code, possibly being able to step through each of the steps the user took to generate working code.
