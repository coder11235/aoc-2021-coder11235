import functools
import time

st = time.perf_counter()

@functools.cache
def get_bin(val: str):
    bn = bin(int(val, 16))[2:]
    return "0"*(4-len(bn))+bn

data = open('data.txt', 'r')
version_sum = 0

packet = "".join([get_bin(i) for i in data.read()])

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
"""
def parse_literal(content: str):
    # recusrive function that accepts a literal extra bits towards the end
    def recurse_unpad(cnt):
        # gets the first bit
        first = cnt[0]

        # case to see if its not the last litieral value
        if first == '1':
            return recurse_unpad(cnt[5:])
        else:
            if len(cnt) > 5:
                # return the extra bits
                return cnt[5:]
    
    # return extra bits after the literal or None if there are no bits after it
    return recurse_unpad(content)


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
print(time.perf_counter()-st)