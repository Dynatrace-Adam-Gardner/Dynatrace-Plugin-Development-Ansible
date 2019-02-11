dynatrace-plugin-development
=========

# This is a work in progress and should not be used yet!!

Ansible role to install a Dynatrace plugin environment on Linux.

Role currently only works with Dynatrace SaaS Environments.

Requirements
------------

- A running Amazon Linux AMI 2018.03.0 instance.
- A Dynatrace SaaS tenant.


Role Variables
--------------
Change or override these in defaults/main.yml:
- `environment_id`
- `api_token`
- `plugin_installer_path`
- `plugin_token`

`environment_id` is your SaaS URL portion: https://abc123.live.dynatrace.com

`api_token` is your `InstallerDownload` token from Settings > Integration > Platform as a Service.

`plugin_installer_path` is found like this:
- Visit https://***.live.dynatrace.com/#settings/monitoredtechnologies/addextension/addlocal
- Open chrome dev tools and look for the `ruxitSdkDownloadPath` endpoint
- Copy the `sdkDownloadPath` value eg. `installer/plugin_sdk/Unknown/1.153.218.20180918-135116/***`

`install_demo_data` does the following:
- Installs Apache and PHP
- Creates an index.php page which shows a JSON document and a random number
- Drops the plugin files which pulls the random number once per minute and charts the results in Dynatrace
- Builds and uploads the plugin files to the tenant

`plugin_token` is the specialised plugin development token found at `https://***.live.dynatrace.com/#settings/monitoredtechnologies/customextensions`


Example Playbook
----------------

    ---
    - name: Install Plugin SDK for Dynatrace
      hosts: aws
      
      vars:
        environment_id: ***
        api_token: ***
        plugin_installer_path: installer/plugin_sdk/Unknown/1.***.***.***/***
		install_demo_data: true
		plugin_token: ***

      roles:
        - dynatrace_adam_gardner.dynatrace_plugin_development_ansible

License
-------

BSD

Author Information
------------------

Adam Gardner - https://agardner.net