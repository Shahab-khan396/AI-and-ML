import random

def flip():
    return random.randint(0, 1)

def simulate_coin_tosses(num_tosses):
   
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        result = flip()
        if result == 1:
            print("Heads")
            heads_count += 1
        else:
            print("Tails")
            tails_count += 1

    print("\nResults after", num_tosses, "tosses:")
    print("Heads:", heads_count)
    print("Tails:", tails_count)

# Simulate 100 coin tosses
simulate_coin_tosses(100)
