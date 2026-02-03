#!/bin/bash
cd /Users/harshilpatel/CODE/BLOCKCHAIN
geth --datadir node1 \
  --networkid 12345 \
  --port 30306 \
  --http \
  --http.api eth,net,web3,personal,miner,admin \
  --unlock "7e560f12f927eda1a85e5a0d40cfdda404ed35d0" \
  --password pass.txt \
  --allow-insecure-unlock
