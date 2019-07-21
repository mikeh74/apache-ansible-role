import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_apache_is_installed(host):
    apache = host.package("apache2")
    assert apache.is_installed
    assert apache.version.startswith("2.4")


def test_apache_running_and_enabled(host):
    apache = host.service("apache2")
    assert apache.is_running
    assert apache.is_enabled
