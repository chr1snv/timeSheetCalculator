Getting paid hourly though not getting paid time to generate time sheets or invoices?<br/>
is converting between hours and minutes and am / pm complex?<br/>
wish there was a well explained method to do it quickly?<br/>
Then look no further! command line time sheet calculator is here!<br/>
<br/>
it converts am/pm time to 24 hour format<br/>
subtracts hours and minutes ( carrying over an hour if neccessary )<br/>
then divides minutes by /60 and adds them to hours to get a decimal number<br/>
then multiplys by the hourly rate<br/>
and prints the result and accumulated sum so the results can be verified<br/>
<br/>
Here is an example of using it:<br/>
======Input:========<br/>
python3 timeDiffToHours.py 27 10:48am 12:30am   9:31am 10:40am   8:52am 9:26am<br/>
<br/>
=====Result/Output:========<br/>
rate: $27.00 num pairs: 3<br/>
	['10', '48', 'am'] ['12', '30', 'am']<br/>
	1hrs 42mins<br/>
	1.7 $45.90<br/>
1.70hrs $45.90<br/>
	['9', '31', 'am'] ['10', '40', 'am']<br/>
	1hrs 9mins<br/>
	1.14 $30.78<br/>
2.84hrs $76.68<br/>
	['8', '52', 'am'] ['9', '26', 'am']<br/>
	0hrs 34mins<br/>
	0.56 $15.12<br/>
total:<br/>
3.40hrs $91.80<br/>
<br/>
Simple, command line based. Less than 50 lines of commented code<br/>
No Frills, testable, verifiable solution.<br/>
Time Sheet Calculator .py<br/>
