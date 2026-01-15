from django.test import TestCase
from django.contrib.auth.models import User
from loja.models import Usuario


class UsuarioModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='caio',
            email='caio@test.com',
            password='123456'
        )

    def test_usuario_is_created_when_user_is_created(self):
        """Deve criar automaticamente um Usuario quando um User é criado"""
        usuario = Usuario.objects.get(user=self.user)
        self.assertIsNotNone(usuario)

    def test_usuario_default_values(self):
        """Verifica valores default do model Usuario"""
        usuario = Usuario.objects.get(user=self.user)

        self.assertEqual(usuario.perfil, 2)
        self.assertIsNone(usuario.aniversario)
        self.assertIsNone(usuario.token)
        self.assertIsNotNone(usuario.criado_em)
        self.assertIsNotNone(usuario.alterado_em)

    def test_usuario_str_method(self):
        """__str__ deve retornar o username do User"""
        usuario = Usuario.objects.get(user=self.user)
        self.assertEqual(str(usuario), self.user.username)

    def test_usuario_is_not_deleted_on_user_update(self):
        """Atualizar o User não deve quebrar o Usuario"""
        self.user.first_name = "Caio"
        self.user.save()

        self.assertTrue(
            Usuario.objects.filter(user=self.user).exists()
        )