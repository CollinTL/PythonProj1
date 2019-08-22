"""Collin Lloyd CPSC 3600 Project1"""
from Test import TestResultContainer
resultCounter = 0
while True:
	"""Looping through to get input from user."""
	if resultCounter == 0:
		Results = TestResultContainer()
	try:
		"""Have to start with try incase user wants out of loop."""
		thPut = input("What is the throughput?")
		throughPut = float(thPut)
		if throughPut < 0:
			print("Cannot enter negative number, try again.")
			resultCounter = 0
			continue
		elif not isinstance(throughPut, float):
			print("Not a float, try again.")
			resultCounter = 0
			continue
		Results.pushTPut(throughPut)
		rtt = input("What is the Round Trip Time?")
		roundTrip = float(rtt)
		if roundTrip < 0:
			print("Cannot enter a negative number, restart.")
			resultCounter = 0
			continue
		elif not isinstance(roundTrip, float):
			print("Not a float, restart.")
			resultCounter = 0
			continue
		Results.pushRTT(roundTrip)
		ConSt = input("What is the Connection Status?")
		connectStatus = float(ConSt)
		if connectStatus < 0:
			print("Cannot enter a negative number, restart.")
			resultCounter = 0
			continue
		elif not isinstance(connectStatus, float):
			print("Not a float, restart.")
			resultCounter = 0
			continue
		Results.pushCS(connectStatus)

		resultCounter += 1

	except KeyboardInterrupt:
		"""For user to get out of loop using CTRL+C."""
		print()
		print("You added {} results." .format(resultCounter))
		break

"""While loop is over, calculate values from class with calls to functions."""
Results.calcThroughPut()
Results.calcRTT()
Results.calcConnectStat()

Results.write_to_json(Results.Numbers)
