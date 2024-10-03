from qlbm.components.collisionless import GridMeasurement
from qlbm.lattice import CollisionlessLattice

# Build an example lattice
lattice = CollisionlessLattice({
    "lattice": {
        "dim": {
        "x": 8,
        "y": 8
        },
        "velocities": {
        "x": 4,
        "y": 4
        }
    },
    "geometry": [
        {
        "x": [5, 6],
        "y": [1, 2],
        "boundary": "specular"
        }
    ]
})

# Draw the measurement circuit
GridMeasurement(lattice).draw("mpl")