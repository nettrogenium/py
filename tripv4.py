#trip = TRue IP
def trip(IPv4):
    # checks if there are only 3 dots in the ip
    if IPv4.count('.') < 3 or IPv4.count('.') > 4: return False
    
    # replace colons with dot to identify port
    IPv4 = IPv4.replace(':', '.')
    
    # check if dots are correct
    try:
        IPv4 = list(map(int, IPv4.split('.')))
    except ValueError:
        return False
    
    # checks if there are more ports/octets
    if len(IPv4) > 5: return False
    
    # check if port is correct
    if len(IPv4) == 5:
        if IPv4[4] < 0 or IPv4[4] > 65535: return False
    
    # check if octets are correct
    for i in range(4):
        if IPv4[i] < 0 or IPv4[i] > 255: return False
        
    return True
