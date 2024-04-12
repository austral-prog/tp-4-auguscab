def line():
	import math
	a=float(input("Ingrese el coeficiente A: "))
	b=float(input("Ingrese el coeficiente B: "))
	x1=float(input("Ingrese el coeficiente X1: "))
	x2=float(input("Ingrese el coeficiente X2: "))

	y1=a*x1+b
	y2=a*x2+b
	print(f"""El coeficiente A de su ecuación de la recta es: {a}
		El coeficiente B de su ecuación de la recta es: {b}
		El coeficiente X1 de su ecuación de la recta es: {x1}
		El coeficiente X2 de su ecuación de la recta es: {x2}""")
	print(f"""\nPara la siguiente ecuación:
		\tY={a}X + {b}""")
	print(f"""Dados los siguientes puntos:
		\tP1 ({x1}, {y1})
		\tP2({x2}, {y2})""")

	d= math.sqrt((x2-x1)**2 + (y2-y1)**2)

	print(f"\nLa distancia entre ellos es: {d}")
