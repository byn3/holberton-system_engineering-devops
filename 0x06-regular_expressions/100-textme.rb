#!/usr/bin/env ruby
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
# the first \[ will start from the first left bracker
# the next group is contained in the ()
# we use the optional and look for all from: to: and flags: strings
# we find that match, next we search for all filler with .*?
# after we have whatever filler, we want to stop at ]
# we also have to change join to add a comma
