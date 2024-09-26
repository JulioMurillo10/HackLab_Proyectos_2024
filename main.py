grados = 0

def on_button_pressed_a():
    input.calibrate_compass()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_forever():
    global grados
    grados = input.compass_heading()
    if grados < 45:
        basic.show_string("Norte")
    elif grados < 135:
        basic.show_string("Este")
    elif grados < 225:
        basic.show_string("Sur")
    elif grados < 315:
        basic.show_string("Oeste")
    else:
        basic.show_string("Norte")
basic.forever(on_forever)
