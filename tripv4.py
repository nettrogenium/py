#trip = TRue IP
def trip(IPv4):
    
    # replace colons with dot to identify port
    IPv4 = IPv4.replace(':', '.')
    
    # check if dots are correct
    try:
        IPv4 = list(map(int, IPv4.split('.')))
    except ValueError:
        return False
    
    # check if port is correct
    if IPv4[4] < 0 or IPv4[4] > 65535: return False
    
    # check if octets are correct
    for i in range(4):
        if IPv4[i] < 0 or IPv4[i] > 255: return False
            
    # if IPv4 is correct, return True    
    return True
