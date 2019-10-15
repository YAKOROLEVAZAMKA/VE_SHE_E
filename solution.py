daysparty = list(map(int, input().split()))
days = []
for i in range(1, daysparty[0] + 1):
    days.append(i)
N = daysparty[1]
# print(days)
# print(party)
party = []
for i in range(N):
    party.append(list(map(int, input().split())))
# print(party)
ddays = []
for elem in party:
    j = elem[0]
    while j <= daysparty[0]:
        ddays.append(j)
        j += elem[1]
# print(ddays)
ddays = set(ddays)
# print(ddays)
holidays = []
j = 6
while j <= daysparty[0]:
    ddays.discard(j)
    ddays.discard(j + 1)
    j += 7
print(len(ddays))
