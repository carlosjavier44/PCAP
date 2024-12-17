from time import sleep

segundos = 0

while True:
    try:
        print(segundos)
        segundos+=1
        sleep(1)
    except KeyboardInterrupt:
        print('No hagas eso!!!!, saliendo...')
        break
        