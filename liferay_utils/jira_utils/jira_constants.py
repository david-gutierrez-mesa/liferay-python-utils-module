class CustomField:
    Bug_type = 'customfield_10240'
    Epic_Link = 'customfield_10014'
    Fix_Priority = 'customfield_10211'
    QA_Engineer = 'customfield_10227'


class Instance:
    Jira_URL = "https://liferay.atlassian.net"
    Type = "Cloud"


class Status:
    Closed = 'Closed'
    In_Testing = 'In Testing'
    Open = 'Open'
    Ready_for_testing = '10619'


class Strings:
    subtask_automation_test_creation_summary = 'Product QA | Automation Test Creation'
    subtask_check_ux_pm_impedibug_summary = 'Product QA | Test Validation - Assert fix PM/Design bugs'
    subtask_backend_description = '* Fill the Backend coverage on the test scenarios table, created in the parent ' \
                                  'story.\n* Implement the Backend unit and/or integration tests that are missing, ' \
                                  'comparing with the test scenarios table, created in the parent story. '
    subtask_backend_summary = 'Test Scenarios Coverage | Backend'
    subtask_frontend_description = '* Fill the Frontend coverage on the test scenarios table, created in the parent ' \
                                   'story.\n* Implement the Frontend unit and/or integration tests that are missing, ' \
                                   'comparing with the test scenarios table, created in the parent story. '
    subtask_frontend_summary = 'Test Scenarios Coverage | Frontend'
    subtask_round_1_summary = 'Product QA | Test Validation - Round 1'
    subtask_test_creation_summary = 'Test Scenarios Coverage | Test Creation'
    subtask_ux_summary = 'Design QA | UX Review - Round 1'


class IssueTypes:
    Design_Task = 'Design task'
    Technical_Task = 'Technical Task'
    Technical_Testing = 'Technical Testing'
    Testing = 'Testing'


class Transition:
    Closed = 'Closed'
    In_Testing = 'In Testing'
    In_Progress = 'In Progress'
    Ready_for_Product_Review = 'Ready for Product Review'
    Selected_for_development = 'Selected for Development'
