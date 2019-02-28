# puppet script to handle config management of a broken wp site
# error was found in line 137 in wp-settings, extra p: typo

# so first check if the file is there, if so then exec
file {
  '/var/www/html/wp-settings.php':
  ensure => present
  # source => all
}
-> exec {
  'configWPsettings':
  command => 'sed -i --follow-symlinks "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/bin',
  }
