// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureElectionVoting {
    struct Voter {
        bool isRegistered;
        bool hasVoted;
    }

    struct Candidate {
        string name;
        uint256 voteCount;
        bool isRegistered;
    }

    address public admin;
    uint256 public candidateCount;

    mapping(address => Voter) public voters;
    mapping(uint256 => Candidate) public candidates;

    event VoterRegistered(address voter);
    event CandidateRegistered(uint256 candidateId, string name);
    event VoteCast(address voter, uint256 candidateId);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call");
        _;
    }

    modifier onlyRegisteredVoter() {
        require(voters[msg.sender].isRegistered, "Voter not registered");
        _;
    }

    modifier notVotedYet() {
        require(!voters[msg.sender].hasVoted, "Voter already voted");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function registerVoter(address voter) external onlyAdmin {
        require(voter != address(0), "Invalid voter");
        require(!voters[voter].isRegistered, "Voter already registered");

        voters[voter] = Voter({isRegistered: true, hasVoted: false});
        emit VoterRegistered(voter);
    }

    function registerCandidate(string calldata name) external onlyAdmin {
        require(bytes(name).length > 0, "Name required");

        candidates[candidateCount] = Candidate({
            name: name,
            voteCount: 0,
            isRegistered: true
        });

        emit CandidateRegistered(candidateCount, name);
        candidateCount += 1;
    }

    function vote(uint256 candidateId)
        external
        onlyRegisteredVoter
        notVotedYet
    {
        require(candidateId < candidateCount, "Invalid candidate");
        require(candidates[candidateId].isRegistered, "Candidate not registered");

        voters[msg.sender].hasVoted = true;
        candidates[candidateId].voteCount += 1;

        emit VoteCast(msg.sender, candidateId);
    }

    function getCandidate(uint256 candidateId)
        external
        view
        returns (string memory name, uint256 voteCount)
    {
        require(candidateId < candidateCount, "Invalid candidate");
        Candidate storage candidate = candidates[candidateId];
        return (candidate.name, candidate.voteCount);
    }

    function results()
        external
        view
        returns (string[] memory names, uint256[] memory votes)
    {
        names = new string[](candidateCount);
        votes = new uint256[](candidateCount);

        for (uint256 i = 0; i < candidateCount; i++) {
            Candidate storage candidate = candidates[i];
            names[i] = candidate.name;
            votes[i] = candidate.voteCount;
        }
    }
}
