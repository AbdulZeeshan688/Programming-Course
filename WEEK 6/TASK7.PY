"""Simple travel/progress demo.

This script reads a small CSV progress file for a player, decodes
an ROT13 passphrase, attempts to read a message file named
"{next_id}_{passphrase_ciphered}.gkg", decodes it and saves the
plain text. The script is defensive about missing files.

This refactor improves structure and readability while keeping
the original behaviour.
"""

from pathlib import Path
import csv
import codecs
from typing import Dict, List

LOCATIONS: List[str] = [
	"home",
	"Galba's palace",
	"Otho's palace",
	"Vitellius' palace",
	"Vespasian's palace",
]
PROGRESS_FILE = Path("player_progress.txt")


def ensure_progress_file(path: Path) -> None:
	"""Create a starter progress file when missing."""
	if path.exists():
		return
	with path.open("w", newline="") as pf:
		writer = csv.writer(pf, delimiter=";")
		writer.writerow(["current_location", "next_location", "passphrase"])
		# Default starting row: at 0, next is 1, passphrase ROT13("discipline")
		writer.writerow([0, 1, "qvfpvcyvar"])


def read_last_progress(path: Path) -> Dict[str, str]:
	"""Read the last progress row as a dict. Raises ValueError if file is empty."""
	with path.open("r", newline="") as pf:
		rows = list(csv.DictReader(pf, delimiter=";"))
	if not rows:
		raise ValueError("Progress file contains no data")
	return rows[-1]


def rot13(text: str) -> str:
	return codecs.decode(text or "", "rot_13")


def main() -> None:
	ensure_progress_file(PROGRESS_FILE)
	last = read_last_progress(PROGRESS_FILE)

	current_id = int(last["current_location"])
	next_id = int(last["next_location"])
	passphrase_ciphered = last.get("passphrase", "")
	passphrase_plain = rot13(passphrase_ciphered)

	print("Travel starting.")
	print(f"Currently at {LOCATIONS[current_id]}.")
	print(f"Travelling to {LOCATIONS[next_id]}...")
	print(f"...Arriving to the {LOCATIONS[next_id]}.")
	print("Passing the guard at the entrance.")
	print(f'"{passphrase_plain}!"')

	message_file = Path(f"{next_id}_{passphrase_ciphered}.gkg")
	if message_file.exists():
		with message_file.open("r", encoding="utf-8", errors="replace") as mf:
			ciphered_message = mf.readline().strip()
	else:
		ciphered_message = ""

	print("Looking for the message in the palace...")
	if ciphered_message:
		print("Ah, there it is! Seems cryptic.")
	else:
		print("No message file found. Proceeding without message.")

	print("[Game] Progress autosaved!")

	plain_message = rot13(ciphered_message)

	plain_file = Path(f"{next_id}-{passphrase_plain}.txt")
	with plain_file.open("w", encoding="utf-8") as pf:
		pf.write(plain_message)

	# Append next progress row. Keep next passphrase empty by default.
	with PROGRESS_FILE.open("a", newline="") as pf:
		writer = csv.writer(pf, delimiter=";")
		writer.writerow([next_id, min(next_id + 1, len(LOCATIONS) - 1), ""])  # empty passphrase

	print("Deciphering Emperor's message...")
	if plain_message:
		print("Looks like I've got now the plain version copy of the Emperor's message.")
	else:
		print("No plain message was produced.")
	print("Time to leave...")
	print("Travel ending.")


if __name__ == "__main__":
	main()
