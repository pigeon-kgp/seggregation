from math import sqrt


def cube_round(x,y,z):
    rx = round(x)
    ry = round(y)
    rz = round(z)

    x_diff = abs(rx - x)
    y_diff = abs(ry - y)
    z_diff = abs(rz - z)

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry-rz
    elif y_diff > z_diff:
        ry = -rx-rz
    else:
        rz = -rx-ry
    return rx, ry, rz

def cube_to_axial(x,y,z):
    q = x
    r = z
    return q, r

def axial_to_cube(q,r):
    x = q
    z = r
    y = -x-z
    return x, y, z

def hex_round(q,r):
    x,y,z = axial_to_cube(q,r)
    rx,ry,rz = cube_round(x,y,z)
    return cube_to_axial(rx,ry,rz)

def pixel_to_hex(x, y, size=2):
    q = (x * sqrt(3)/3 - y / 3) / size
    r = (y * 2/3) / size
    hereq, herer = hex_round(q,r)
    return [hereq,herer]

# a = float(raw_input())
# b = float(raw_input())
# print pixel_to_hex(a,b)

# size is edge length of a hexagon
