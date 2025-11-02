# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2025-11-02

### Added
- Multi-platform support for Ubuntu 20.04+, Debian 11+, and RHEL/CentOS 8+
- OS-specific variable files (vars/Debian.yml, vars/RedHat.yml)
- Modern SSL/TLS configuration with secure cipher suites
- Security headers (HSTS, X-Frame-Options, X-Content-Type-Options, etc.)
- Apache security hardening (ServerTokens, ServerSignature)
- Firewall configuration support for RHEL-based systems
- Comprehensive virtual host management with SSL support
- GitHub Actions CI/CD pipeline
- Molecule testing framework with Docker support
- Ansible-lint and yamllint configuration
- Collection dependencies (community.general, ansible.posix)
- Document root auto-creation for virtual hosts
- Support for custom Apache directives per virtual host
- Server aliases support for virtual hosts
- SSL certificate validation

### Changed
- **BREAKING**: Minimum Ansible version requirement from 2.4 to 2.12
- **BREAKING**: Updated template variable from `item` to `vhost` for clarity
- **BREAKING**: Modernized variable naming conventions
- **BREAKING**: Dropped support for Ubuntu 16.04 and 18.04
- Updated from deprecated `with_items` to modern `loop` syntax
- Changed from `service` module to `systemd` for better control
- Updated from `apt` to `package` module for cross-platform compatibility
- Migrated to Fully Qualified Collection Names (FQCN) for all modules
- Enhanced virtual host templates with modern Apache 2.4 syntax
- Improved handlers with systemd support and reload capabilities
- Updated Molecule configuration for modern testing practices
- Comprehensive documentation rewrite with usage examples

### Fixed
- Deprecated Apache 2.2 directory access control syntax
- Template syntax compatibility with modern Jinja2
- Role metadata compliance with Ansible Galaxy requirements
- YAML formatting and linting issues

### Security
- Disabled insecure SSL protocols (SSLv3, TLSv1, TLSv1.1)
- Implemented modern cipher suites (ECDHE-ECDSA-AES128-GCM-SHA256)
- Added comprehensive security headers
- Server information disclosure protection
- Modern directory access controls

### Removed
- Support for Ubuntu 16.04 and 18.04 (end of life)
- Deprecated Apache 2.2 configuration syntax
- Legacy Molecule configuration

## [1.x] - Legacy

### Features
- Basic Apache installation for Ubuntu 16.04/18.04
- Simple virtual host management
- Basic module enabling
- Minimal configuration options

---

## Migration Guide from 1.x to 2.0

### Prerequisites
1. Upgrade to Ansible 2.12 or later
2. Install required collections: `ansible-galaxy install -r requirements.yml`

### Variable Changes
```yaml
# Old (1.x)
virtual_hosts:
  - name: test
    server_name: example.com
    document_root: /var/www/html/

# New (2.0)
virtual_hosts:
  - name: test
    server_name: example.com
    document_root: /var/www/html/
    ssl_enabled: false
    options: "Indexes FollowSymLinks"
    allow_override: "All"
```

### Template Changes
If you have customized templates, update variable references:
- Change `{{ item.* }}` to `{{ vhost.* }}`
- Update Apache configuration syntax to 2.4 format

### New Required Variables
Some variables now have defaults but can be customized:
```yaml
apache_server_tokens: "Prod"
apache_server_signature: "Off"
apache_remove_default_vhost: false
apache_create_vhosts: true
```

### Testing
Use the new Molecule framework to test your configurations:
```bash
molecule test
```