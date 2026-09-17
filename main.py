Addr = input("Enter MAC Address: ")


def ValidateMAC(Addr):

    if not isinstance(Addr, str):
        return False

    Addr = Addr.strip().replace("-", ":")

    Parts = Addr.split(":")

    if len(Parts) != 6:
        return False

    for Part in Parts:

        if len(Part) != 2:
            return False

        for Char in Part:
            if Char.upper() not in "0123456789ABCDEF":
                return False

    return True


def Analyze(Addr):

    if not ValidateMAC(Addr):
        print("Invalid MAC Address")
        return

    Addr = Addr.strip().replace("-", ":").upper()

    Parts = Addr.split(":")

    OUI = ":".join(Parts[:3])
    NIC = ":".join(Parts[3:])

    Binary = ""

    for Part in Parts:
        Binary += f"{int(Part, 16):08b}:"

    Binary = Binary[:-1]

    Decimal = int(Addr.replace(":", ""), 16)

    FirstByte = int(Parts[0], 16)

    if FirstByte & 1:
        Type = "Multicast"
    else:
        Type = "Unicast"

    if FirstByte & 2:
        Admin = "Locally Administered"
    else:
        Admin = "Universally Administered"

    print("MAC Address    :", Addr)
    print("OUI            :", OUI)
    print("NIC            :", NIC)
    print("Binary         :", Binary)
    print("Decimal        :", Decimal)
    print("Bits           : 48")
    print("Type           :", Type)
    print("Administration :", Admin)


Analyze(Addr)