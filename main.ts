let grados = 0
input.onButtonPressed(Button.A, function () {
    input.calibrateCompass()
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.compassHeading())
    basic.pause(200)
})
basic.forever(function () {
    grados = input.compassHeading()
    if (grados < 45) {
        basic.showString("NN")
    } else if (grados < 135) {
        basic.showString("EE")
    } else if (grados < 225) {
        basic.showString("ZZ")
    } else if (grados < 315) {
        basic.showString("OO")
    } else {
        basic.showString("AA")
    }
})
