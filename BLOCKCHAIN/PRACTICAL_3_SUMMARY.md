# Practical 3: Ethereum Private Blockchain - Complete Summary

## 📌 Project Completion Status: ✅ 100%

### PART 2 - Private Blockchain with 2 Local Peer Nodes: **READY TO RUN**

---

## 📂 Files Created/Updated

1. **genesis.json** - Private blockchain genesis configuration
2. **start_node1.sh** - Startup script for Node 1
3. **start_node2.sh** - Startup script for Node 2
4. **SETUP_GUIDE.md** - Detailed setup and usage guide
5. **node1/keystore/** - Account for Node 1
6. **node2/keystore/** - Account for Node 2

---

## 🔑 Account Credentials

### Node 1

- **Address:** `7e560f12f927eda1a85e5a0d40cfdda404ed35d0`
- **Password:** `123456789`
- **Port:** 30306
- **HTTP Port:** 8545

### Node 2

- **Address:** `4d2ce4daf32591bfa96453116e40c6a03bfc4078`
- **Password:** `123456789`
- **Port:** 30307
- **HTTP Port:** 8546

---

## 🚀 Quick Start (3 Easy Steps)

### Step 1: Open Terminal 1 - Start Node 1

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
./start_node1.sh
```

**Wait for:** "HTTP server started on port 8545"

### Step 2: Open Terminal 2 - Start Node 2

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
./start_node2.sh
```

**Wait for:** "HTTP server started on port 8546"

### Step 3: Open Terminal 3 - Connect Peers

```bash
# Get Node 1's enode
geth attach http://localhost:8545
> admin.nodeInfo.enode
# Copy output, then exit (Ctrl+D)

# Connect Node 2 to Node 1
geth attach http://localhost:8546
> admin.addPeer("enode://PASTE_NODE1_ENODE_HERE")
> admin.peers
# Should show [Object] - peer connected ✅
```

---

## 📝 Genesis Block Configuration

```json
{
	"config": {
		"chainId": 12345,
		"clique": {
			"period": 5,
			"epoch": 30000
		},
		"terminalTotalDifficulty": 0,
		"terminalTotalDifficultyPassed": true
	},
	"difficulty": "1",
	"gasLimit": "8000000",
	"extraData": "0x00000000000000000000000000000000000000000000000000000000000000004d2ce4daf32591bfa96453116e40c6a03bfc40780000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
	"alloc": {}
}
```

**Key Settings:**

- **Network ID:** 12345 (identifies private network)
- **Consensus:** Clique PoA (Proof of Authority)
- **Block Time:** 5 seconds
- **Sealer:** 4d2ce4daf32591bfa96453116e40c6a03bfc4078 (Node 2 account)
- **Gas Limit:** 8,000,000

---

## 🧪 Testing Commands (After Nodes Connected)

### In Node 1 Console:

```javascript
// Check connected peers
admin.peers;

// Check account balance
eth.getBalance("0x7e560f12f927eda1a85e5a0d40cfdda404ed35d0");

// Send transaction to Node 2
eth.sendTransaction({
	from: "0x7e560f12f927eda1a85e5a0d40cfdda404ed35d0",
	to: "0x4d2ce4daf32591bfa96453116e40c6a03bfc4078",
	value: web3.toWei(1, "ether"),
});
```

---

## 🎓 What You've Learned

### Concepts:

1. **Private Blockchain** - Isolated from public Ethereum
2. **Clique PoA** - Authority-based consensus (no mining required)
3. **Peer Discovery** - Node-to-node communication
4. **Network ID** - Ensures correct network isolation
5. **Genesis Block** - Initial state definition
6. **Accounts & Keystores** - Ethereum account management

### Technical Skills:

✅ Install and configure Geth
✅ Create blockchain accounts
✅ Generate genesis blocks
✅ Initialize blockchain nodes
✅ Connect nodes as peers
✅ Interact with blockchain via console

---

## 🔍 Directory Structure

```
/Users/harshilpatel/CODE/BLOCKCHAIN/
├── genesis.json                    ← Blockchain definition
├── pass.txt                        ← Password for accounts
├── start_node1.sh                  ← Node 1 launcher
├── start_node2.sh                  ← Node 2 launcher
├── SETUP_GUIDE.md                  ← This setup guide
├── node1/
│   ├── geth/
│   │   ├── chaindata/              ← Blockchain data (chain, state, etc.)
│   │   ├── nodekey                 ← Node's private key
│   │   └── geth.ipc                ← IPC socket (for console)
│   ├── keystore/
│   │   └── UTC--...-7e560f...      ← Account keystore file
│   └── LOCK
├── node2/
│   ├── geth/
│   │   ├── chaindata/              ← Blockchain data
│   │   ├── nodekey                 ← Node's private key
│   │   └── geth.ipc                ← IPC socket
│   ├── keystore/
│   │   └── UTC--...-4d2ce4...      ← Account keystore file
│   └── LOCK
└── bootnode/                       ← Optional (not used here)
```

---

## ⚠️ Common Issues & Solutions

| Problem                                 | Solution                                             |
| --------------------------------------- | ---------------------------------------------------- |
| **"Address already in use"**            | Change port numbers in start_node\*.sh               |
| **"Could not create listening socket"** | Another geth instance running, kill it first         |
| **Nodes won't connect**                 | Ensure `--networkid 12345` on both nodes             |
| **Unlock fails**                        | Verify password in pass.txt matches account password |
| **Peer list empty**                     | Add peer manually with `admin.addPeer(enode)`        |
| **"Genesis mismatch"**                  | Delete node\*/geth folder and reinitialize           |

---

## 🎯 Next Steps (Optional - PART 3-5)

### PART 3: Distributed Nodes (Different Networks)

- Deploy Node 1 on local machine
- Deploy Node 2 on cloud (AWS EC2)
- Connect via public IP + port forwarding

### PART 4: Connect to Sepolia Testnet

- Use public testnet to test on real Ethereum chain
- Get test ETH from faucet

### PART 5: Layer 2 Networks

- Deploy smart contracts on Arbitrum/Optimism
- Test scaling solutions

---

## ✅ Verification Checklist

Before submission, verify:

- [ ] Both nodes start without errors
- [ ] Node 1 shows "HTTP server started on port 8545"
- [ ] Node 2 shows "HTTP server started on port 8546"
- [ ] Can attach to Node 1: `geth attach http://localhost:8545`
- [ ] Can attach to Node 2: `geth attach http://localhost:8546`
- [ ] Can get Node 1's enode: `admin.nodeInfo.enode`
- [ ] Can add Node 2 as peer to Node 1
- [ ] `admin.peers` shows connected peers
- [ ] Can check account balance: `eth.getBalance("0x...")`

---

## 📞 Support Commands

```bash
# Check geth version
geth version

# See running processes
ps aux | grep geth

# Kill a geth instance
killall geth

# Reset blockchain (CAUTION - deletes all data)
rm -rf /Users/harshilpatel/CODE/BLOCKCHAIN/node1/geth
rm -rf /Users/harshilpatel/CODE/BLOCKCHAIN/node2/geth
```

---

## 🎉 You're All Set!

Your private Ethereum blockchain is ready to use. Start the nodes and experiment with transactions, account management, and peer connections!
