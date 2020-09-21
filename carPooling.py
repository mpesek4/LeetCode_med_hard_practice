def carPooling(trips, capacity):

    trips.sort(key=lambda x: x[1])
    cap_arr = [0 for _ in range(1000)]

    for idx,trip in enumerate(trips):
        cmax = -1
        cmax = max(cmax,trip[2])
        cap_arr[trip[2]] -= trip[0]
        cap_arr[trip[1]]+= trip[0]
    current_cap = 0
    for i in range(0, cmax+1):
        current_cap+= cap_arr[i]
        if current_cap > capacity:
            return False
    return True

print(carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))