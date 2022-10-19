import unittest
from datetime import time

from MessengerLES.client import create_presence_msg, get_message
from MessengerLES.server import process_client_message


class Tests_client(unittest.TestCase):
    def test_client_create_presence_msg(self):
        self.assertEqual(create_presence_msg('user1'), {
        'ACTION': 'PRESENCE',
        'TIME': time(),
        'USER': {'ACCOUNT_NAME': 'user1'},
    })


    def test_test_client_create_presence_msg_ACTION(self):
        self.assertIn(create_presence_msg('user1')
                      ['USER']['ACCOUNT_NAME'], 'user1')


    def test_get_message(self):
        self.assertEqual(get_message('m'), b'm')


    def test_process_client_message(self):
        self.assertEqual(process_client_message('m'),
                         {'400': 'Bad request'})


if __name__ == '__main__':
    unittest.main()