flag = [
    [0xFFFFFF] * 16,  
    [0xFFFFFF] * 16,
    [0xFFFFFF] * 16,
    [0xFFFFFF] * 16,
    [0xFFFFFF] * 16,
    [0x0000FF] * 16,  
    [0x0000FF] * 16,
    [0x0000FF] * 16,
    [0x0000FF] * 16,
    [0x0000FF] * 16,
    [0x0000FF] * 16,
    [0xFF0000] * 16,  
    [0xFF0000] * 16,
    [0xFF0000] * 16,
    [0xFF0000] * 16,
    [0xFF0000] * 16,
    
]

for line in flag:
    for pixel in line:
        pixel_r = pixel >> 16
        pixel_g = (pixel >> 8) & 0x00FF
        pixel_b = pixel & 0xFF
        gr = int((max(pixel_r, pixel_g, pixel_b) + min(pixel_r, pixel_g, pixel_b)) / 2)
        print(f'\033[38;2;{gr};{gr};{gr}m' + '\u2588'*2,end='')
    print()

