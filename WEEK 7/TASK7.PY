ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift_char(c, offset):
idx = ALPHABET.index(c)
return ALPHABET[(idx + offset) % 26]

class Rotor:
def **init**(self, wiring, position=0):
self.wiring = wiring
self.position = position

```
def forward(self, c):
    idx = (ALPHABET.index(c) + self.position) % 26
    return self.wiring[idx]

def backward(self, c):
    idx = (self.wiring.index(c) - self.position) % 26
    return ALPHABET[idx]

def step(self):
    self.position = (self.position + 1) % 26
```

class Enigma:
def **init**(self, rotor1, rotor2, rotor3, reflector):
self.rotors = [rotor1, rotor2, rotor3]
self.reflector = reflector

```
def encrypt_char(self, c):
    # Rotate rotors
    self.rotors[0].step()
    if self.rotors[0].position == 0:
        self.rotors[1].step()
    if self.rotors[1].position == 0:
        self.rotors[2].step()

    # Forward pass
    for rotor in self.rotors:
        c = rotor.forward(c)
    # Reflect
    c = self.reflector[ALPHABET.index(c)]
    # Backward pass
    for rotor in reversed(self.rotors):
        c = rotor.backward(c)
    return c

def encrypt_message(self, msg):
    encrypted = ""
    for ch in msg.upper():
        if ch in ALPHABET:
            encrypted += self.encrypt_char(ch)
        else:
            encrypted += ch
    return encrypted
```

def main():
print("Program starting.")

```
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

enigma = Enigma(rotor1, rotor2, rotor3, reflector)
input("Insert plugs (y/n)?: n\nNo extra plugs inserted.\nEnigma initialized.\n")

while True:
    row = input("Insert row (empty stops): ")
    if row == "":
        print("Enigma closing.")
        break
    encrypted = enigma.encrypt_message(row)
    print(f"Converted row - \"{encrypted}\".\n")
```

if **name** == "**main**":
main()
