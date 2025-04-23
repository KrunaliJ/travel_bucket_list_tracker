
# Your bucket list and visited places
bucket_list = {"Japan", "Norway", "Brazil", "Canada"}
visited = {"India", "Brazil"}

# Friend's travel list
friend_list = {"Japan", "Italy", "Canada", "Spain"}

print("Your Travel Bucket List:", bucket_list)
print(" Places You've Visited:", visited)

# Add a new dream destination
print("\n Adding 'New Zealand' to your bucket list...")
bucket_list.add("New Zealand")
print("Updated Bucket List:", bucket_list)

# Remove a place you no longer want to visit
print("\n Removing 'Brazil' (already visited)...")
bucket_list.discard("Brazil")  # Avoid error if it's not present
print("Bucket List After Update:", bucket_list)

# List places still left to visit
to_visit = bucket_list.difference(visited)
print("\nPlaces still to visit:", to_visit)

# Common places you and your friend want to visit
common_wishlist = bucket_list.intersection(friend_list)
print("Shared Dream Destinations with Friend:", common_wishlist)

# All unique places either of you want to visit
all_wishlist = bucket_list.union(friend_list)
print("Combined Bucket List:", all_wishlist)

# Show bucket list with loop
print("\nLooping through your bucket list:")
for place in bucket_list:
    print("-", place)

# Check if you and your friend have totally different travel goals
if bucket_list.isdisjoint(friend_list):
    print("\nYou and your friend have completely different travel dreams!")
else:
    print("\nYou and your friend share some common destinations!")

# Bonus: Who is more adventurous?
if len(bucket_list) > len(friend_list):
    print("You're more adventurous!")
elif len(bucket_list) < len(friend_list):
    print("Your friend is more adventurous!")
else:
    print("You both have equally big dreams!")
