from .agent_based_api.v1 import *


def discovery_chia_netspace(section):
	yield Service()


def check_chia_netspace(section):
	for lineArray in section:
		line = ' '.join(lineArray)
		if line.startswith("Estimated network space"):
				yield Metric("netspace", float(lineArray[3]))
				yield Result(state=State.OK, summary="Netspace " + lineArray[3] + " " + lineArray[4])
				return

	yield Result(state=State.UNKNOWN, summary="No netspace status found")


register.check_plugin(
	name="chia_netspace",
	service_name="Chia Netspace",
	discovery_function=discovery_chia_netspace,
	check_function=check_chia_netspace,
)

