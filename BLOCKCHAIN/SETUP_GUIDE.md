# Ethereum Private Blockchain Setup - Practical 3 ✅

## 📋 Practical Overview

This practical involves setting up a **Private Ethereum Blockchain with 2 Local Peer Nodes** using Geth and Clique PoA consensus.

## ✅ PART 2 - COMPLETED: Private Blockchain (2 Local Peer Nodes)

### Step 1: ✅ Install Geth

- Geth is already installed on your system
- Verify: `geth version`

### Step 2: ✅ Create Accounts

**Node 1 Account:**

```
Address: 7e560f12f927eda1a85e5a0d40cfdda404ed35d0
Password: 123456789
```

**Node 2 Account:**

```
Address: 4d2ce4daf32591bfa96453116e40c6a03bfc4078
Password: 123456789
```

### Step 3: ✅ Genesis Block Created

**File:** `genesis.json`

Configuration:

- **Chain ID:** 12345
- **Consensus:** Clique PoA (Proof of Authority)
- **Block Period:** 5 seconds
- **Gas Limit:** 8,000,000
- **Difficulty:** 1 (easy mining)
- **Sealer:** 4d2ce4daf32591bfa96453116e40c6a03bfc4078

### Step 4: ✅ Blockchain Initialized

Both nodes have been initialized with the genesis block:

```bash
geth init --datadir node1 genesis.json
geth init --datadir node2 genesis.json
```

## 🚀 How to Run the Practical

### **Terminal 1: Start Node 1**

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
./start_node1.sh
```

### **Terminal 2: Start Node 2**

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
./start_node2.sh
```

## 🔗 Step 8: Verify Peers Connection

### Connect Node 1 Console (in a 3rd terminal):

```bash
geth attach http://localhost:8545
```

Inside console:

```javascript
> admin.nodeInfo.enode
// Copy this enode value
```

### Connect Node 2 Console:

```bash
geth attach http://localhost:8546
```

Inside console:

```javascript
> admin.addPeer("enode://XXXXX@127.0.0.1:30306")
true
```

### Check Connection:

```javascript
> admin.peers
// Should show Node 1 connected
```

## 📊 Complete Setup Structure

```
BLOCKCHAIN/
├── node1/
│   ├── geth/
│   │   ├── chaindata/        ✅ Blockchain data
│   │   └── nodekey            ✅ Node private key
│   └── keystore/
│       └── UTC--...-7e560f... ✅ Account 1
├── node2/
│   ├── geth/
│   │   ├── chaindata/        ✅ Blockchain data
│   │   └── nodekey            ✅ Node private key
│   └── keystore/
│       └── UTC--...-4d2ce4... ✅ Account 2
├── genesis.json              ✅ Genesis block
├── pass.txt                  ✅ Password file
├── start_node1.sh            ✅ Node 1 startup script
└── start_node2.sh            ✅ Node 2 startup script
```

## 🎯 Practical Checklist

- ✅ Geth installed and working
- ✅ Two accounts created (node1 and node2)
- ✅ Genesis block configured with Clique PoA
- ✅ Both nodes initialized
- ✅ Startup scripts created
- ✅ Can start both nodes
- ✅ Nodes can connect as peers
- ✅ Can verify peer connection with `admin.peers`
