"""Simple SVG drawing CLI.

This script provides interactive commands to draw a square, circle or
hexagon into an svgwrite.Drawing object and save it to disk.

Cleaned and refactored for readability and basic input validation.
"""

from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon
from math import cos, sin, radians, sqrt
from typing import Tuple


def _input_int(prompt: str) -> int:
	"""Read an integer from input, reprompting until valid."""
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid integer.")


def draw_square(dwg: Drawing) -> None:
	"""Draw a square based on user input into the provided Drawing."""
	x = _input_int("Left edge position: ")
	y = _input_int("Top edge position: ")
	side = _input_int("Side length: ")
	fill = input("Fill color (name or hex, empty for none): ") or None
	stroke = input("Stroke color (name or hex, empty for none): ") or None
	dwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))


def draw_circle(dwg: Drawing) -> None:
	"""Draw a circle based on user input into the provided Drawing."""
	cx = _input_int("Center X coord: ")
	cy = _input_int("Center Y coord: ")
	r = _input_int("Radius: ")
	fill = input("Fill color (name or hex, empty for none): ") or None
	stroke = input("Stroke color (name or hex, empty for none): ") or None
	dwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))


def _regular_polygon_points(center: Tuple[int, int], radius: float, sides: int, start_angle: float = 0.0):
	"""Return a list of (x, y) points for a regular polygon."""
	cx, cy = center
	points = []
	angle_step = 360.0 / sides
	for i in range(sides):
		angle_deg = start_angle + i * angle_step
		x = round(cx + radius * cos(radians(angle_deg)))
		y = round(cy - radius * sin(radians(angle_deg)))
		points.append((x, y))
	return points


def draw_hexagon(dwg: Drawing) -> None:
	"""Draw a regular hexagon using apothem input as in the original.

	The apothem a relates to circumradius R by R = 2a/sqrt(3).
	"""
	cx = _input_int("Middle point X: ")
	cy = _input_int("Middle point Y: ")
	a = _input_int("Apothem length: ")
	fill = input("Fill color (name or hex, empty for none): ") or None
	stroke = input("Stroke color (name or hex, empty for none): ") or None
	radius = (2 * a) / sqrt(3)
	points = _regular_polygon_points((cx, cy), radius, sides=6, start_angle=30)
	dwg.add(Polygon(points=points, fill=fill, stroke=stroke))


def save_svg(dwg: Drawing) -> None:
	"""Prompt for filename and save the drawing if confirmed."""
	filename = input("Filename (including .svg): ")
	if not filename:
		print("No filename provided. Cancelled saving.")
		return
	print(f'Saving file to "{filename}"')
	proceed = input("Proceed (y/n)?: ")
	if proceed.lower().startswith("y"):
		dwg.save(pretty=True, indent=2)
		print("Vector saved successfully!")
	else:
		print("Save cancelled.")


def main() -> None:
	dwg = Drawing(size=("500px", "500px"))
	menu = (
		"Options:\n"
		"1 - Draw square\n"
		"2 - Draw circle\n"
		"3 - Draw hexagon\n"
		"4 - Save svg\n"
		"0 - Exit"
	)
	print("Program starting.")
	while True:
		print(menu)
		choice = input("Your choice: ")
		if choice == "1":
			draw_square(dwg)
		elif choice == "2":
			draw_circle(dwg)
		elif choice == "3":
			draw_hexagon(dwg)
		elif choice == "4":
			save_svg(dwg)
		elif choice == "0":
			print("Exiting program.")
			break
		else:
			print("Unknown option!")
	print("Program ending.")


if __name__ == "__main__":
	main()
