import random

# --------- PoW Simulation ---------
miner1 = {"name": "Miner A", "power": random.randint(1, 100)}
miner2 = {"name": "Miner B", "power": random.randint(1, 100)}
pow_winner = miner1 if miner1["power"] > miner2["power"] else miner2

print("\n--- Proof of Work (PoW) ---")
print(f"{miner1['name']} Power: {miner1['power']}")
print(f"{miner2['name']} Power: {miner2['power']}")
print(f"Selected: {pow_winner['name']} (Highest power wins)")

# --------- PoS Simulation ---------
staker1 = {"name": "Staker A", "stake": random.randint(1, 100)}
staker2 = {"name": "Staker B", "stake": random.randint(1, 100)}
pos_winner = staker1 if staker1["stake"] > staker2["stake"] else staker2

print("\n--- Proof of Stake (PoS) ---")
print(f"{staker1['name']} Stake: {staker1['stake']}")
print(f"{staker2['name']} Stake: {staker2['stake']}")
print(f"Selected: {pos_winner['name']} (Highest stake wins)")

# --------- DPoS Simulation ---------
delegates = ["Delegate A", "Delegate B", "Delegate C"]
votes = {
    "Voter 1": random.choice(delegates),
    "Voter 2": random.choice(delegates),
    "Voter 3": random.choice(delegates)
}

# Count votes
vote_count = {delegate: list(votes.values()).count(delegate) for delegate in delegates}
most_voted = max(vote_count, key=vote_count.get)

print("\n--- Delegated Proof of Stake (DPoS) ---")
for voter, choice in votes.items():
    print(f"{voter} voted for {choice}")
print(f"Selected: {most_voted} (Most voted delegate)")
