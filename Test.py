"""Collin Lloyd CPSC 3600 Project1"""
import statistics
import json
class TestResultContainer:
	"A simple container of results usng a dictionary of lists."
	 
	Numbers = {
		"ThroughPut": [], 
		"RoundTripTime": [], 
		"ConnectionStatus": [],
	}

	def __init__(self):
		"""initialize class"""
		pass
	def pushTPut(TestResultContainer, x):
		"""append to list in throughput key"""
		key = "ThroughPut"
		TestResultContainer.Numbers[key].append(x)
	def pushRTT(TestResultContainer, y):
		"""append to list in RTT key."""
		key = "RoundTripTime"
		TestResultContainer.Numbers[key].append(y)
	def pushCS(TestREsultContainer, z):
		"""append to list in connectstatus key."""
		key = "ConnectionStatus"
		TestResultContainer.Numbers[key].append(z)

	def calcThroughPut(TestResultContainer):
		"""calculate the values in throughput list."""
		key = "ThroughPut"
		Average = 0
		length = 0
		for x in TestResultContainer.Numbers[key]:
			Average = x + Average;
			length += 1
		Average = Average/length
		stDev = statistics.stdev(TestResultContainer.Numbers[key], Average)
		print("ThroughPut average and standard dev is {} and {}." .format(Average, stDev))

	def calcRTT(TestResultContainer):
		"""calculate calues in round trip time key values."""
		key = "RoundTripTime"
		Average = 0
		length = 0
		for x in TestResultContainer.Numbers[key]:
			Average = x + Average
			length += 1
		Average = Average/length
		stDev = statistics.stdev(TestResultContainer.Numbers[key], Average)
		print("Round Trip Time average and standard dev is {} and {}." .format(Average, stDev))

	def calcConnectStat(TestResultContianer):
		"""calc the values of the connectstatus key values."""
		key = "ConnectionStatus"
		Average = 0
		length = 0
		for x in TestResultContainer.Numbers[key]:
			Average = x + Average
			length += 1
		Average = Average/length
		stDev = statistics.stdev(TestResultContainer.Numbers[key], Average)
		print("Connection Status average and standard dev is {} and {}." .format(Average, stDev))

	def write_to_json(TestResultContainer, Numbers):
		with open('results.json', 'w') as fp:
			json.dump(Numbers, fp)
