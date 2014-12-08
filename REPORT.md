Python Tutor Data Analysis Project
=============

Python Tutor is a free web based tool created by Phillip Guo located here http://pythontutor.com/. This tool allows a Python Programmer to obtain a visualization of their Python code, and the ability to step through each line to view Python's internal object structure as the code is executed.

The interesting part that we'll be looking at in this project is the fact that this program stores the code a user executes, allowing us at the backend to do some analysis of the code users submit.

For instance each submission to the site is timestamped and ipaddress logged, allowing us to view a history of each users code submissions. For this project we'll have access to JSON encoded records of the information provided to the site.

Python tutor submissions are stored in JSON format, one example of this is below.

```
JSON Sample
{
	"ip": "75.147.182.5", 
	"dt": "2014-07-01 00:00:02", 
	"py": 2, 
	"user_script": "def odd(x):\n  \n   x%2 != 0\n   return True\n   else\n   return False\n\nodd(10)"
}
```


Problem Statement
=============

The Nature and Scale of the Python Tutor Data gives us many potential problems to look at. Since we have so much data from so many different users there are many problems that can be looked at.

- One problem we can approach is to use this data to get at an analysis of programmer mistakes made by novice programers. Can we see interesting or frequent mistakes that new programmers make when writing Python code?

Getting at a solution to the above problem is an extensive task, quite a bit larger than the scope of this courses project. However in the spirit of that overall goal we identified several smaller problems we can get a handle on in the time we had that will help in furthering that goal.

- What type of data model or storage system works well for further analysis of the data?
- Is there a good way to visualize the data, in such a way where we can ask for further 'expert' input into the data for use in
further analysis?
- How to best separate the submissions into a 'session' so we can identify a specific 'user' in analysis of the data.
- What are the basic statistics of the data, how many error types are there, how many 'sessions' can we see in a typical month of submissions?

Why is this interesting?
=============

Analysis of novice programmer mistakes has many facets to it. 

- A large aspect of this analysis is by loookig at mistakes that are common for programmers we can help direct education and training.
- We can also look at the usefulness of compile and runtime errors messages in a language and see how often the programmer makes the appropriate correction.

In addition to the larger problem, the smallers problems are also interseting to look at.

- We can do a review of various tools and database systems that are currently available to do this type of work.
- There is interest for us as a team in exploring Python as a data analysis and web tool.
- Exploration of best methods for visualizing code for an external user.
- Getting at the statistics of the data as it currently stands gives us insight in how to proceed with the larger project goal, and how much useful information is contained in the submissions.

Limitations of Existing Methods
=============

Before engaging in this project we did a quick review of some literature on the subject, much of it at this point older but still enlightening.

One example that illustrates how some of this research was done in the past is out of the International Journal of Human-Computer Studies `Novice Programmer Errors:Language Constructs and Plan Composition` from 1994. In this study the authors looked at 80 students enrolled in introductory level programming classes split into groups of 20. Each group was enrolled in a different class in 4 different languages (C, Fortran, Pascal, and Lisp).[1] This study looked at two faces of programming:

- Plan Composition - Measuring the understanding of problem solving, such as how two parts of a problem can be composed to solve the whole.
- Language Constructs - Measuring the understanding of a languages semantics and syntax.

There are some limitations to this approach. 

- For one the small sample size may hide certain trends in programmer errors. 
- In addition the methods used relied on manual analysis of the code submission and interview of students, which creates a lot of bookkeeping and a large amount of time to do. 
- Lastly this study focused on only a small number of programming assignments, limiting the variation.

Improvements
=============

By using the vast amount of Python Tutor data in future analysis we can 
What are your results so far that show the solution works well


