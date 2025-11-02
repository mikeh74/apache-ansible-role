# Apache Ansible Role

A modern, comprehensive Ansible role for installing and configuring Apache HTTP Server on Ubuntu, Debian, and RHEL-based systems.

## Features

- Multi-platform support (Ubuntu, Debian, RHEL/CentOS/Rocky/AlmaLinux)
- Modern Apache configuration with security headers
- SSL/TLS support with modern cipher suites
- Virtual host management
- Firewall configuration (optional)
- Security hardening
- Molecule testing framework

## Requirements

- Ansible >= 2.12
- Python >= 3.8
- Target system: Ubuntu 20.04+, Debian 11+, or RHEL 8+

## Role Variables

### Package Management
```yaml
apache_packages:           # List of Apache packages to install
  - apache2                # Default for Debian/Ubuntu

apache_update_cache: true  # Update package cache before installation
apache_cache_valid_time: 3600  # Cache validity time in seconds
```

### Service Configuration
```yaml
apache_service: apache2    # Apache service name
apache_state: started      # Service state (started/stopped)
apache_enabled: true       # Enable service on boot
```

### Apache Modules
```yaml
apache_modules:            # List of Apache modules to enable
  - rewrite
  - ssl
  - headers
```

### Security Settings
```yaml
apache_server_tokens: "Prod"        # Server tokens setting
apache_server_signature: "Off"      # Server signature setting
apache_ssl_protocol: "all -SSLv3 -TLSv1 -TLSv1.1"  # SSL protocols
apache_ssl_cipher_suite: "ECDHE-ECDSA-AES128-GCM-SHA256:..."  # SSL ciphers
```

### Virtual Hosts
```yaml
apache_remove_default_vhost: false  # Remove default Apache vhost
apache_create_vhosts: true          # Create virtual hosts

virtual_hosts:
  - name: example                    # Virtual host name
    server_name: example.com         # Primary domain
    server_aliases:                  # Additional domains (optional)
      - www.example.com
    server_admin: admin@example.com  # Admin email
    document_root: /var/www/html/example
    listen_port: 80                  # HTTP port
    ssl_enabled: false               # Enable SSL (optional)
    ssl_cert_path: /path/to/cert.crt # SSL certificate path
    ssl_key_path: /path/to/key.key   # SSL private key path
    options: "Indexes FollowSymLinks" # Directory options
    allow_override: "All"            # AllowOverride setting
    extra_config: |                  # Additional Apache config
      # Custom directives here
```

### Firewall Configuration
```yaml
apache_configure_firewall: false    # Configure firewall rules
apache_firewall_zone: "public"      # Firewall zone (RHEL/CentOS)
```

## Dependencies

This role requires the following Ansible collections:
- `community.general`
- `ansible.posix`

Install with:
```bash
ansible-galaxy install -r requirements.yml
```

## Example Playbook

### Basic Installation
```yaml
- hosts: webservers
  become: true
  roles:
    - apache-ansible-role
```

### With Virtual Hosts
```yaml
- hosts: webservers
  become: true
  vars:
    apache_remove_default_vhost: true
    virtual_hosts:
      - name: website
        server_name: www.example.com
        server_aliases:
          - example.com
        server_admin: webmaster@example.com
        document_root: /var/www/html/website
        ssl_enabled: false
      
      - name: secure-site
        server_name: secure.example.com
        server_admin: admin@example.com
        document_root: /var/www/html/secure
        ssl_enabled: true
        ssl_cert_path: /etc/ssl/certs/secure.crt
        ssl_key_path: /etc/ssl/private/secure.key
        
  roles:
    - apache-ansible-role
```

### Advanced Configuration
```yaml
- hosts: webservers
  become: true
  vars:
    apache_modules:
      - rewrite
      - ssl
      - headers
      - expires
      - deflate
    
    apache_configure_firewall: true
    apache_remove_default_vhost: true
    
    virtual_hosts:
      - name: app
        server_name: app.example.com
        document_root: /var/www/html/app
        ssl_enabled: true
        ssl_cert_path: /etc/letsencrypt/live/app.example.com/fullchain.pem
        ssl_key_path: /etc/letsencrypt/live/app.example.com/privkey.pem
        extra_config: |
          # Enable compression
          <Location />
              SetOutputFilter DEFLATE
              SetEnvIfNoCase Request_URI \
                  \.(?:gif|jpe?g|png)$ no-gzip dont-vary
              SetEnvIfNoCase Request_URI \
                  \.(?:exe|t?gz|zip|bz2|sit|rar)$ no-gzip dont-vary
          </Location>
          
          # Security headers
          Header always set Content-Security-Policy "default-src 'self'"
          
  roles:
    - apache-ansible-role
```

## Directory Structure

```
apache-ansible-role/
├── defaults/main.yml          # Default variables
├── handlers/main.yml          # Handlers for service management
├── meta/main.yml             # Role metadata
├── tasks/main.yml            # Main tasks
├── tasks/virtual_hosts.yml   # Virtual host tasks
├── templates/                # Jinja2 templates
│   ├── virtualhost.conf.j2
│   └── virtualhost-ssl.conf.j2
├── vars/                     # OS-specific variables
│   ├── Debian.yml
│   └── RedHat.yml
└── molecule/                 # Testing framework
    └── default/
        ├── molecule.yml
        ├── playbook.yml
        ├── requirements.yml
        └── verify.yml
```

## Testing

This role uses [Molecule](https://molecule.readthedocs.io/) for testing.

### Prerequisites
```bash
pip install molecule[docker] ansible-lint yamllint
```

### Run Tests
```bash
# Test all scenarios
molecule test

# Test specific scenario
molecule test -s default

# Create and converge only
molecule converge

# Run verification only
molecule verify
```

## Security Features

- Modern SSL/TLS configuration with secure cipher suites
- Security headers (HSTS, X-Frame-Options, X-Content-Type-Options, etc.)
- Server information disclosure protection
- Modern directory access controls
- Optional firewall configuration

## Platform Support

| Platform | Versions | Status |
|----------|----------|--------|
| Ubuntu   | 20.04, 22.04, 24.04 | ✅ Supported |
| Debian   | 11, 12 | ✅ Supported |
| RHEL     | 8, 9 | ✅ Supported |
| CentOS   | 8, 9 | ✅ Supported |
| Rocky    | 8, 9 | ✅ Supported |
| AlmaLinux| 8, 9 | ✅ Supported |

## Changelog

### v2.0.0
- Complete modernization for Ansible 2.12+
- Multi-platform support (Debian/Ubuntu/RHEL)
- Modern SSL/TLS configuration
- Security headers and hardening
- Molecule testing framework
- Breaking changes from v1.x

### v1.x
- Legacy version supporting Ubuntu 16.04/18.04
- Basic Apache installation and configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests
5. Run molecule tests
6. Submit a pull request

## License

MIT

## Author Information

This role was created by mhorrocks and modernized in 2025.

For issues and contributions, please visit: [GitHub Repository](https://github.com/mikeh74/apache-ansible-role)