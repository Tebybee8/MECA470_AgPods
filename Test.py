try:
	import sim
except:
	print('error... could not import sim.py')
sim.simxFinish(-1)
clientID = sim.simxStart('192.168.56.1', 19997, True, True, 5000, 5)
if clientID != -1:
	print('Pass')
	sim.simxAddStatusbarMessage(clientID, 'Pass', sim.simx_opmode_oneshot)
	sim.simxGetPingTime(clientID)
	sim.simxFinish(clientID)
else:
	print('Fail')

