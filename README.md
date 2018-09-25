#### Steps to install on edX platform:

- open cms.env and lms.env or private.py and set FEATURES flags
  
  ```
  "FEATURES": {
    "ENABLE_EXPORT_GIT": true,
    "ENABLE_GIT_AUTO_EXPORT": true
  }
  ```
- Update github.in i.e
  - `-e git+https://github.com/mitodl/edx-git-auto-export.git@v0.1#egg=edx-git-auto-export`
- Update cms/envs/common. Append **INSTALLED_APPS**
    ```    
    # git auto export
    'git_auto_export',
    ```
- Now run `make dev.provision` to install `edx-git-auto-export`. or run

```docker-compose exec lms bash -c 'source /edx/app/edxapp/edxapp_env && cd /edx/app/edxapp/edx-platform && pip install -e git+https://github.com/mitodl/edx-git-auto-export.git@v0.1#egg=edx-git-auto-export'```
- Run server `make dev.up`

#### Studio UI settings
- Open studio then course and go to advance settings.
- Choose field GIT URL and add you OLX git repo. For example `https://github.com/amir-qayyum-khan/test_edx_course.git`.
- Now add a unit for testing and publish it.
- Test commit count increase on your OLX repo.
