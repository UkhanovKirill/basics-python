from time import sleep

class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается на \n '
                  f'{TrafficLight._color[i]}')
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(2)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()