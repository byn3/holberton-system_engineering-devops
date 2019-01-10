# Terminates the killmenow process
exec {
  'killmenow':
  command =>  '/usr/bin/pkill killmenow'
}
