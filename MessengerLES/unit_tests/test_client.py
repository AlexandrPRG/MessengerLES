import sys
sys.path.append('../')
import unittest
from common.msg_utils import create_presence_msg, get_message, process_client_message
from client import socket

class Tests_client(unittest.TestCase):
    def test_client_create_presence_msg(self):
        self.assertEqual(create_presence_msg('user1'),
                         {'action': 'presence',
                          'time': 1.1,
                          'user': {'account_name': 'user1'}
                          },
    )

    def test_client_create_presence_msg_ACTION(self):
        self.assertIn(create_presence_msg('user1')
                      ['user']['account_name'], 'user1')


    # def test_get_message(self):
    #     self.assertEqual(get_message(socket), b'm')


    def test_process_client_message(self):
        self.assertEqual(process_client_message('m'),
                         {'400': 'Bad request'})


if __name__ == '__main__':
    print(f'{sys.path=}')
    unittest.main()
