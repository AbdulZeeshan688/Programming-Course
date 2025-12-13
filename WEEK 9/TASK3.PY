
"""Small utility to print a file's contents with simple headers.

This script accepts a filename via command-line argument or prompts the user.
It prints the file path in a header, then the file contents, then a footer.
"""

from __future__ import annotations

from pathlib import Path
import sys


def read_and_print_file(path: str) -> int:
	"""Read the file at ``path`` and print its contents with headers.

	Returns 0 on success, 1 on failure.
	"""
	p = Path(path).expanduser()
	if not p.exists():
		print(f'File "{p}" does not exist.')
		return 1

	print(f"## {p} ##")
	try:
		text = p.read_text()
	except Exception as exc:  # pragma: no cover - simple CLI handling
		print(f"Couldn't read file '{p}': {exc}")
		return 1

	# Strip a trailing newline but keep internal formatting
	print(text.rstrip())
	print(f"## {p} ##")
	return 0


def main() -> int:
	"""Entry point for the script.

	If a filename is provided as the first CLI argument it will be used.
	Otherwise the user is prompted to type a filename.
	"""
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		try:
			filename = input("Insert filename: ").strip()
		except (EOFError, KeyboardInterrupt):
			print("No filename provided.")
			return 1

	if not filename:
		print("No filename provided.")
		return 1

	return read_and_print_file(filename)


if __name__ == "__main__":
	raise SystemExit(main())

