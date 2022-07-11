"""
Set Operations
set is special case of list with no repeatations,no index
1.union => club both sets and return all items in both sets
2.intersection => gets the common items in both sets
3.difference => ex:A-B items which are present in A but not present in B
4.add   => adds a new item to the set, single item
5.update  => also adds new item to the set, adds multiple items
6.discard  => removes specified item
7.remove  => removes specified item if item exists else throws error
8.issubset => A.issubset(B) ALL Contents of A exists in B and more
9.issuperset =>A.issuperset(B) All contents of B exists in A and more

"""
set_1 ={10,11,34,22,56,78,34,67,45}
set_2 ={11,45,23,67,89}
set_3={56,78,45,67,9999,6666}
#1.union => club both sets and return all items in both sets
abc123 = set_1.union(set_2)
print(abc123)
"""
Result:
{34, 67, 10, 11, 45, 78, 22, 23, 56, 89}

"""
#2.intersection => gets the common items in both sets
result_qwerty=set_1.intersection(set_2)
print(result_qwerty)
"""
{11, 67, 45}
"""
asdf_123=set_1.union(set_3)
asdf_789=set_1.intersection(set_3)
zxcv_1 = set_1.union(set_2).union(set_3)
print(zxcv_1)
zxcv_2 = set_1.union(set_2).intersection(set_3)
print(zxcv_2)
"""
Result:
{34, 67, 10, 11, 6666, 45, 78, 9999, 22, 23, 56, 89}
{56, 67, 45, 78}

"""
#3.difference => ex:A-B items which are present in A but not present in B
as_1 = set_1-set_2
print(as_1)
as_2 = set_2-set_1
print(as_2)
as_3 = set_3-set_1
print(as_3)
"""
Result:
{34, 10, 78, 22, 56}
{89, 23}
{6666, 9999}
"""
#4.add   => adds a new item to the set, single item
print(set_1)
set_1.add(777)
print(set_1)
set_1.add(666)
print(set_1)
"""
Result:
{34, 67, 10, 11, 45, 78, 22, 56}
{34, 67, 777, 10, 11, 45, 78, 22, 56}
{34, 67, 777, 10, 11, 45, 78, 22, 56, 666}

"""
#5.update  => also adds new item to the set, adds multiple items
print(set_1)
set_1.update((22,33,44,55,66))
print(set_1)
set_1.update((4444,6666,7777))
print(set_1)
"""
Result:
{33, 34, 67, 66, 777, 10, 11, 44, 45, 78, 22, 55, 56, 666}
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 78, 6666, 22, 55, 56, 666, 4444}
"""
#6.discard  => removes specified item
print(set_1)
set_1.discard(78)
print(set_1)
set_1.discard(6666)
print(set_1)
set_1.discard(99999)
print(set_1)
"""
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 78, 6666, 22, 55, 56, 666, 4444}
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 6666, 22, 55, 56, 666, 4444}
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 22, 55, 56, 666, 4444}
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 22, 55, 56, 666, 4444}
"""

#7.remove  => removes specified item if item exists else throws error
print(set_1)
set_1.remove(55)
print(set_1)
#set_1.remove(1111)
#print(set_1)
"""
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 22, 55, 56, 666, 4444}
{33, 34, 67, 66, 7777, 777, 10, 11, 44, 45, 22, 56, 666, 4444}

KeyError: 1111
"""
#8.issubset => A.issubset(B) ALL Contents of A exists in B and more
A={10,20,30}
B={10,20,30,40}
result = A.issubset(B)
print(result)
result1= B.issubset(A)
print(result1)
"""
True
False
"""
#9.issuperset =>A.issuperset(B) All contents of B exists in A and more
result2 = A.issuperset(B)
print(result2)
result3 = B.issuperset(A)
print(result3)
"""
False
True
"""

cricket ={"rohit","kohli","pant","hari"}
football={"rohit","ashok","ramesh","hari"}
vollyball={"ramesh","harish","suman","hari"}
TT={"hanish","arjun","arvind","suman","hari"}
all_players=cricket.union(football).union(vollyball).union(TT)
print(all_players)
all_games_players = cricket.intersection(football).intersection(vollyball).intersection(TT)
print(all_games_players)
#players play football and cricket
#players play cricket and vollyball
#player play TT and cricket
#new player "chandu" added to TT,football
#player "suman" removed from TT and vollyball
#player arjun moved from TT to cricket
#players play cricket but not football
#player play TT but not vollyball
#player play football but not vollyball and TT
