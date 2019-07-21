# Apache2 role

This is an ansible role for installing apache2 on Ubuntu

## Requirements

None

## Role Variables

These are the default variables for this role

```yaml
apache_packages: []
```

A list of packages to install for apache

```yaml
apache_modules: []
```

A list of modules to enable

```yaml
apache_service: string
```

The name of the apache service to start and restart the service 

Defaults to 'apache2'

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - role: apache
```

## License

MIT
