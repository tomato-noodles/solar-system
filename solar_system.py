from turtle import color
from graphics import *
import time
from math import sin, cos, sqrt


au_in_pixels = 50
m_per_pixel = 1.496e11 / au_in_pixels  
t_scale = 5_000_000
g = 6.6743e-11 
sun_m = 1.989e30

def square(x):
    return x * x


#orbit_radius: AU, radius is planet_radius in pixels
def create_planet(sun_x, sun_y, orbit_radius_au, color, size, mass, init_speed, win):
    speed_x = 0
    speed_y = init_speed
    x = sun_x + orbit_radius_au * au_in_pixels
    y = sun_y
    sprite = Circle(Point(x, y), size)
    sprite.setFill(color)
    sprite.draw(win)

    planet = {
        'mass': mass,
        'x': x,
        'y': y,
        'speed_x': speed_x,
        'speed_y': speed_y,
        'sprite': sprite   
    }
    return planet

#laptop_res 1270, 620
def main():
    width = 1800
    height = 1000
    sun_x = width/2
    sun_y = height/2
    frame_rate = 120
    dt = 1 / frame_rate
    win = GraphWin("My Solar System", width, height)    
    win.setBackground("black")
    sun = Circle(Point(width/2, height/2), 15)
    sun.setFill("yellow")
    sun.draw(win)
    mercury = create_planet(sun_x, sun_y, 
        orbit_radius_au=0.41, 
        color="dark gray", 
        size=3,
        mass=3.3022e23,
        init_speed=46522.44, 
        win=win)
    venus = create_planet(sun_x, sun_y, 
        orbit_radius_au=0.7, 
        color="dark goldenrod", 
        size=4.8,
        mass=4.8685e24,
        init_speed=35604.54,          
        win=win)
    earth = create_planet(sun_x, sun_y, 
        orbit_radius_au=1, 
        color="cornflower blue", 
        size=5,
        mass=5.9736e24, 
        init_speed=29788.89, 
        win=win)
    mars = create_planet(sun_x, sun_y, 
        orbit_radius_au=1.52, 
        color="tomato", 
        size=2.8,
        mass=6.4185e23, 
        init_speed=24161.98, 
        win=win)
    jupiter = create_planet(sun_x, sun_y, 
        orbit_radius_au=5.2, 
        color="peru", 
        size=55,
        mass=1.8986e27, 
        init_speed=13063.29, 
        win=win)
    saturn = create_planet(sun_x, sun_y, 
        orbit_radius_au=9.5, 
        color="dark khaki", 
        size=45,
        mass=5.6846e26, 
        init_speed=9664.79, 
        win=win)
    uranus = create_planet(sun_x, sun_y, 
        orbit_radius_au=19.8, 
        color="light blue", 
        size=20,
        mass=8.6810e25, 
        init_speed=6694.55, 
        win=win)
    neptune = create_planet(sun_x, sun_y, 
        orbit_radius_au=30, 
        color="dodger blue", 
        size=20,
        mass=10.243e25, 
        init_speed=5438.68, 
        win=win)

    
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


    while True:
        time.sleep(dt)
        scaled_dt = dt * t_scale 

        for p in planets:
            old_x = p['x'] 
            old_y = p['y']
            r_squared = square(sun_x - old_x) + square(sun_y - old_y)
            a = g * sun_m / r_squared
            p['x'] = old_x + scaled_dt * p['speed_x'] / m_per_pixel 
            p['y'] = old_y + scaled_dt * p['speed_y'] / m_per_pixel
            p['sprite'].move(p['x'] - old_x, p['y'] - old_y)

main()

