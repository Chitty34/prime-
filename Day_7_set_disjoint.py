#disjoint
a={1,2,3,4,5,6,7,8,9}
even={2,4,6,8}
odd={1,3,5,7,9}
print(even.isdisjoint(a))
print(odd.isdisjoint(a))
print(a.isdisjoint(a))
print(even.isdisjoint(odd))
print(odd.isdisjoint(even))
