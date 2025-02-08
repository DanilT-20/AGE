scooters = []
with open('C:/Users/DTolstyh/Desktop/Новая папка/26_9711.txt') as file:
    M, N = map(int, file.readline().split())
    max_time = 0
    for line in file:
        a, b, c, d = map(int, line.split())
        scooters.append([a, a+b+1, c, d])
        if max_time < a + b + 1:
            max_time = a+b+1
scooters = sorted(scooters)
start_scooters = [0] * (M + 1)
end_scooters = []
for i in range(M + 1):
    end_scooters.append([])

for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    start_park = scooter[2]
    end_park = scooter[3]
    if len(end_scooters[start_park]) != 0 \
            and min(end_scooters[start_park]) <= start_time:
        end_scooters[start_park].remove(min(end_scooters[start_park]))
    else:
        start_scooters[start_park] += 1
    end_scooters[end_park].append(end_time)
timeline = [0] * max_time
for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    for i in range(start_time, end_time):
        timeline[i] += 1
print(timeline.index(max(timeline)))
print(start_scooters.index(max(start_scooters)))