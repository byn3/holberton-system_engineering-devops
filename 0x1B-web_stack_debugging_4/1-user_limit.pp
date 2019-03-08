# adds tons of workers
exec {'increase':
    command => 'sudo sed -i "s/holberton hard nofile 5\nholberton softnofile 4/holberton hard nofile 5000\nholberton soft nofile 4000" /etc/security/limits.conf;',  # lint:ignore:140chars
    path    => '/etc/security/limits.conf:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
