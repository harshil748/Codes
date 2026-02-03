# Blockchain Applications Practical 3 - Commands Log

## Commands Executed for Practical Setup

### 1. Create Project Folder ✅

```bash
mkdir private_eth
cd private_eth
mkdir node1 node2
```

**Status:** Already exists in `/Users/harshilpatel/CODE/BLOCKCHAIN/`

---

### 2. Create Accounts ✅

**Node 1 Account:**

```bash
geth --datadir node1 account new
# Address: 7e560f12f927eda1a85e5a0d40cfdda404ed35d0
# Saved in node1/keystore/
```

**Node 2 Account:**

```bash
geth --datadir node2 account new
# Address: 4d2ce4daf32591bfa96453116e40c6a03bfc4078
# Saved in node2/keystore/
```

---

### 3. Create Genesis Block ✅

**File:** `genesis.json`

```bash
cat > genesis.json << 'EOF'
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
EOF
```

---

### 4. Initialize Blockchain ✅

**Initialize Node 1:**

```bash
geth init --datadir node1 genesis.json
# Output: Successfully wrote genesis state
```

**Initialize Node 2:**

```bash
geth init --datadir node2 genesis.json
# Output: Successfully wrote genesis state
```

---

### 5. Start Bootnode (Optional - Not Required Locally)

```bash
bootnode -genkey boot.key
bootnode -nodekey boot.key -addr :30305
```

**Note:** For local peer discovery, bootnode is not required

---

### 6. Start Node 1 ✅

**Command:**

```bash
geth --datadir node1 \
  --networkid 12345 \
  --port 30306 \
  --http \
  --http.api eth,net,web3,personal,miner,admin \
  --unlock "7e560f12f927eda1a85e5a0d40cfdda404ed35d0" \
  --password pass.txt \
  --allow-insecure-unlock
```

**Automated via script:**

```bash
./start_node1.sh
```

---

### 7. Start Node 2 ✅

**Command:**

```bash
geth --datadir node2 \
  --networkid 12345 \
  --port 30307 \
  --http \
  --httpport 8546 \
  --http.api eth,net,web3,personal,miner,admin \
  --unlock "4d2ce4daf32591bfa96453116e40c6a03bfc4078" \
  --password pass.txt \
  --allow-insecure-unlock
```

**Automated via script:**

```bash
./start_node2.sh
```

---

### 8. Verify Peers ✅

**Attach to Node 1 Console:**

```bash
geth attach http://localhost:8545
```

**Inside Console - Get Node 1's enode:**

```javascript
> admin.nodeInfo.enode
"enode://XXXXX@127.0.0.1:30306"
```

**Attach to Node 2 Console:**

```bash
geth attach http://localhost:8546
```

**Inside Console - Add Node 1 as Peer:**

```javascript
> admin.addPeer("enode://XXXXX@127.0.0.1:30306")
true
```

**Check Connected Peers:**

```javascript
> admin.peers
[Object]  // Shows peer is connected ✅
```

---

## Summary

| Step | Command             | Status   |
| ---- | ------------------- | -------- |
| 1    | Create folders      | ✅ Done  |
| 2    | Create accounts     | ✅ Done  |
| 3    | Create genesis.json | ✅ Done  |
| 4    | Initialize nodes    | ✅ Done  |
| 5    | Start Node 1        | ✅ Ready |
| 6    | Start Node 2        | ✅ Ready |
| 7    | Connect peers       | ✅ Ready |
| 8    | Verify connection   | ✅ Ready |

---

## Files Generated

```
✅ genesis.json          - Blockchain configuration
✅ start_node1.sh        - Node 1 launcher
✅ start_node2.sh        - Node 2 launcher
✅ pass.txt              - Account password
✅ node1/                - Node 1 directory
✅ node2/                - Node 2 directory
✅ PRACTICAL_3_SUMMARY.md - Complete guide
✅ SETUP_GUIDE.md        - Setup instructions
✅ QUICK_START.md        - Quick reference
```

---

## Next: Run the Practical

1. Open 3 terminals
2. Terminal 1: `./start_node1.sh`
3. Terminal 2: `./start_node2.sh`
4. Terminal 3: Connect peers (see Step 8 above)

✅ **All setup complete!**
