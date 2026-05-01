const FoodSupplyChainTracker = artifacts.require("FoodSupplyChainTracker");

module.exports = function (deployer) {
	deployer.deploy(FoodSupplyChainTracker);
};
