Python Tutor Data Analysis Project
=============

Python Tutor is a free web based tool created by Phillip Guo located here http://pythontutor.com/. This tool allows a Python Programmer to obtain a visualization of their Python code, and the ability to step through each line to view Python's internal object structure as the code is executed.

The interesting part that we'll be looking at in this project is the fact that this program stores the code a user executes, allowing us at the backend to do some analysis of the code users submit.

For instance each submission to the site is timestamped and ipaddress logged, allowing us to view a history of each users code submissions. For this project we'll have access to JSON encoded records of the information provided to the site.

Project Goals
=============

The first goal of the project will be to find the interesting users code, what we're looking for here are users who submit non working code (either compile or run time errors) and then end up submitting a working version. This will give us view of students as they work through a problem.

1. Development an object model to represent the user and their code submissions.
2.Processing of the JSON data into the object model for further analysis. We'll want to take a look at the data here and try to organize by the ip address to categorize them first. Then for each of these ip addresses we can look at the time stamping to find groupings, we can limit this by denisity of submission. We treat each set of closely related by time stamp submission as a user after this point.
3. Analysis of the objects to determine whether they fit our datapoints or not, and to find out how much of the data actually conforms to the use cases that we're looking for.
4. Running of the code (by VM) on these interesting cases to obtain what errors are being generated.
5. Analyze the structure of the AST in each step the user took (for those segments that actually compile) and see how these trees progress. This could give us some interseting insight into the thought process of the students.

Tools
=============
