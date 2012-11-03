import unittest

from ..database import construct_mysql_command


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
        full_command = 'mysqldump --user=project --password=pwd --port=3306' \
            ' --host=localhost first_db > /home/backups/mysql_first_db/' \
            'mysql_dump.sql'
        self.assertEqual(construct_mysql_command(self.database), full_command)

    def test_with_socket(self):
        del self.database['db_host']
        self.database['db_socket'] = '/var/run/mysqld/mysqld.sock'
        full_command = 'mysqldump --user=project --password=pwd --port=3306' \
            ' --socket=/var/run/mysqld/mysqld.sock first_db > /home/backups/' \
            'mysql_first_db/mysql_dump.sql'
        self.assertEqual(construct_mysql_command(self.database), full_command)

    def test_minimal_config(self):
        del self.database['backup_dir']
        del self.database['db_host']
        del self.database['db_port']
        del self.database['git_remote']
        full_command = 'mysqldump --user=project --password=pwd first_db' \
            ' > mysql_dump.sql'
        self.assertEqual(construct_mysql_command(self.database), full_command)

    def test_without_db_name(self):
        del self.database['db_name']
        full_command = 'mysqldump --user=project --password=pwd --port=3306' \
            ' --host=localhost > /home/backups/mysql_first_db/mysql_dump.sql'
        self.assertEqual(construct_mysql_command(self.database), full_command)

    def test_without_backup_dir(self):
        del self.database['backup_dir']
        full_command = 'mysqldump --user=project --password=pwd --port=3306' \
            ' --host=localhost first_db > mysql_dump.sql'
        self.assertEqual(construct_mysql_command(self.database), full_command)
