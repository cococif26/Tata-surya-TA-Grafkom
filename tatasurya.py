from ursina import *
from math import cos, sin, radians

app = Ursina()
window.color = color.black

camera.position = (0, 30, -50)
camera.rotation_x = 30


matahari = Entity(
    model='sphere',
    color=color.orange,
    scale=5
)

# Cahaya
PointLight(
    parent=matahari,
    y=2,
    z=-3,
    color=color.white
)
ambient_light = AmbientLight(color=color.white)


data_planet = [
    ('Merkurius', 5, 0.5, color.gray, 80),
    ('Venus', 8, 0.8, color.yellow, 60),
    ('Bumi', 11, 1.1, color.blue, 45),
    ('Mars', 14, 0.7, color.red, 35),
    ('Jupiter', 17, 2.2, color.brown, 25),
    ('Saturnus', 20, 1.5, color.gold, 20),
    ('Uranus', 23, 1.2, color.cyan, 15),
    ('Neptunus', 26, 1.2, color.azure, 10)
]

entitas_planet = []

# buat garis orbit disetiap planet
def garis_orbit(jarak):

    orbit = Entity(
        model=Mesh(
            vertices=[
                Vec3(
                    cos(radians(i)) * jarak,
                    0,
                    sin(radians(i)) * jarak
                )
                for i in range(361)
            ],
            mode='line'
        ),
        color=color.white
    )

    return orbit


for nama, jarak, skala, warna, kecepatan in data_planet:

    orbit_parent = Entity()

    planet = Entity(
        parent=orbit_parent,
        model='sphere',
        color=warna,
        texture='earth',
        scale=skala,
        position=(jarak, 0, 0),
        name=nama
    )

    garis_orbit(jarak)

    entitas_planet.append({
        'orbit': orbit_parent,
        'kecepatan': kecepatan
    })

# Animasi
def update():

    for planet in entitas_planet:
        planet['orbit'].rotation_y += (
            planet['kecepatan'] * time.dt
        )

app.run()