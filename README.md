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

```docker-compose exec studio bash -c 'source /edx/app/edxapp/edxapp_env && cd /edx/app/edxapp/edx-platform && pip install -e git+https://github.com/mitodl/edx-git-auto-export.git@v0.1#egg=edx-git-auto-export'```
- Run server `make dev.up`

#### If using vagrant or local env:
 If you're testing from a vagrant machine running devstack, you'll need to generate SSH keys in that
machine and add them to your Github account 
(https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/ - 
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account)

#### Studio/CMS UI settings
- Open studio then course and go to advance settings.
- Choose field GIT URL and add you OLX git repo. For example `https://github.com/amir-qayyum-khan/test_edx_course.git`.
- Make a change to the course content and publish.
- Test commit count increase on your OLX repo.
