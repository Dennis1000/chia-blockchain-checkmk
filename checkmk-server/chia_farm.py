from .agent_based_api.v1 import *


def discovery_chia_farm(section):
	yield Service()


def check_chia_farm(section):
	plots = 0
	plotsize = 0.0
	plotsizeUnit = ""
	rewards = 0.0
	farmed = 0.0
	summaryText = "No farming status found"
	farmState = State.UNKNOWN

	for lineArray in section:
		line = ' '.join(lineArray)
		if line.startswith("Plot count"):
			 plots  = int(lineArray[5])

		if line.startswith("Total size of plots"):
			plotsize = float(lineArray[4])
			plotsizeUnit = lineArray[5]

		if line.startswith("Block rewards"):
 			rewards = float(lineArray[2])

		if line.startswith("Total chia farmed"):
			farmed = float(lineArray[3])

		if line.startswith("Farming status"):
			summaryText = line
			if "status: Farming" in line:
				farmState = State.OK
			else:
				farmState=State.CRIT

	yield Metric("plots", plots)
	yield Metric("plotsize", plotsize)
	yield Metric("rewards", rewards)
	yield Metric("farmed", farmed)

	yield Result(state=farmState, summary=summaryText + " Plots:" + str(plots) + " Plot size:" + str(plotsize) + " " + plotsizeUnit + " Rewards: " + str(rewards) + " Total farmed: " + str(farmed))

register.check_plugin(
	name="chia_farm",
	service_name="Chia Farm",
	discovery_function=discovery_chia_farm,
	check_function=check_chia_farm,
)

