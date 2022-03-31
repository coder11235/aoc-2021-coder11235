import functools

@functools.cache
def get_bin(val: str):
    bn = bin(int(val, 16))[2:]
    return "0"*(4-len(bn))+bn

data = open('data.txt', 'r').read().strip()
versions = []
packet = ''

version_sum = 0

for i in data:
    packet += get_bin(i)

def clear_padding_zeroes(packet: str):
    # remove 0s at end
    packet = packet[::-1]
    newpacket = ""
    encountered = False
    for i in packet:
        if not encountered:
            if i != '0':
                encountered = True
                newpacket += i
        else:
            newpacket += i
    return newpacket[::-1]

packet = clear_padding_zeroes(packet)

"""
accepts the content of a literal with soe extra data

parses a literal

returns the part of the content that isnt part of the ltieral
if it used all the content then it returns None
"""
def parse_literal(content: str):
    bits = ''

    # recusrive function that accepts a literal and extra
    def recurse_unpad(cnt):
        # trims the first bit
        first = cnt[0]
        cnt = cnt[1:]
        nonlocal bits

        # case to see if its not the last litieral value
        if first == '1':
            bits += cnt[0:4]
            rest = cnt[4:]
            val = recurse_unpad(rest)
            # return None back if it used up everything or else return the extra content
            if val is not None:
                return val
        else:
            # if it used up the entire literal
            if len(cnt) == 4:
                bits += cnt[0:4]
            # if it did but it also has to take some more bits to get a multiple of 4
            elif len(cnt) < 4:
                rem = 4-len(cnt)
                bits += cnt + '0'*rem
            # if it didnt use up the entire literal and has some extra left
            else:
                bits += cnt[0:4]
                extra = cnt[4:]
                # return the extra bits
                return extra
        # return None because it used up everything
        return None
    
    # res is the extra/ None value for the extra chars
    res = recurse_unpad(content)
    return res

"""
accepts the content of the packet and all ahead of it and its length

splits the data into the correct content and parses it

returns the extra
"""
def parse_first_operator(content: str, length: int):
    disc = content[length:]
    content = content[:length]
    # if the content is None that means it encountered a literal packet which used up all data and ended the packet
    while content is not None:
        content = basic_parse(content)
    if disc != '':
        return disc
    else:
        return None

def parse_second_operator(content: str, length: int):
    count = 0
    while count < length:
        content = basic_parse(content)
        count += 1
    if content != '':
        return content
    else:
        return None

def basic_parse(packet: str):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]
    global version_sum
    version_sum += version
    if type_id == 4:
        return parse_literal(packet)
    else:
        lti = packet[0]
        if lti == '0':
            length = int(packet[1:16], 2)
            return(parse_first_operator(packet[16:], length))
        else:
            length = int(packet[1:12], 2)
            return(parse_second_operator(packet[12:], length))

basic_parse(packet)
print(version_sum)