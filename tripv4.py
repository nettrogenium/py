# currently checks only ip w/o port (127.0.0.1:4444 -> False)
# trip = TRue IP
def trip(IPv4):
    try:
        IPv4 = list(map(int, IPv4.split('.')))
    except ValueError:
        return False
    for i in range(4):
        if IPv4[i] < 0 or IPv4[i] > 255: return False
        
    return True
    
print(trip(input()))
    
