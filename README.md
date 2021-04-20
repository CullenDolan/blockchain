# Blockchain App
Trying to build a full app to deploy on AWS with the flask framework. Using [this blog on HackerNoone](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46) as the guide.

## Definitions
* **Hash** - A function that takes an input value and creates an output value in a deterministic way. The simplest example is *f(x) = y*. And y cannot be reerse engineered to get x.
* **Block** - An object that typically includes an index, timestamp, list of transactions, a proof, and hash of previous block.
* **Transactions** - Part of the block that include the sender, recipient, and amount exchanged.
