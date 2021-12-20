binmaps = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

data = 'A0016C880162017C3686B18A3D4780'


versions = []

nd = ''

for i in data:
    nd += binmaps[i]

def parse_packet(nd):

    # discard remaining
    data = reversed(nd)
    trd = False
    nd = ""
    for i in data:
        if i == "0" and not trd: continue
        nd += i
        trd = True
    nd = nd[::-1]

    # #append till 5s
    # extra = len(nd)%5
    # if extra == 0: extra = 5
    # nd = "0"*(5-extra) + nd

    #fetch version and type
    version = int(nd[:3], 2)
    versions.append(version)
    nd = nd[3:]
    type_id = int(nd[:3], 2)
    nd = nd[3:]

    if type_id == 4:
        # discard first bit of every 5 bits
        def recsplit(arr: str):
            if len(arr) < 5:
                return arr[1:]
            nr = arr[1:5]
            rest = arr[5:]
            return nr + recsplit(rest)
        value = int(recsplit(nd), 2)

        # debug
        print(f"literal packet ve:{version}, ti:{type_id}, v:{value}")
    else:
        # perform operator operations
        len_type_id = nd[:1]
        nd = nd[1:]
        print(f"op ve: {version}, lentype: {len_type_id}")
        if len_type_id == '1':
            l = int(nd[:11], 2)
            nd = nd[11:]
            lpp = len(nd)//l
            sub = []
            def recursesplit(arr: str, sub: list, lpp: int):
                if len(arr) < lpp:
                    return
                first = arr[:lpp]
                sub.append(first)
                rest = arr[lpp:]
                recursesplit(rest, sub, lpp)
            recursesplit(nd, sub, lpp)
            for i in sub:
                parse_packet(i)
        else:
            l = int(nd[:15], 2)
            print(l, nd)
            nd = nd[15:]
            print(l, nd)
            first_packet = nd[:11]
            nd = nd[11:]
            if l > 11:
                parse_packet(first_packet)
                parse_packet(nd)
            else:
                parse_packet(first_packet)


parse_packet(nd)
print(versions)
print(sum(versions))