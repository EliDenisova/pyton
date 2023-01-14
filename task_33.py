import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# def find_farthest_orbit(orbits):
#     s = [3.14 * max(x) * min(x) if max(x) != min(x)
#          else 0 for x in orbits]
#     return (orbits[s.index(max(s))])




def find_farthest_orbit(list_of_orbits):
    list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
    list_of_areas = [(math.pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
    max_area_index = list_of_areas.index(max(list_of_areas))
    return list_of_elliptical_orbits[max_area_index]

print(*find_farthest_orbit(orbits))
