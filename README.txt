Collin Lloyd
Project 1 "Intro to Python"

So, my design was for main to get in data from a user through a while loop while have a try except clause to check if the user entered CTRL+C to stop
the intake of data. The while loop would check if the data would be valid and the push it into the classes dictionary using the correct key. 3 
different functions were created for pushing data into a value. 3 functions representing the 3 keys. The dictionary has a key and the values are 
lists to store multiple values. The push functions main would call would append the value of the user into the list of the key. 3 more functions were
made for the calculation of each key(input). One for throughput one for RTT and one for connectstatus. I know of some flaws i wasnt too sure how to 
fix. When a wrong value is entered, the program prompts the user to restart all the way to the beginning. So the creation of a new class object could
use up a lot of memory that isnt necesarry. The assumption is that the user will enter values correctly without messing up. Another one is that the 
format of the output is really lengthy. More of OCD thing than a flaw. Another flaw is exciting the while loop too early could possibly mess wth the 
values.

Evaluation 1
You added 3 results.
ThroughPut average and standard dev is 3.8333333333333335 and 1.5044378795195679.
Round Trip Time average and standard dev is 11.033333333333333 and 1.0016652800877812.
Connection Status average and standard dev is 25.599999999999998 and 1.682260384126072.

Evaluation 2
you added 6 results.
ThroughPut average and standard dev is 3.7550000000000003 and 1.0342871941583731.
Round Trip Time average and standard dev is 14.325000000000003 and 4.39383090252686.
Connection Status average and standard dev is 20.691666666666666 and 5.822062921908923.
