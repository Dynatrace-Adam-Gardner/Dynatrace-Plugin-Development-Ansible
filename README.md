dynatrace-plugin-development
=========

Ansible role to install a Dynatrace plugin environment on Linux.

Role currently only works with Dynatrace SaaS Environments.

Requirements
------------

- A running AWS AMI linux VM.
- Download the plugin SDK from https://abc123.live.dynatrace.com/#settings/monitoredtechnologies/addextension/addlocal
- Rename ZIP to `plugin-sdk.zip` and place into root of roles `files/` directory

Role Variables
--------------
Change These in vars/main.yml:
- environment_id set to abc123
- api_token set to abcD123eFGh****

Where environment_id is your SaaS URL portion: https://abc123.live.dynatrace.com
Where api_token is found in the installer link at: https://abc123.live.dynatrace.com/#install/agentlinux

No Change Needed:
- plugin_install_directory set to /tmp/plugin
- python_install_directory set to /usr/local/lib/python3.5

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
