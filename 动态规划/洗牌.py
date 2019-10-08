def xi(start,end=[]):
    part1,part2 = start[:int(len(start)/2)],start[int(len(start)/2):]
    for i in range(len(part1)-1,-1,-1):
        end.append(part2[i])
        end.append(part1[i])
    return end
start = [1,2,3,4,5,6]
for i in range(2):
    print(start)
    start=xi(start,end=[])
print(start)
