Python Tutor Data Analysis Project
Post 1 - Raw Data Analysis
=============

For the initial stage of the analysis project for the Python Tutor data we went and did some basic
statistical analysis of the raw data. In addition we were able to come up with some statistics
on the types of compiler errors in the submitted code.

In order to do this cleanly, we made use of a product called GraphLab, which can be found at www.graphlab.com. This
software package has a very clean Python API, and can read data directly from JSON. This gave us a very clean, and quick
way to get right to doing analysis on the data.

Data
=============

The first step in analyzing any data is to take a look at the format of the data, and what fields are contained in it.
Python Data came to us in the form of 'submissions' encoded in JSON format. An example of one such record is shown below.

```
JSON Sample
{
	"ip": "75.147.182.5", 
	"dt": "2014-07-01 00:00:02", 
	"py": 2, 
	"user_script": "def odd(x):\n  \n   x%2 != 0\n   return True\n   else\n   return False\n\nodd(10)"
}
```

Every time a user presses the `submit` button through the python tutor one of these records is generated. You can
see that we have access to the IP Address of the user, the date and time of submission, what version of Python they
are writing code for, and the actual code the user is attempting to run.

One thing we can notice here is that we can 'localize' a user by the IP Address, but because of shared usage this may
not be enough, so we may also be able to make use of the actual date and time to bind a user to a 'time slice'. 

Having the Python version and the code allows us to execute the code on the appropriate interpreter, which has the potential to allow us to make inferences as to errors, and what a user does when encountered with errors.

Basic Statistics
=============

- How did we get the statistics

- How many IP's (and how many submissions for each?)
- distribution of versions

Error Statistics
=============

- How did we get the errors (python code samples)

- actual statistics found (split up into both Python versions)
