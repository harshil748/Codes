#!/bin/bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
geth --datadir node2 \
  --networkid 12345 \
  --port 30307 \
  --http \
  --httpport 8546 \
  --http.api eth,net,web3,personal,miner,admin \
  --unlock "4d2ce4daf32591bfa96453116e40c6a03bfc4078" \
  --password pass.txt \
  --allow-insecure-unlock
