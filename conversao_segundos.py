segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs=int(segundos_str)

horas=total_segs //3600
segs_restantes = total_segs % 3600
if segs_restantes => 24 dia_int <-24-segs_restantes
minutos = segs_restantes // 60
segs_restantes_final =  segs_restantes % 60

print (dia_int, "dias", horas, "horas", minutos, "minutos e ", segs_restantes_final, "segundos")
