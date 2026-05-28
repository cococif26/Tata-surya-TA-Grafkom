from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from math import cos, sin, radians

app = Ursina(title='Tata Surya')
window.color = color.black

matahari = Entity(
    model='sphere',
    color=color.orange,
    scale=5
)

# Cahaya
PointLight(parent=matahari)
AmbientLight(color=color.white)

matahari.scale = 0.1
matahari.animate_scale(
    5,
    duration=1,
    curve=curve.out_bounce
)

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

planets = []

for nama, jarak, ukuran, warna, kecepatan in data_planet:

    Entity(
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

    orbit = Entity()

    planet = Entity(
        parent=orbit,
        model='sphere',
        color=warna,
        scale=ukuran,
        position=(jarak, 0, 0),
    )

    planets.append((orbit, planet, kecepatan))

    ground = Entity(
        model='plane',
        scale=(200,1,200),
        collider='box',
        visible=False
    )

    player = FirstPersonController(
        position=(0,2,-40),
        kecepatan=10
    )

# Animasi 3D
def update():

    for orbit, planet, kecepatan in planets:

        orbit.rotation_y += kecepatan * time.dt
        planet.rotation_y += 40 * time.dt

    player.x = clamp(player.x, -80, 80)
    player.z = clamp(player.z, -80, 80)

app.run()