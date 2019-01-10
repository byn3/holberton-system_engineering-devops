# Using Puppet, install puppet-lint. ensure present or latest but we want 2.1.1
package{
  'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
