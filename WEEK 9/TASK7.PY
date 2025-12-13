import sys
import os
import shutil
from typing import Optional


def show_help() -> None:
	"""Print usage help for the script."""
	print("[USAGE] python TASK7.py src_file dst_file")


def copy_file(src: str, dst: str, force: Optional[bool] = None) -> None:
	"""Copy src to dst.

	If dst exists, prompt the user unless force is True/False.
	"""
	if force is None and os.path.exists(dst):
		choice = input(
			f'Destination file "{dst}" already exists.\n'
			"Do you want to overwrite it? (y/n): "
		)
		if choice.lower() != "y":
			print("Copy cancelled by user.")
			return

	try:
		shutil.copyfile(src, dst)
		print(f'Copied file "{src}" to "{dst}".')
	except FileNotFoundError:
		print(f'Source file "{src}" not found.')
		sys.exit(1)
	except PermissionError:
		print(f'Permission denied when writing to "{dst}".')
		sys.exit(1)
	except Exception as exc:  # pragma: no cover - generic fallback
		print(f'Failed to copy "{src}" to "{dst}": {exc}')
		sys.exit(1)


def main(argv: Optional[list] = None) -> None:
	"""Parse arguments and perform file copy.

	argv: list of arguments (defaults to sys.argv)
	"""
	if argv is None:
		argv = sys.argv

	print("Program starting.")

	if len(argv) != 3:
		print("Invalid number of arguments.")
		show_help()
		sys.exit(2)

	src_file = argv[1]
	dst_file = argv[2]

	if not os.path.exists(src_file):
		print(f'Source file "{src_file}" does not exist.')
		sys.exit(1)

	copy_file(src_file, dst_file)
	print("Program ending.")


if __name__ == "__main__":
	main()
