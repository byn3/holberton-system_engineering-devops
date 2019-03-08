# adds tons of workers
exec {'increase':
    command => 'sudo sed -i "s/worker_processes 4;/worker_processes 20;worker_rlimit_nofile 3000;/" /etc/nginx/nginx.conf; sudo service nginx restart',  # lint:ignore:140chars
    path    => '/etc/nginx/nginx.conf:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
