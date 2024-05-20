def t_peticion(t_acceso,t_transferencia):
    return suma(t_acceso) + t_transferencia

def ms_Segundos(ms):
    return ms/1000

print(ms_Segundos(12))

def rpm_rps(rpm):
    return rpm/60

print(rpm_rps(9000))

def lat_rot_Media():
    return 1/(2*rpm_rps(5900))

print(lat_rot_Media)