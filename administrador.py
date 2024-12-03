# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
class TestEscof:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/ECSOF/public")
        self.driver.find_element(By.XPATH,"//a[text()=' Inicio De Sesion ']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@aria-label='Correo electrónico']").send_keys("admin@example.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@aria-label='Contraseña']").send_keys("Password.1")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()=' Iniciar sesión ']").click()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print('\nprueba Completada')
    #inicio de Reservas Recientes
    def test_verify_title(self):
        esperado = "Admin Dashboard"
        actual = self.driver.find_element(By.XPATH, "//h2[text()=' Admin Dashboard ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Reservas_Recientes(self):
        esperado = "Ver Detalles"
        actual = self.driver.find_element(By.XPATH, "//button[text()=' Ver Detalles ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    def test_verify_Ver_detalles(self):
        self.driver.find_element(By.XPATH,"//button[text()=' Ver Detalles ']").click()
        time.sleep(2)
        esperado = "Detalle de la Reserva"
        actual = self.driver.find_element(By.XPATH, "//h2[text()=' Detalle de la Reserva ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Asignar_Personal(self):
        self.driver.find_element(By.XPATH,"//button[text()=' Ver Detalles ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()=' Asignar personal ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value=3]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()=' Asignar Trabajadores ']").click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert_text = alert.text
        print(f"Mensaje de alerta: {alert_text}")
        alert.accept()
        esperado = "You're logged in!"
        actual = self.driver.find_element(By.XPATH, "//div[@class='p-6 text-gray-900 dark:text-gray-100']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    #Fin Reservas Recientes
    #Inicio de Registro Empleados
    def test_verify_Registro_Trabajador(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Registro Empleados ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Yute")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='apellido']").send_keys("Teran")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='edad']").send_keys("23")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='celular']").send_keys("51969921218")
        time.sleep(5)
        ruta_foto_perfil = r"C:\Users\yutem\OneDrive\Escritorio\fotoperfil.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='foto_perfil']").send_keys(ruta_foto_perfil)
        time.sleep(2)
        ruta_antecedentes = r"C:\Users\yutem\OneDrive\Escritorio\antecedentes.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='antecedentes']").send_keys(ruta_antecedentes)
        time.sleep(2)
        ruta_factura_luz = r"C:\Users\yutem\OneDrive\Escritorio\facturaluz.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='factura_luz']").send_keys(ruta_factura_luz)
        time.sleep(2)
        ruta_factura_agua = r"C:\Users\yutem\OneDrive\Escritorio\facturaagua.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='factura_agua']").send_keys(ruta_factura_agua)
        time.sleep(2)
        ruta_contrato = r"C:\Users\yutem\OneDrive\Escritorio\contrato.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='contrato']").send_keys(ruta_contrato)
        time.sleep(2)
        ruta_carta_responsabilidad = r"C:\Users\yutem\OneDrive\Escritorio\carta.jpg"
        self.driver.find_element(By.XPATH, "//input[@id='carta_responsabilidad']").send_keys(ruta_carta_responsabilidad)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@value=9]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button//span[text()='Registrar Trabajador']").click()
        time.sleep(2)
        esperado = "Reservas Recientes Asignadas"
        actual = self.driver.find_element(By.XPATH, "//h2[text()=' Reservas Recientes Asignadas ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_CRUD(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Registro Empleados ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//SPAN[text()='Ir al CRUD']").click()
        time.sleep(2)
        esperado = "Administración de Empleados"
        actual = self.driver.find_element(By.XPATH, "//span[text()='Administración de Empleados']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"

    def test_verify_CRUD_Editar(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Registro Empleados ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//SPAN[text()='Ir al CRUD']").click()
        time.sleep(2)
        #self.driver.find_element(By.XPATH,"").click()
        #time.sleep(2)
        esperado = "Editar"
        actual = self.driver.find_element(By.XPATH, "//tr[td[1][text()='Yute'] and td[2][text()='Teran']]//a[contains(@href, 'edit')]").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    #Fin de Registro de empleados
    #Inicio de Agregar Servicios
    def test_verify_Agergar_servicios(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        esperado = "Administración de Servicios"
        actual = self.driver.find_element(By.XPATH, "//span[text()='Administración de Servicios']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"

    def test_verify_Agregar_Especialidad(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Agregar Especialidad']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("prueba")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@id='ubicacion']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value=4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Guardar Especialidad']").click()
        time.sleep(2)
        esperado = "prueba"
        actual = self.driver.find_element(By.XPATH, "//tr[td[2][text()='prueba'] and td[3][text()='Jardineria']]").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Editar_especialidades(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tr[td[2][text()='prueba'] and td[3][text()='Jardineria']]//a").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("modificado")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Actualizar Especialidad']").click()
        time.sleep(2)
        esperado = "pruebamodificado"
        actual = self.driver.find_element(By.XPATH, "//tr[td[2][text()='modificado'] and td[3][text()='Jardineria']]").text.strip()
        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Eliminar_Servicios(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tr[td[2][text()='modificado'] and td[3][text()='Jardineria']]//button").click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert_text = alert.text
        print(f"Mensaje de alerta: {alert_text}")
        alert.accept()
        # Verificar que la fila con texto "modificado" ya no está en la tabla
        elementos = self.driver.find_elements(By.XPATH, "//tr[td[text()='pruebamodificado']]")
        assert len(elementos) == 0, "La fila no fue eliminada correctamente."

    def test_verify_Agregar_tarea(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Agregar Tarea']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("prueba")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='descripcion']").send_keys("relleno")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='costo']").send_keys(10)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='tiempo']").send_keys(25)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@id='especialidad']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value=10]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Guardar Tarea']").click()
        time.sleep(2)
        esperado = "prueba"
        actual = self.driver.find_element(By.XPATH, "//tr[td[2][text()='pruebamodificado'] and td[3][text()='relleno']]").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Editar_Tarea(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tr[td[2][text()='prueba'] and td[3][text()='relleno']]//a").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("modificado")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Actualizar Tarea']").click()
        time.sleep(2)
        esperado = "pruebamodificado"
        actual = self.driver.find_element(By.XPATH, "//tr[td[2][text()='pruebamodificado'] and td[3][text()='relleno']]").text.strip()
        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    
    def test_verify_Eliminar_Tarea(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Agregar Servicios ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tr[td[2][text()='modificado'] and td[3][text()='relleno']]//button").click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert_text = alert.text
        print(f"Mensaje de alerta: {alert_text}")
        alert.accept()
        # Verificar que la fila con texto "modificado" ya no está en la tabla
        elementos = self.driver.find_elements(By.XPATH, "//tr[td[text()='pruebamodificado']]")
        assert len(elementos) == 0, "La fila no fue eliminada correctamente."
    #Fin de Agregar Servicios
    #Inicio de Historial de Servicios Realizados
    def test_verify_Agergar_servicios(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Historial de Servicios Realizados ']").click()
        time.sleep(2)
        esperado = "Admin Dashboard"
        actual = self.driver.find_element(By.XPATH, "//h2[text()=' Admin Dashboard ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    #Fin de Historial de Servicios Realizados
    #Inicio de Servicios Disponibles
    def test_verify_Agergar_servicios(self):
        self.driver.find_element(By.XPATH,"//div[@class='hidden sm:flex space-x-6']//a[text()=' Servicios en Proceso ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Limpieza Interna")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@id='ubicacion']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value=3]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Crear Grupo']").click()
        time.sleep(2)
        esperado = "Limpieza Interna -"
        actual = self.driver.find_element(By.XPATH, "//h4[text()='Limpieza Interna - ']").text.strip()

        assert esperado == actual, f"FAIL: actual: {actual}, esperado: {esperado}"
    #Fin de Servicios Disponibles
    #Inicio de logout
    def test_verify_logout(self):
        self.driver.find_element(By.XPATH,"//button[text()=' Cerrar Sesión ']").click()
        time.sleep(2)
    #Fin de logout