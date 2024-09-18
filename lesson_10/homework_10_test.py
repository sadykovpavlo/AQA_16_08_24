import pytest
from homework_10 import log_event
from logfile_handler import log_file_return_last_log


class TestLogEvenFunction:

    def test_success_login_status_log(self):
        entry_data = ('User_1', 'success')
        expected_data = ['User_1', 'success\n']
        log_event(*entry_data)
        result = log_file_return_last_log('login_system.log')
        assert expected_data[0] in result, expected_data[1] in result

    def test_expire_login_status_log(self):
        entry_data = ('User_1', 'expired')
        expected_data = ['User_1', 'expired\n']
        log_event(*entry_data)
        result = log_file_return_last_log('login_system.log')
        assert expected_data[0] in result, expected_data[1] in result

    def test_another_login_status_log(self):
        entry_data = ('User_1', 'another')
        expected_data = ['User_1', 'another\n']
        log_event(*entry_data)
        result = log_file_return_last_log('login_system.log')
        assert expected_data[0] in result, expected_data[1] in result
