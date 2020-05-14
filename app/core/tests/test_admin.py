from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "rose.li@xxx.com",
            "rose123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            "test@xxx.com",
            "test123"
        )

    def test_admin_lists(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.email)
        # print(res.content)
        # self.assertContains(res, self.user.password)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        # print(res.content)

    def test_user_create_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        # print(res.content)
