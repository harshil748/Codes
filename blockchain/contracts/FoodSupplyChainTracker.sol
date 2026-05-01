// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FoodSupplyChainTracker {
    struct SupplyItemInput {
        string farmerName;
        string harvestDate;
        string distributor;
        string retailer;
        string status;
    }

    struct SupplyItem {
        string batchId;
        string farmerName;
        string harvestDate;
        string distributor;
        string retailer;
        string status;
        bool exists;
    }

    address public admin;
    mapping(string => SupplyItem) private batches;

    event BatchAdded(string batchId);
    event BatchUpdated(string batchId, string status);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function addBatch(string calldata batchId, SupplyItemInput calldata input)
        external
        onlyAdmin
    {
        require(bytes(batchId).length > 0, "Batch ID required");
        require(!batches[batchId].exists, "Batch already exists");

        batches[batchId] = SupplyItem({
            batchId: batchId,
            farmerName: input.farmerName,
            harvestDate: input.harvestDate,
            distributor: input.distributor,
            retailer: input.retailer,
            status: input.status,
            exists: true
        });

        emit BatchAdded(batchId);
    }

    function updateBatch(
        string calldata batchId,
        string calldata distributor,
        string calldata retailer,
        string calldata status
    ) external onlyAdmin {
        require(batches[batchId].exists, "Batch not found");

        SupplyItem storage item = batches[batchId];
        if (bytes(distributor).length > 0) {
            item.distributor = distributor;
        }
        if (bytes(retailer).length > 0) {
            item.retailer = retailer;
        }
        if (bytes(status).length > 0) {
            item.status = status;
        }

        emit BatchUpdated(batchId, item.status);
    }

    function getBatch(string calldata batchId)
        external
        view
        returns (
            string memory farmerName,
            string memory harvestDate,
            string memory distributor,
            string memory retailer,
            string memory status
        )
    {
        require(batches[batchId].exists, "Batch not found");
        SupplyItem storage item = batches[batchId];
        return (
            item.farmerName,
            item.harvestDate,
            item.distributor,
            item.retailer,
            item.status
        );
    }
}
