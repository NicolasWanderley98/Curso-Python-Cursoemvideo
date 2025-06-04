times = ('Flamengo','Cruzeiro','Bragantino', 'Palmeiras',
         'Fluminense','Bahia','Mirassol','Atlético-MG','Botafogo'
             ,'Ceará','Corinthians','Grêmio','São Paulo',
         'Internacional','Vasco','Vitória','Fortaleza','Santos',
         'Juventude','Sport')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatros útimos são {times[-4:]} ')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O vasco está na {times.index("Vasco")+1}° posição')