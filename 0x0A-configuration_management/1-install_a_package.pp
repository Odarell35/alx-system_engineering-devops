# Ensure pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Use pip3 to install Flask
exec { '1-install_a_package.pp':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
