# Apache2 role

This is an ansible role for installing apache2

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

These are the default variables for this role

### apache_packages

A list of packages to install for apache

### apache_modules

A list of modules to enable

### apache_service

The name of the apache service to start and restart the service 

Defaults to 'apache2'

## Example Playbook

    - hosts: servers
      roles:
         - role: apache

## License

MIT
