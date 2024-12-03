import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
from PIL import Image
class TestECSOF:
    resultados = []
     # Inicializar el driver de Chrome
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/ECSOF/public')
        time.sleep(2)
    def teardown_method(self):
        pass
#Inicio de sesion
    def test_reservar_despues_de_iniciar_sesion(self):
        driver = self.driver
        #Inicio de sesion
        driver.find_element(By.XPATH, "//*[@id='app']/div/header/div/nav[2]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("cliente@example.com")

        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Password.1")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/form/div[4]/button").click()
        time.sleep(2)
        TestECSOF.resultados.append("Inicio de sesión: PASS")
        #reservas
        driver.find_element(By.XPATH, "//*[@id='ubicacionDeLimpieza']/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='subservice']/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='status']/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='city']/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div/div/div/div/main/div[2]/a").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[1]/ul/li[1]/div/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[1]/ul/li[1]/div/div/div[1]/div/input").send_keys("2")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[1]/ul/li[2]/div/input").click()
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[1]/ul/li[2]/div/div/div[1]/div/input").send_keys("3")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[1]/ul/li[3]/div/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div/div/div/form/div[2]/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[2]/form/div[1]/div/div/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/table/tbody/tr[3]/td[5]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[2]/form/div[2]/div/button[7]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[2]/form/div[3]/button").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='map']/div[2]/div[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='caracteristicas']").send_keys("casa Blanca")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='numero_lugar']").send_keys("555")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[3]/div[2]/button").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div/div/div[4]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div[2]/div/div[3]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='aceptar-terminos']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div/div/div[6]/button[2]").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        TestECSOF.resultados.append("Reserva: PASS")
        #fin reserva
        #Historial
        driver.find_element(By.XPATH, "//*[@id='app']/div/nav/div/div[1]/div[1]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div/div/div/div/div[2]/div/div[2]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/main/div/div/div/div[4]/button[2]").click()
        time.sleep(2)
        TestECSOF.resultados.append("Historial: PASS")
        #Fin Historial
        #Cerrar sesion
        driver.find_element(By.XPATH, "//*[@id='app']/div/nav/div/div[2]/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/nav/div/div[2]/div/div/button").click()
        time.sleep(2)
        TestECSOF.resultados.append("Cerrar sesion: PASS")
        driver.quit()
        #fin cerrar sesion
    def test_registro(self):
        driver = self.driver
        #registro
        driver.find_element(By.XPATH, "//*[@id='app']/div/header/div/nav[2]/a[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='nombre']").send_keys("Amira")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='apellido']").send_keys("Troche")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='email']").send_keys("automatizacion1@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='edad']").send_keys("22")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='celular']").send_keys("777888965")
        time.sleep(1)
        ruta_imagen = r"C:\Users\amira\OneDrive\Imágenes\perfil.jpg"
        driver.find_element(By.XPATH, "//*[@id='foto_perfil']").send_keys(ruta_imagen)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Password.1")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='password_confirmation']").send_keys("Password.1")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/form/div[9]/button").click()
        time.sleep(2)
        TestECSOF.resultados.append("Registro: PASS")
        #fin registro
        #editar perfil
        driver.find_element(By.XPATH, "//*[@id='app']/div/nav/div/div[2]/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/nav/div/div[2]/div/div/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='nombre']").send_keys(" Angi")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='apellido']").send_keys(" Vene")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[1]/form/div[4]/button").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='current_password']").send_keys("Password.1")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Password.2")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='password_confirmation']").send_keys("Password.2")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/form/div[4]/button").click()
        time.sleep(2)
        ruta_imagen1 = r"C:\Users\amira\OneDrive\Imágenes\perfil1.png"
        driver.find_element(By.XPATH, "//*[@id='foto_perfil']").send_keys(ruta_imagen1)
        time.sleep(1)
        driver.quit()
        TestECSOF.resultados.append("Editar perfil: PASS")
        #fin editar perfil
    def print_results(self):
        yield
        print("\nResumen de pruebas:")
        for resultado in TestECSOF.resultados:
            print(resultado)

