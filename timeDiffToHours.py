
#reads arguments from command line and calculates the difference between hour + minute times
#and converts the hour:minute difference to hour.tenths of an hour
#then multiplies it by hourly rate to do a timesheet calcuation
#how to use example
#python3 timeDiffToHours.py 27 10:48am 12:30pm
#<interpreter> <program.py> <hourlyRate> <start time> <end time>
#returns number of inputs
#the parsed hour, minutes, am/pm
#the calcuated hour minute difference
#the hour minute difference in decimal form (hours + minutes / 60)
#the decimal difference multiplied by the hourly rate

import sys #for reading command line arguments


accumTime = 0
accumDollars = 0

numTimePairs = int((len(sys.argv)-1)/2)
hourlyRate = float(sys.argv[1])
print( 'rate: $%.2f num pairs: %i' % (hourlyRate, numTimePairs) )
for i in range(0,numTimePairs):
	if( i != 0 ):
		print( '%.2fhrs $%.2f' % (accumTime, accumDollars) )
	#start time  use the : to seperate the hours, minutes and am/pm
	hM1 = sys.argv[2+i*2].split(':')
	hM1.append( hM1[1][2:] )
	hM1[1] = hM1[1][:2]
	#end time parse parts
	hM2 = sys.argv[2+i*2+1].split(':')
	hM2.append( hM2[1][2:] )
	hM2[1] = hM2[1][:2]

	#if the start time is before noon and the end time after noon
	if( ( hM1[2] == 'AM' or hM1[2] == 'am' ) and 
		( (hM2[2] == 'PM' or hM2[2] == 'pm') and int(hM2[0]) < 12 ) ):
		hM2[0] = int(hM2[0])+12 #convert the end time hours to a 24 hr style number

	#print the hour and minutes input used for calcuation for verification
	print( "\t" + str(hM1) + " " + str(hM2) )

	#calculate difference of hours and minutes
	hDiff = int(hM2[0]) - int(hM1[0])
	mDiff = int(hM2[1]) - int(hM1[1])
	#if the minutes are negative, i.e  30-32 convert 1 hour into minutes and 
	#remove the negative minutes from it
	if( mDiff < 0 ):
		hDiff -= 1
		mDiff = 60 + mDiff
	#print for verifying calculation
	print( '\t' + str(hDiff) + "hrs " + str(mDiff) + "mins" )
	#convert to decimal form
	diff = hDiff + (mDiff/60.0)
	diff = int(diff * 100)/100 #round down to nearest 100th of an hour (2 decimal places)
	accumTime += diff
	#output the calculation of decimal hours * hourly rate
	pairSum = diff * hourlyRate
	print( '\t' + str(diff) + ' $%.2f' % pairSum ) #print result for verification
	accumDollars += pairSum
print("total:")
print( '%.2fhrs $%.2f' % (accumTime, accumDollars) ) 
