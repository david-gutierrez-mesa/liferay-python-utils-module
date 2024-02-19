# liferay-python-utils-module
Python utils to interact with Liferay systems.

To use it, type the following command in your project root:
```
git submodule add https://github.com/david-gutierrez-mesa/liferay-python-utils-module.git utils
```
After this, a new folder called utils will appear in your project. You need to commit it with your code.

Add following line into you requirements.txt file in order to install all needed dependencies:
```
-r ./utils/requirements.txt
```

To use any function inside this module you need to import it as in this example:
```python
from utils.liferay_utils.jira_utils.jira_liferay import get_jira_connection
```
