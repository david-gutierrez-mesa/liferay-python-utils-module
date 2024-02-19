import unittest

from liferay_utils.jira_utils.jira_helpers import initialize_subtask_patch_release
from liferay_utils.jira_utils.jira_liferay import get_jira_connection


class EchoTestMapTests(unittest.TestCase):

    def test_initialize_subtask_patch_release(self):
        try:
            expected = {'project': {'key': 'LPD'}, 'summary': 'LPD-15582 - Validation',
                        'description': 'https://liferay.atlassian.net/browse/LPD-15582',
                        'issuetype': {'name': 'Technical Task'},
                        'parent': {'id': '1038479'}}
            jira = get_jira_connection()
            parent_lps = jira.issue('LPD-16987', fields='id')
            summary = 'LPD-15582'
            sub_task = initialize_subtask_patch_release(parent_lps, summary)
            self.assertEqual(sub_task, expected)
            print(sub_task)

        except Exception:
            self.fail("Test failed unexpectedly!")


if __name__ == '__main__':
    unittest.main()
