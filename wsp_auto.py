from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

#Lista de contactos (Hardcodeada)
contactos = {
	"+54 9 11 0000-0000": "Hola desde el bot. Feliz navidad.", #Formato de contacto
	"Nombre de un grupo": "Hola desde un bot. Feliz navidad.", #Formato de grupo
}

def iniciar_driver():
	ser = Service('./driver/chromedriver_linux')
	opt = webdriver.ChromeOptions()
	opt.add_argument(r"user-data-dir=./driver/data")
	global driver
	driver = webdriver.Chrome(service = ser, options = opt)
	driver.get("https://web.whatsapp.com/")
	time.sleep(20)

def enviar_mensajes():

	try:

		for nombre, mensaje in contactos.items():

			# Busca el contacto
			boton_buscador = driver.find_element(By.CLASS_NAME, "_28-cz")
			boton_buscador.click()
			time.sleep(1)

			# Escribir el nombre del contacto
			input_buscador = driver.find_element(By.CLASS_NAME, "_13NKt")
			input_buscador.send_keys(nombre)
			time.sleep(2)

			# Seleccionar el usuario (Presionar enter)
			input_buscador.send_keys(Keys.ENTER)
			time.sleep(2)

			# Enviar el mensaje
			driver.find_element(By.CLASS_NAME, "_1LbR4").send_keys(mensaje)

			# Boton de enviar
			driver.find_element(By.CLASS_NAME, "_4sWnG").click()

			time.sleep(3)

	except:
		s = input("¿Matar al bot? (K)")
		if s == "K" or s == "k":
			driver.quit()
		else:
			enviar_mensajes()


if __name__ == '__main__':

	# Cual es la hora a la que hay que iniciar el bot?
	print("Formato de hora: hh:mm (24h)")
	hora = int(input("Hora de inicio: ? "))
	minuto = int(input("Minuto de inicio: ? "))

	while True:

		# Cual es la hora actual?
		hora_actual = time.localtime().tm_hour
		minuto_actual = time.localtime().tm_min

		# Si es la hora que queremos, avisar y comenzar a enviar mensajes
		if hora_actual == hora and minuto_actual == minuto:
			iniciar_driver()
			enviar_mensajes()
			break

		# Si no es la hora que queremos, esperar un 10s y volver a revisar
		else:
			time.sleep(10)
