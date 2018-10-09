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
Change these in vars/main.yml:
- `environment_id`
- `api_token`
- `plugin_installer_path`

`environment_id` is your SaaS URL portion: https://abc123.live.dynatrace.com

`api_token` is your `InstallerDownload` token from Settings > Platform as a Service.

`plugin_installer_path` is found like this:
- Visit https://***.live.dynatrace.com/#settings/monitoredtechnologies/addextension/addlocal
- Open chrome dev tools and look for the `ruxitSdkDownloadPath` endpoint
- Copy the `sdkDownloadPath` value eg. `installer/plugin_sdk/Unknown/1.153.218.20180918-135116/***`


Example Playbook
----------------

    ---
    - name: Install Plugin SDK for Dynatrace
      hosts: aws

      roles:
        - dynatrace_adam_gardner.dynatrace-plugin-development-ansible

License
-------

BSD

Author Information
------------------

Adam Gardner - https://agardner.net
