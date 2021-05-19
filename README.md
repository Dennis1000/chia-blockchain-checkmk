# chia-blockchain-checkmk
A Checkmk 2.0+ agent plugin for monitoring your Chia Blockchain Nodes and Chia Farms


# Installation
1. Copy all `checkmk-server/` files into your Checkmk server site agent folder e.g. `OMD[<mysite>]:~/local/lib/check_mk/base/plugins/agent_based/` and mark them as executable with `chmod +x *.py`
2. Copy all `checkmk-client/` files into your Checkmk client plugin folder e.g. `/usr/lib/check_mk_agent/plugins/` and mark them as executable with `chmod +x *`
3. Update the `CHIA_INSTALLATION_PATH=` and `CHIA_INSTALLATION_USER=farmer` in those client plugin files with your chia installation path and Chia user.
4. Rediscover the new services on each client via WATO.

# History
v1.00 Initial commit.