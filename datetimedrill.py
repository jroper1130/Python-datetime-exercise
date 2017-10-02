'''
Python Drill: PyDrill_Datetime_27_idle
Title: Datetime – Python 2.7 – IDLE
Scenario: The company you work for just opened two new branches. One is in New York City,
the other in London. They need a very simple program to find out if the branches are open or
closed based on the current time of the Headquarters here in Portland. The hours of both
branches are 9:00AM - 9:00PM in their own time zone.
What is asked of you:
Create code that will use the current time of the Portland HQ to find out the time in the NYC &
London branches, then compare that time with the branches hours to see if they are open or
closed.
Print out if each of the two branches are open or closed.
====================================================================================================
'''
#drill4
import datetime

portland = datetime.datetime.now()
london = datetime.datetime.now().hour+8
newyork = datetime.datetime.now().hour+3


if 21 > london and london >= 9:
    print('open')
else:
    print('closed')

if 21 > newyork and newyork >= 9:
    print('open')
else:
    print('closed')







