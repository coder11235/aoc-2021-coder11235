import math
import functools

@functools.cache
def get_bin(val: str):
    bn = bin(int(val, 16))[2:]
    return "0"*(4-len(bn))+bn

data = open('data.txt', 'r').read().strip()

packet = "".join([get_bin(i) for i in data])

def clear_padding_zeroes(packet: str):
    # remove 0s at end
    last_0 = packet.rindex("0")
    return packet[:last_0]

packet = clear_padding_zeroes(packet)

"""
accepts the content of a literal with soe extra data

parses a literal

returns the part of the content that isnt part of the ltieral
if it used all the content then it returns None
also returns the value of the literal
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
    
    # res is the extra/ None value for the extra chars
    res = recurse_unpad(content)
    return res, int(bits, 2)

"""
accepts the content of the packet and all ahead of it and its length

splits the data into the correct content and parses it

returns the extra
"""
def parse_first_operator(content: str, length: int):
    disc = content[length:]
    content = content[:length]
    values = []
    # if the content is None that means it encountered a literal packet which used up all data and ended the packet
    while content is not None:
        content, value = basic_parse(content)
        values.append(value)
    if disc != '':
        return disc, values
    else:
        return None, values

def parse_second_operator(content: str, length: int):
    count = 0
    values = []
    while count < length:
        content, value = basic_parse(content)
        values.append(value)
        count += 1
    if content != '':
        return content, values
    else:
        return None, values

def basic_parse(packet: str):
    type_id = int(packet[3:6], 2)
    packet = packet[6:]
    if type_id == 4:
        return parse_literal(packet)
    else:
        lti = packet[0]
        extra = None
        values: list = []
        if lti == '0':
            length = int(packet[1:16], 2)
            extra, values = parse_first_operator(packet[16:], length)
        else:
            length = int(packet[1:12], 2)
            extra, values = parse_second_operator(packet[12:], length)
        val = 0
        if type_id == 0:
            val = sum(values)
        elif type_id == 1:
            val = math.prod(values)
        elif type_id == 2:
            val = min(values)
        elif type_id == 3:
            val = max(values)
        elif type_id == 5:
            val = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            val = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            val = 1 if values[0] == values[1] else 0
        return extra, val

print(basic_parse(packet)[1])