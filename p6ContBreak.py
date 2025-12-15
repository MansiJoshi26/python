# continue and break statement in python


# break return the for no items will print further
nameS=["ram","sita","shyam","radha","krishna"]
for name in nameS:
  if name == "radha":
    break
  print(name)

print("____________________________________________")
# continue skips
for name in nameS:
  if name == "radha":
    continue
  print(name)
