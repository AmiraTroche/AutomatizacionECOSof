from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

class TestSIU:
    def setup_method(self):
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get('http://localhost/ECSof/public')
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        
    def test_textCorreo(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        correo = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[1]/label/span')
        assert correo.text == "Correo electrónico", f"Texto encontrado: {correo.text}"
        time.sleep(1)
        
    def test_InputCorreoYContraseña(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(2)
        cuenta = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/div/div[2]/div/button/span')
        assert cuenta.text == "Worker", f"Texto encontrado: {cuenta.text}"
        time.sleep(3)

    def test_TextTitule(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(2)
        reservas = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/h2')
        assert reservas.text == "Reservas Recientes Asignadas", f"Texto encontrado: {reservas.text}"
        time.sleep(3)
        
    def test_TextBoton(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div/div[2]/button').click()
        boton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div[2]/h4')
        assert boton.text == "Detalles Adicionales", f"Texto encontrado: {boton.text}"
        time.sleep(3)
    
    def test_textMaps(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div/div[2]/button').click()
        self.driver.execute_script("document.body.style.zoom='80%'")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div[2]/div/a[1]').click()
        time.sleep(1)
        boton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/h2')
        assert boton.text == "Ubicación de la Reserva", f"Texto encontrado: {boton.text}"
        time.sleep(3)

    def test_botonMapsVolver(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div/div[2]/button').click()
        self.driver.execute_script("document.body.style.zoom='80%'")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div[2]/div/a[1]').click()
        time.sleep(3)
        boton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/button')
        assert boton.text == "Volver", f"Texto encontrado: {boton.text}"
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/button').click()
        time.sleep(3)

    def test_botonIr(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/nav[2]/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("worker.workerap@miempresa.com")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password.1")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div/div[2]/button').click()
        self.driver.execute_script("document.body.style.zoom='80%'")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div[2]/div/a[1]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div/div[2]/button').click()
        time.sleep(1)
        self.driver.execute_script("document.body.style.zoom='80%'")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/ul/li/div[2]/div/a[2]').click()
        time.sleep(5)
        text = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]')
        assert text.text.strip() == "NOT FOUND", f"Texto encontrado: {text.text.strip()}"
