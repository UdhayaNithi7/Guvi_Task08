#Q1-3 calculate the Area & Perimeter of the Circle using Class

class Circle:
    def __init__(self,list_1,pi):
        self.list_1 = list_1    # List of radii
        self.pi = pi            # Value of pi

    def area(self):
        are_li = []     # List to store calculated areas
        s = 0 
        for i in self.list_1:
            s = ((self.pi) * (i**2))
            are_li.append(s)
        return are_li

    def peri(self):
        peri_li = []    # List to store calculated perimeters
        p = 0
        for j in self.list_1:
            p = 2 * self.pi * j
            peri_li.append(p)
        return peri_li

perform = Circle(list_1 = [10,501,22,37,100,999,87,351], pi = 3.141)
area_1 = perform.area()
peri_1 = perform.peri()
print("Areas of given Radius: ", area_1)
print("Perimeter of the given Radius: ", peri_1)



class Tv:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 45000  
        self.inches = 32  
        self.on = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
Entertain = Tv("Sony")
Entertain.increase_volume()
Entertain.set_channel(63)
print(Entertain.status())



class LED(Tv):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    
    def led_status(self):
        return f"{self.brand} in LED type \n screen_thickness : {self.screen_thickness} \n energy_usage: {self.energy_usage} \n lifespan: {self.lifespan} \n refresh_rate: {self.refresh_rate}"
    
tv_type = LED("Sony", 5, 100, 5, 120)
print(tv_type.led_status())

class PLASMA(Tv):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
    
    def plasma_status(self):
        return f"Screen Thickness: {self.screen_thickness}mm \n Energy Usage: {self.energy_usage}W \n Lifespan: {self.lifespan} years \n Refresh Rate: {self.refresh_rate}Hz \n Viewing Angle: {self.viewing_angle} degrees \n Backlight: {self.backlight}"

tv_type1 = PLASMA("LG", 7, 150, 6, 60, 180, "RGB")
print(tv_type1.plasma_status())