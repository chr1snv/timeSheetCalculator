Getting paid hourly though not getting paid time to generate time sheets or invoices?
is converting between hours and minutes and am / pm complex?
wish there was a well explained method to do it quickly?
Then look no further! command line time sheet calculator is here!

it converts am/pm time to 24 hour format
subtracts hours and minutes ( carrying over an hour if neccessary )
then divides minutes by /60 and adds them to hours to get a decimal number
then multiplys by the hourly rate
and prints the result and accumulated sum so the results can be verified

Here is an example of using it:
======Input:========
python3 timeDiffToHours.py 27 10:48am 12:30am   9:31am 10:40am   8:52am 9:26am

=====Result/Output:========
rate: $27.00 num pairs: 3
	['10', '48', 'am'] ['12', '30', 'am']
	1hrs 42mins
	1.7 $45.90
1.70hrs $45.90
	['9', '31', 'am'] ['10', '40', 'am']
	1hrs 9mins
	1.14 $30.78
2.84hrs $76.68
	['8', '52', 'am'] ['9', '26', 'am']
	0hrs 34mins
	0.56 $15.12
total:
3.40hrs $91.80

Simple, command line based. Less than 50 lines of commented code
No Frills, testable, verifiable solution.
Time Sheet Calculator .py
