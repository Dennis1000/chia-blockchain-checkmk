from .agent_based_api.v1 import *


def discovery_chia_blockchain(section):
	yield Service()


def check_chia_blockchain(section):
	for lineArray in section:
		line = ' '.join(lineArray)

	netspace = 0.0
	netspaceUnit = ""
	difficulty = 0
	summaryText = "No blockchain status found"
	nodeState = State.UNKNOWN

	for lineArray in section:
		line = ' '.join(lineArray)
		if line.startswith("Estimated network space"):
			netspace = float(lineArray[3])
			netspaceUnit = lineArray[4]

		if line.startswith("Current difficulty"):
			difficulty = int(lineArray[2])

		if line.startswith("Current Blockchain Status"):
			summaryText = line
			if "Full Node Synced" in line:
 				nodeState = State.OK
			else:
				nodeState = State.CRIT

	yield Metric("difficulty", difficulty)
	yield Metric("netspace", netspace)

	yield Result(state=nodeState, summary=summaryText + " Difficulty:" + str(difficulty) + " Netspace:" + str(netspace) + " " + netspaceUnit)


register.check_plugin(
	name="chia_blockchain",
	service_name="Chia Blockchain",
	discovery_function=discovery_chia_blockchain,
	check_function=check_chia_blockchain,
)

