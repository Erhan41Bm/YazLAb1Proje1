import tkinter as tk
import random

class BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Top Hareketi Uygulaması")
        self.root.geometry("1000x600")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #    Pencerenin boyutunu ekran boyutuna ayarla
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Canvas (Çizim Ekranı) oluşturuluyor
        self.canvas = tk.Canvas(self.root, width=1000, height=600, bg='white')
        self.canvas.pack()

        # Kontrol panelini (butonlar ve radiobutton'lar) üst kısma alıyoruz
        control_frame = tk.Frame(self.root)
        control_frame.pack(anchor=tk.CENTER)
        
        # Boyut butonları
        self.small_button = tk.Button(control_frame, text="Küçük", command=lambda: self.set_size(20))
        #/self.small_button.pack(side=tk.RIGHT, padx=5, pady=10,pady=1)
        self.small_button.grid(row=0, column=0, pady=5)  # İlk satır

        # self.red_radio.pack(side=tk.TOP, pady=5)

        self.medium_button = tk.Button(control_frame, text="Orta", command=lambda: self.set_size(30))
        #self.medium_button.pack(side=tk.RIGHT, padx=5, pady=10,pady=2)
        self.medium_button.grid(row=0,column=1,padx=5, pady=10)

        self.large_button = tk.Button(control_frame, text="Büyük", command=lambda: self.set_size(40))
        #self.large_button.pack(side=tk.RIGHT, padx=5, pady=10, pady=3)
        self.large_button.grid(row=0,column=2,padx=5, pady=10)


        # Renk radiobutton'ları
        self.color_var = tk.StringVar(value="red")  # Varsayılan olarak kırmızı seçili

        self.red_radio = tk.Radiobutton(control_frame, text="Kırmızı", variable=self.color_var,fg='red', value="red")
        #self.red_radio.pack(side=tk.RIGHT, padx=5, pady=10)
        self.red_radio.grid(row=1,column=0,padx=5, pady=10)
        
        self.green_radio = tk.Radiobutton(control_frame, text="Yeşil", variable=self.color_var,fg="green", value="green")
        #self.green_radio.pack(side=tk.RIGHT, padx=5, pady=10)
        self.green_radio.grid(row=1,column=1,padx=5, pady=10)

        
        self.blue_radio = tk.Radiobutton(control_frame, text="Mavi", variable=self.color_var,fg="blue", value="blue")
        #self.blue_radio.pack(side=tk.RIGHT, padx=5, pady=10)
        self.blue_radio.grid(row=1,column=2,padx=5, pady=10)


        # Hareket butonları
        self.start_button = tk.Button(control_frame, text="Start", command=self.start_animation)
        #self.start_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.start_button.grid(row=2,column=0,padx=5, pady=10)
        
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_animation)
        #self.stop_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.stop_button.grid(row=2,column=1,padx=5, pady=10)
        
        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset)
        #self.reset_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.reset_button.grid(row=2,column=2,padx=5, pady=10)
        
       

        self.speed_button = tk.Button(control_frame, text="Speed Up", command=self.speed_up)
        #self.speed_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.speed_button.grid(row=0,column=4,padx=25)

        self.istant_speed=tk.Label(control_frame,text="Hız:  0")
        self.istant_speed.grid(row=1,column=4,padx=25)


        self.speed_down_button = tk.Button(control_frame, text="Speed Down", command=self.speed_down)
        #self.speed_down_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.speed_down_button.grid(row=2,column=4,padx=25)

        # Ball özellikleri
        self.balls = []
        self.running = False
        self.speed = 5  # Başlangıç hızı
        self.size = 20  # Varsayılan top boyutu
        self.animation_active = False  # Çift start engellemek için bayrak

    def set_size(self, size):
        """Butonla seçilen boyutu ayarlayan fonksiyon."""
        self.size = size
        self.add_ball()

    def create_ball(self, x, y, r, color):
        """Yeni top oluştur ve canvas'a ekle."""
        ball = {
            "x": x,
            "y": y,
            "r": r,
            "color": color,
            "dx": random.choice([-1, 1]) * self.speed,
            "dy": random.choice([-1, 1]) * self.speed,
            "id": None
        }
        ball["id"] = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
        self.balls.append(ball)

    def start_animation(self):
        if not self.animation_active:  # Eğer animasyon çalışıyorsa tekrar başlatma
            self.running = True
            self.animation_active = True
            self.animate_balls()
        self.istant_speed.config(text="Hız:  "+str(self.speed))
        
    def stop_animation(self):
        self.running = False
        self.animation_active = False
        self.istant_speed.config(text="Hız:  "+str(self.speed))

        
    def reset(self):
        self.running = False
        self.animation_active = False
        self.canvas.delete("all")
        self.speed=5
        self.balls = []
        self.running = False
        self.animation_active = False
        self.istant_speed.config(text="Hız:  "+str(self.speed))

        
    def speed_up(self):
        self.speed += 5
        self.istant_speed.config(text="Hız:  "+str(self.speed))

        for ball in self.balls:
            # Yeni hız değerini toplara uygula
            ball["dx"] = (ball["dx"] / abs(ball["dx"])) * self.speed if ball["dx"] != 0 else self.speed
            ball["dy"] = (ball["dy"] / abs(ball["dy"])) * self.speed if ball["dy"] != 0 else self.speed
        if self.speed>0:
            self.speed_down_button.config(state="normal")
        if self.speed>40:
            self.speed_button.config(state="disabled")

    def speed_down(self):
        self.speed -= 5
        self.istant_speed.config(text="Hız:  "+str(self.speed))

        if self.speed<=0:
            self.speed_down_button.config(state="disabled")
        if self.speed<=40:
            self.speed_button.config(state="normal")
        for ball in self.balls:
            # Yeni hız değerini toplara uygula
            ball["dx"] = (ball["dx"] / abs(ball["dx"])) * self.speed if ball["dx"] != 0 else self.speed
            ball["dy"] = (ball["dy"] / abs(ball["dy"])) * self.speed if ball["dy"] != 0 else self.speed

    def animate_balls(self):
        if self.running:
            for ball in self.balls:
                ball["x"] += ball["dx"]
                ball["y"] += ball["dy"]
                
                # Sınır kontrolü
                if ball["x"] - ball["r"] <= 0 or ball["x"] + ball["r"] >= 1000:
                    ball["dx"] = -ball["dx"]
                if ball["y"] - ball["r"] <= 0 or ball["y"] + ball["r"] >= 600:
                    ball["dy"] = -ball["dy"]
                
                # Canvas'taki topu güncelle
                self.canvas.coords(ball["id"],
                                   ball["x"] - ball["r"], ball["y"] - ball["r"],
                                   ball["x"] + ball["r"], ball["y"] + ball["r"])
            
            self.root.after(30, self.animate_balls)
    
    def add_ball(self):
        # Radiobutton'dan seçilen rengi al
        color = self.color_var.get()
        r = self.size

        # Topların başlangıç pozisyonlarının çakışmamasını kontrol et
        while True:
            x = random.randint(r, 600 - r)
            y = random.randint(r, 600 - r)
            overlap = False
            for ball in self.balls:
                distance = ((ball["x"] - x)**2 + (ball["y"] - y)**2)**0.5
                if distance < ball["r"] + r:  # Çakışma durumu
                    overlap = True
                    break
            if not overlap:
                break

        self.create_ball(x, y, r, color)

# Ana pencereyi oluştur
root = tk.Tk()
app = BallApp(root)

root.mainloop()
