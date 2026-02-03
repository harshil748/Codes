# Quick Reference - Blockchain Applications Practical 3

## 🚀 START HERE

### Terminal 1: Node 1

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN && ./start_node1.sh
```

### Terminal 2: Node 2

```bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN && ./start_node2.sh
```

### Terminal 3: Connect & Verify

```bash
# Get Node 1's enode
geth attach http://localhost:8545
> admin.nodeInfo.enode
# Copy the enode output

# Add Node 1 as peer to Node 2
geth attach http://localhost:8546
> admin.addPeer("enode://PASTE_HERE")

# Verify connection
> admin.peers
```

---

## 📋 Account Info

| Node | Address                                    | Password    | RPC Port | P2P Port |
| ---- | ------------------------------------------ | ----------- | -------- | -------- |
| 1    | `7e560f12f927eda1a85e5a0d40cfdda404ed35d0` | `123456789` | 8545     | 30306    |
| 2    | `4d2ce4daf32591bfa96453116e40c6a03bfc4078` | `123456789` | 8546     | 30307    |

---

## 🧪 Test Commands

```javascript
// Check peers
admin.peers;

// Get balance
eth.getBalance("0x7e560f12f927eda1a85e5a0d40cfdda404ed35d0");

// Send 1 ether
eth.sendTransaction({
	from: "0x7e560f12f927eda1a85e5a0d40cfdda404ed35d0",
	to: "0x4d2ce4daf32591bfa96453116e40c6a03bfc4078",
	value: web3.toWei(1, "ether"),
});

// Exit console
Ctrl + D;
```

---

## ⚙️ Config

- **Network:** Private (ID: 12345)
- **Consensus:** Clique PoA
- **Block Time:** 5 seconds
- **Gas Limit:** 8M

✅ **Setup complete and ready to run!**
