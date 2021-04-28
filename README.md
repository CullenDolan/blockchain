# Blockchain App
Trying to build a full app to deploy on AWS with the flask framework. Using [this blog on HackerNoon](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46) as the guide.

## Definitions
* **Hash** - A function that takes an input value and creates an output value in a deterministic way. The simplest example is *f(x) = y*. And y cannot be reerse engineered to get x.
* **Block** - An object that typically includes an index, timestamp, list of transactions, a proof, and hash of previous block.
* **Transactions** - Part of the block that include the sender, recipient, and amount exchanged.
* **Genesis Block** - Very first blok in the chain that needs to be created manually.
* **SHA-256** - Secure Hash Algorithm, computed with 8 32-bit words. This is important because most computers have a 32-bit or 64-bit architecture, and that is the amount of information a CPU can process each time it performs an operation.
* **Proof of Work** - One party (prover) perform a moderately hard, but feasible computation that is easy to check by another part (varifier).

## Python Libraries Imported
* **hashlib** [[Documentation](https://docs.python.org/3/library/hashlib.html)] - specifically `.sha256()` creates a SHA-256 hash object and `.hexdigest()` returns the data passed to the hass object as a string object of *double* length, containing only hexidecimal digits.
* **json** [[Documentation](https://docs.python.org/3/library/json.html)] - specifically `json.dumps` converts serialized object to JSOM formatted string.
* **uuid** - [[Documentation](https://docs.python.org/3/library/uuid.html)] - immutable unique IDs that come with '-'
* **time** - 


## Python Decorators Used
* **staticmethod** [[Documentation](https://docs.python.org/3/library/functions.html#staticmethod)] - does not receive an implicit first argument
* **property** [[Documentation](https://docs.python.org/3/library/functions.html#property)] - simpler way to implement the property(fget, fset, fdel, doc) built-in function

## Built-in Python Functions and Methods Used
* **.encode()** [[Documentation](https://docs.python.org/3/howto/unicode.html#converting-to-bytes)] - strings are initially stored as Unicode and this method converts the string to UTF-8
* **.append()** [[Documentation](https://docs.python.org/3/tutorial/datastructures.html)] - adds an item to the end of a list
* **.replace()** [[Documentation](https://docs.python.org/3/library/stdtypes.html#str.replace)] - returns a copy of the original string w/ the new string
