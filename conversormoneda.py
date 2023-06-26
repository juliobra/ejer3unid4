import requests
import tkinter as tk

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Conversor de Precio")
        
        self.label_precio_dolar = tk.Label(self.ventana, text="Precio en Dólares:")
        self.label_precio_dolar.pack()
        
        self.entry_precio_dolar = tk.Entry(self.ventana)
        self.entry_precio_dolar.pack()
        
        self.btn_convertir = tk.Button(self.ventana, text="Convertir a Pesos", command=self.convertir_a_pesos)
        self.btn_convertir.pack()
        
        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()
    
    def convertir_a_pesos(self):
        try:
            precio_dolar = float(self.entry_precio_dolar.get())
            cotizacion_dolar = self.obtener_cotizacion_dolar()
            precio_pesos = precio_dolar * cotizacion_dolar
            self.label_resultado.config(text=f"Precio en Pesos: {precio_pesos:.2f}")
        except ValueError:
            self.label_resultado.config(text="Ingrese un valor numérico válido")
    
    def obtener_cotizacion_dolar(self):
        try:
            response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
            data = response.json()
            cotizacion = float(data[0]["casa"]["venta"].replace(",", "."))
            return cotizacion
        except (requests.RequestException, ValueError):
            return 0.0
  

app = App()
app.ventana.mainloop()