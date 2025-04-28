# travel_bucket_list_tracker using set

bucket_list = {"Japan", "Norway", "Brazil", "Canada"}
visited = {"India", "Brazil"}
We create two sets:
bucket_list: places you want to visit
visited: places you've already visited

"Brazil" is in both — meaning you planned to visit it and now have.

# Friend's travel list
friend_list = {"Japan", "Italy", "Canada", "Spain"}
A third set — your friend’s travel wishlist.

print("Your Travel Bucket List:", bucket_list)
print("Places You've Visited:", visited)
Just prints the two sets so the user sees their current data.

# Add a new dream destination
print("\n Adding 'New Zealand' to your bucket list...")
bucket_list.add("New Zealand")
print("Updated Bucket List:", bucket_list)
Adds "New Zealand" to your bucket list using add() method.

# Remove a place you no longer want to visit
print("\n Removing 'Brazil' (already visited)...")
bucket_list.discard("Brazil")  # Avoid error if it's not present
print("Bucket List After Update:", bucket_list)
discard("Brazil") removes "Brazil" from bucket_list.
We use discard() instead of remove() to avoid error if the item isn’t in the set.

# List places still left to visit
to_visit = bucket_list.difference(visited)
print("\n Places still to visit:", to_visit)
difference() gives items in bucket_list that are not in visited.
These are your upcoming dream destinations.

# Common places you and your friend want to visit
common_wishlist = bucket_list.intersection(friend_list)
print(" Shared Dream Destinations with Friend:", common_wishlist)
🫱 intersection() finds places both you and your friend want to visit — i.e. shared dream locations.

# All unique places either of you want to visit
all_wishlist = bucket_list.union(friend_list)
print("Combined Bucket List:", all_wishlist)
union() merges your and your friend’s lists, removing duplicates.

# Show bucket list with loop
print("\n Looping through your bucket list:")
for place in bucket_list:
    print("-", place)
Demonstrates looping through a set using a for loop. Each place is printed with a - bullet.

# Check if you and your friend have totally different travel goals
if bucket_list.isdisjoint(friend_list):
    print("\n You and your friend have completely different travel dreams!")
else:
    print("\n You and your friend share some common destinations!")
isdisjoint() checks whether the two sets have no elements in common.

If true → different goals
If false → some shared interests

# Bonus: Who is more adventurous?
if len(bucket_list) > len(friend_list):
    print("You're more adventurous!")
elif len(bucket_list) < len(friend_list):
    print("Your friend is more adventurous!")
else:
    print("You both have equally big dreams!")
Just a fun comparison based on the length of each set.
Larger set → more adventurous
