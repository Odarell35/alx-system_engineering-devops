# increasing file read limit
exec { 'increase ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 160000\"/' /etc/default/nginx",
}

-> exec { 'reset':
    command => 'sudo service nginx restart',
}
