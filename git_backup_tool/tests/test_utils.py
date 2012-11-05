import os
import unittest

from ..utils import config_from_file, construct_dump_command


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
        self.assertEqual(config.get('db_socket'),
                         '/var/run/mysqld/mysqld.sock')
        self.assertEqual(config.get('db_user'), 'project_2')
        self.assertEqual(config.get('db_name'), 'second_db')
        self.assertEqual(config.get('backup_dir'),
                         '/home/backups/mysql_second_db')
        self.assertEqual(config.get('git_remote'),
                         'git@github.com/username/privaterepo2.git')


class ConstructMySQLCommandTests(unittest.TestCase):

    def setUp(self):
        self.database = {
            'backup_dir': '/home/backups/mysql_first_db',
            'db_host': 'localhost',
            'db_name': 'first_db',
            'db_password': 'pwd',
            'db_port': '3306',
            'db_user': 'project',
            'git_remote': 'git@github.com/username/privaterepo.git'
        }

    def tearDown(self):
        del self.database

    def test_full_command_from_database(self):
        full_command = ['mysqldump', '--user=project', '--password=pwd',
                        '--port=3306', '--host=localhost', 'first_db', '>',
                        '/home/backups/mysql_first_db/mysql_dump.sql']
        self.assertEqual(construct_dump_command(self.database, 'mysql'),
                         full_command)

    def test_with_socket(self):
        del self.database['db_host']
        self.database['db_socket'] = '/var/run/mysqld/mysqld.sock'
        full_command = ['mysqldump', '--user=project', '--password=pwd',
                        '--port=3306', '--socket=/var/run/mysqld/mysqld.sock',
                        'first_db', '>',
                        '/home/backups/mysql_first_db/mysql_dump.sql']
        self.assertEqual(construct_dump_command(self.database, 'mysql'),
                         full_command)

    def test_minimal_config(self):
        del self.database['backup_dir']
        del self.database['db_host']
        del self.database['db_port']
        del self.database['git_remote']
        full_command = ['pg_dump', '--format=plain', '--password=pwd',
                        '--username=project', 'first_db', '>',
                        'pgsql_dump.sql']
        self.assertEqual(construct_dump_command(self.database, 'pgsql'),
                         full_command)

    def test_without_db_name(self):
        del self.database['db_name']
        full_command = ['mysqldump', '--user=project', '--password=pwd',
                        '--port=3306', '--host=localhost', '>',
                        '/home/backups/mysql_first_db/mysql_dump.sql']
        self.assertEqual(construct_dump_command(self.database, 'mysql'),
                         full_command)

    def test_without_backup_dir(self):
        del self.database['backup_dir']
        full_command = ['pg_dump', '--format=plain', '--password=pwd',
                        '--port=3306', '--host=localhost',
                        '--username=project', 'first_db', '>',
                        'pgsql_dump.sql']
        self.assertEqual(construct_dump_command(self.database, 'pgsql'),
                         full_command)
