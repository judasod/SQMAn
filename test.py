import subprocess
import unittest
from unittest.mock import patch, call


class TestAXFRZoneTransferScript(unittest.TestCase):

    @patch('sys.argv', [''])
    @patch('builtins.print')
    def test_no_arguments_provided(self, print):
    
        exec(open('script.py').read())
        print.assert_called_with('No arguments!')


    @patch('sys.argv', ['', 'example'])
    @patch('subprocess.check_output', return_value=b'host: couldn\'t get address for \'example\': not found')
    def test_unsuccessful_axfr_transfer(self, mock_check_output):
        # Run the script
        subprocess.run(['python', 'script.py'])

        # Last system command
        system_output = mock_check_output.return_value.decode()

        # Assert that the output of the system command contains the expected message
        expected_message = "host: couldn't get address for 'example': not found"
        self.assertIn(expected_message, system_output)




    @patch('sys.argv', ['', 'example.com'])
    @patch('os.system', return_value=0)
    @patch('builtins.print')
    def test_successful_axfr_transfer(self, print, os_system):

        exec(open('script.py').read())
        print.assert_called_with('[*]', 'Searching records for domain: ', 'example.com', '\n')
        
        os_system.assert_any_call('for sv in $(host -t ANY example.com | cut -d " " -f4); do \nhost -l example.com $sv | grep "has addr"\ndone')

        # Assert that 'echo $?' call returns 0
        os_system.assert_called_with('echo $?')


if __name__ == '__main__':
    unittest.main()
