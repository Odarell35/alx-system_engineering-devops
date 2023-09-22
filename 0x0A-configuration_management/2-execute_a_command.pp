exec { '2-execute_a_command':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin', '/usr/sbin', '/sbin'],
}
