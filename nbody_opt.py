"""
    N-body simulation.

    Optimized Version

    This version combines all changes to the other versions. Overall processing time slightly above 30 seconds. Relative speed up (i.e. time to run original / time to run optimized version) is around 3.

"""

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),

    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),

    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),

    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}
   
def advance(dt, bodies):
    '''
        advance the system one timestep
    '''
    bodylist = list(bodies.keys())
    bodycount = len(bodylist)
    for i in range(bodycount):
        for j in range(i+1, bodycount):
            body1 = bodylist[i]
            body2 = bodylist[j]
            ([x1, y1, z1], v1, m1) = bodies[body1]
            ([x2, y2, z2], v2, m2) = bodies[body2]
            (dx, dy, dz) = (x1-x2, y1-y2, z1-z2) # compute_deltas
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5)) # compute_mag
            m2_b = m2 * mag # compute_b
            m1_b = m1 * mag # compute_b
            bodies[body1][1][0] -= dx * m2_b # update_vs
            bodies[body1][1][1] -= dy * m2_b # update_vs
            bodies[body1][1][2] -= dz * m2_b # update_vs
            bodies[body2][1][0] += dx * m1_b # update_vs
            bodies[body2][1][1] += dy * m1_b # update_vs
            bodies[body2][1][2] += dz * m1_b # update_vs
    
    for body in bodies.keys():
        (r, [vx, vy, vz], m) = bodies[body]
        bodies[body][0][0] += dt * vx # update_rs
        bodies[body][0][1] += dt * vy # update_rs
        bodies[body][0][2] += dt * vz # update_rs

    return bodies

def map_decrease_energy(body1, body2):
    ((x1, y1, z1), v1, m1) = BODIES[body1]
    ((x2, y2, z2), v2, m2) = BODIES[body2]
    (dx, dy, dz) = (x1-x2, y1-y2, z1-z2) # compute_deltas
    return (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5) # compute_energy  

def map_increase_energy(body):
    (r, [vx, vy, vz], m) = BODIES[body]
    return m * (vx * vx + vy * vy + vz * vz) / 2.
    
def report_energy(bodies, e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    list1 = []
    list2 = []
    bodylist = list(bodies.keys())
    bodycount = len(bodylist)
    for i in range(bodycount):
        for j in range(i+1, bodycount):
            body1 = bodylist[i]
            body2 = bodylist[j]
            list1.append(body1)
            list2.append(body2)
        
    energies = map(map_decrease_energy, list1, list2)
    for energy in energies:
        e -= energy

    energies = map(map_increase_energy, BODIES.keys())
    for energy in energies:
        e += energy
       
    return e

def offset_momentum(ref, px=0.0, py=0.0, pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
    offset_momentum(BODIES[reference])

    bodies = BODIES

    for _ in range(loops):
        report_energy(bodies)
        for _ in range(iterations):
            bodies = advance(0.01, bodies)
        print(report_energy(bodies))

if __name__ == '__main__':
    nbody(100, 'sun', 20000)

