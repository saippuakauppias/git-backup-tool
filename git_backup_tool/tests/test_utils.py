import os
import unittest

from ..utils import config_from_file


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')


class ConfigFromFileTests(unittest.TestCase):

    def setUp(self):
        config_file = os.path.join(PROJECT_ROOT, 'fixtures', 'utils',
                                   'config.ini')
        self.config = config_from_file(config_file)

    def tearDown(self):
        del self.config

    def test_count_sections(self):
        self.assertEqual(len(self.config), 2)

    def test_count_in_first_section(self):
        self.assertEqual(len(self.config['first_database']), 7)
        self.assertEqual(len(self.config['second_database']), 5)

    def test_get_config_string(self):
        config = self.config['first_database']
        self.assertEqual(config.get('db_host'), 'localhost')
        self.assertEqual(config.get('db_port'), '3306')
        self.assertEqual(config.get('db_user'), 'project')
        self.assertEqual(config.get('db_password'), 'pwd')
        self.assertEqual(config.get('db_name'), 'first_db')
        self.assertEqual(config.get('backup_dir'),
                         '/home/backups/mysql_first_db')
        self.assertEqual(config.get('git_remote'),
                         'git@github.com/username/privaterepo.git')

        config = self.config['second_database']
        self.assertEqual(config.get('db_host'), 'localhost')
        self.assertEqual(config.get('db_user'), 'project_2')
        self.assertEqual(config.get('db_name'), 'second_db')
        self.assertEqual(config.get('backup_dir'),
                         '/home/backups/mysql_second_db')
        self.assertEqual(config.get('git_remote'),
                         'git@github.com/username/privaterepo2.git')
