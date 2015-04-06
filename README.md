# GraphicsBtns-PY
This is a basic buttons addon for graphics.py.

Button: makes a class of your button.
	Usage: Button(Name, x1, x2, y1, y2)
	Example: creates a button with the top left corner at 1,3 and the bottom right corner at 2,4
		new_button = Button("quit", 1, 2, 3, 4)
setBtnColor: sets the color of your button.
	Usage: setBtnColor(redValue, greenValue, blueValue)
	Example: sets button to red
		new_button.setBtnColor(255, 0, 0)
drawBtn: draws your button.
	Usage: drawBtn(window)
	Example:
		new_button.drawBtn(win)
testBtn: tests a point to see if button is trigered
	Usage: testBtn(point)
	Example:
		new_button.testBtn(P1)