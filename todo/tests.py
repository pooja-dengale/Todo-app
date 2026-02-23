from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user,
            priority='high'
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.priority, 'high')
        self.assertFalse(task.completed)
        
    def test_task_str(self):
        task = Task.objects.create(title='My Task', user=self.user)
        self.assertEqual(str(task), 'My Task')

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_list.html')
        
    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Task description',
            'priority': 'medium',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        
    def test_task_update_view(self):
        task = Task.objects.create(title='Old Title', user=self.user)
        response = self.client.post(reverse('task_update', args=[task.id]), {
            'title': 'Updated Title',
            'priority': 'high',
            'completed': True
        })
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Title')
        self.assertTrue(task.completed)
        
    def test_task_delete_view(self):
        task = Task.objects.create(title='Delete Me', user=self.user)
        response = self.client.post(reverse('task_delete', args=[task.id]))
        self.assertEqual(Task.objects.count(), 0)
        
    def test_user_can_only_see_own_tasks(self):
        other_user = User.objects.create_user(username='other', password='pass123')
        Task.objects.create(title='My Task', user=self.user)
        Task.objects.create(title='Other Task', user=other_user)
        
        response = self.client.get(reverse('task_list'))
        self.assertEqual(len(response.context['page_obj']), 1)
        
    def test_search_functionality(self):
        Task.objects.create(title='Python Task', user=self.user)
        Task.objects.create(title='Django Task', user=self.user)
        
        response = self.client.get(reverse('task_list') + '?search=Python')
        self.assertEqual(len(response.context['page_obj']), 1)
        
    def test_filter_by_status(self):
        Task.objects.create(title='Task 1', user=self.user, completed=True)
        Task.objects.create(title='Task 2', user=self.user, completed=False)
        
        response = self.client.get(reverse('task_list') + '?status=completed')
        self.assertEqual(len(response.context['page_obj']), 1)

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_login_required_for_task_list(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
        
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
