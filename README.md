# MAC Address Analyzer

A simple Python tool for validating and analyzing MAC addresses.

This project was created as a learning project to better understand MAC addresses, hexadecimal and binary numbers, OUI, NIC, and bitwise operations.

## Features

* Validate MAC addresses without using Regular Expressions
* Support `:` and `-` separators
* Check the number of MAC address groups
* Check the length of each group
* Validate hexadecimal characters
* Extract OUI
* Extract NIC
* Convert MAC address to Binary
* Convert MAC address to Decimal
* Display MAC address length
* Detect Unicast / Multicast
* Detect Universally / Locally Administered addresses

## MAC Address Structure

A standard MAC address is 48 bits long and contains 6 groups.

Example:

```text
A4:5E:60:12:34:56
```

Each group contains two hexadecimal digits.

Each hexadecimal digit represents 4 bits:

```text
A = 1010
4 = 0100
```

Therefore:

```text
A4 = 10100100
```

Each group contains:

```text
2 × 4 = 8 bits
```

And the complete MAC address contains:

```text
6 × 8 = 48 bits
```

## OUI and NIC

The MAC address can be divided into two main parts:

```text
A4:5E:60:12:34:56
└───────┘ └───────┘
   OUI       NIC
  24 bits    24 bits
```

### OUI

OUI stands for:

**Organizationally Unique Identifier**

The OUI is the first 24 bits of the MAC address and identifies an organization or vendor address block.

Example:

```text
A4:5E:60
```

### NIC

The remaining part of the MAC address is:

```text
12:34:56
```

It is used within the assigned address space to distinguish interfaces.

## Binary Conversion

The program converts every hexadecimal group into exactly 8 bits.

Example:

```text
A4 = 10100100
5E = 01011110
60 = 01100000
12 = 00010010
34 = 00110100
56 = 01010110
```

Result:

```text
10100100:01011110:01100000:00010010:00110100:01010110
```

The program uses:

```python
f"{value:08b}"
```

The `08b` format ensures that every group contains exactly 8 binary digits, including leading zeros.

## Decimal Conversion

The complete MAC address can also be treated as a 48-bit hexadecimal value and converted into a decimal integer.

For example:

```text
A4:5E:60:12:34:56
```

is treated as:

```text
A45E60123456
```

and then converted to Decimal.

## Unicast / Multicast

The first byte contains the I/G bit.

The program checks it using:

```python
FirstByte & 1
```

The result is:

```text
0 → Unicast
1 → Multicast
```

## Universal / Local

The first byte also contains the U/L bit.

The program checks it using:

```python
FirstByte & 2
```

The result is:

```text
0 → Universally Administered
1 → Locally Administered
```

## MAC Address Validation

This project does not use Regular Expressions for validation.

The program checks:

* Number of groups
* Length of each group
* Valid hexadecimal characters
* MAC address structure

Valid examples:

```text
A4:5E:60:12:34:56
A4-5E-60-12-34-56
a4:5e:60:12:34:56
```

Invalid examples:

```text
A4:5E:60:12:34
A4:5E:60:12:34:567
A4:5E:60:12:34:GG
A4:5E:60:12:34:5
A4:5E:60:12:34:56:78
```

## Example

Input:

```text
A4:5E:60:12:34:56
```

Example output:

```text
MAC Address    : A4:5E:60:12:34:56
OUI            : A4:5E:60
NIC            : 12:34:56
Binary         : 10100100:01011110:01100000:00010010:00110100:01010110
Decimal        : ...
Bits           : 48
Type           : Unicast
Administration : Universally Administered
```

## Technologies

* Python 3
* String manipulation
* Functions
* Loops
* Conditional statements
* Hexadecimal conversion
* Binary conversion
* Bitwise operations
* Input validation

## Future Improvements

Possible future features:

* OUI → Vendor lookup
* IEEE OUI database support
* Bit-by-bit visualization
* MAC address generator
* Command-line arguments
* JSON output
* More MAC address formats

## Purpose

This is an educational project created to practice Python programming and understand how MAC addresses work at the bit level.
