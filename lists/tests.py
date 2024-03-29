from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from unittest.mock import patch
import django.contrib.auth.decorators
import importlib
import lists

from .views import user_lists
from .models import List, Item

# Create your tests here.
class ListTest(TestCase):

    def test_list_view(self):
        found = resolve('/user-list')
        self.assertEqual(found.func, user_lists)

    # def test_elements_in_template(self):
    #     request = HttpRequest()
    #     response = user_lists(request)
    #     html = response.content.decode('utf-8')
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertIn('Create a list', html)
    #     self.assertTrue(html.endswith('</html>'))

    @patch('django.contrib.auth.decorators.login_required')
    def test_can_save_a_list(self):
        print(django.contrib.auth.decorators.login_required('test1'))
        importlib.reload(django.contrib.auth.decorators)
        print(django.contrib.auth.decorators.login_required('test2'))
        importlib.reload(lists)
        response = self.client.post(
            '/user-list', data={'list_name': 'A New List'})
        self.assertEqual(List.objects.count(), 1)
        new_list = List.objects.first()
        self.assertEqual(new_list.name, 'A New List')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/user-list')
        patch.stopall()
        importlib.reload(lists)


    def test_created_lists_appear_in_dom(self):
        List.objects.create(name='listOne')
        List.objects.create(name='listTwo')

        response = self.client.get('/user-list')
        self.assertIn('listOne', response.content.decode())
        self.assertIn('listTwo', response.content.decode())

    # TO-DO: Add test to see if user is logged int and creating lists

    # def test_created_items_for_list(self):
    #     first_list = List.objects.create(name='listOne')

    #     Item.objects.create(content='itemOne', list_parent=first_list)
    #     Item.objects.create(content='itemTwo', list_parent=first_list)
    #     response = self.client.get('/user-list')
    #     self.assertIn('itemOne', response.content.decode())
    #     self.assertIn('itemTwo', response.content.decode())
        
class ListModelTest(TestCase):
    def test_saving_and_retrieving_lists(self):
        first_list = List(name='My First List')
        first_list.save()

        list_one_item_one = Item(content='item1', list_parent=first_list)
        list_one_item_two = Item(content='item2', list_parent=first_list)
        list_one_item_one.save()
        list_one_item_two.save()

        second_list = List(name='My Second List')
        second_list.save()

        list_two_item_one = Item(content='item3', list_parent=second_list)
        list_two_item_two = Item(content='item4', list_parent=second_list)
        list_two_item_one.save()
        list_two_item_two.save()

        saved_lists = List.objects.all()
        self.assertEqual(saved_lists.count(), 2)

        first_saved_list = saved_lists[0]
        second_saved_list = saved_lists[1]

        self.assertEqual(first_saved_list.name, 'My First List')
        self.assertEqual(second_list.name, 'My Second List')

        self.assertEqual(list_one_item_one.content, 'item1')
        self.assertEqual(list_one_item_one.list_parent, first_list)
        self.assertEqual(list_one_item_one.list_parent.id, first_list.id)

        self.assertEqual(list_one_item_two.content, 'item2')
        self.assertEqual(list_one_item_two.list_parent, first_list)
        self.assertEqual(list_one_item_two.list_parent.id, first_list.id)

        self.assertEqual(list_two_item_one.content, 'item3')
        self.assertEqual(list_two_item_one.list_parent, second_list)
        self.assertEqual(list_two_item_one.list_parent.id, second_list.id)

        self.assertEqual(list_two_item_two.content, 'item4')
        self.assertEqual(list_two_item_two.list_parent, second_list)
        self.assertEqual(list_two_item_two.list_parent.id, second_list.id)
