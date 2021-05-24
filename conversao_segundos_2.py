segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs=int(segundos_str)
dia_str=str

horas=total_segs //3600
if total_segs >= 24:
    dia_str =(total_segs - 24)
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final =  segs_restantes % 60

print (dia_str, "dia[s]", horas, "hora[s]", minutos, "minuto[s] e ", segs_restantes_final, "segundo[s]")
