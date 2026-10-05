from django.test import TestCase
from django.urls import reverse

class SumaFormTestCase(TestCase):
    def test_pagina_y_calculo_suma(self):
        # 1. Obtener la URL de la página
        url = reverse('sumar')
        print(f"\nEnlace a la pagina de suma: http://127.0.0.1:8000{url}")
        
        # 2. Verificar que la página carga correctamente
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        # 3. Enviar datos desde los campos de texto
        response_post = self.client.post(url, {'num1': 5, 'num2': 10})
        self.assertEqual(response_post.status_code, 200)
        
        # 4. Validar el resultado
        self.assertEqual(response_post.context['resultado'], 15.0)
        print("La prueba del formulario y el calculo de la suma fue exitosa.")