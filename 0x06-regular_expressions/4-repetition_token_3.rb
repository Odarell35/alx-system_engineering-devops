#!/usr/bin/env ruby
regex = /hbt{0,}n/
puts ARGV[0].scan(regex).join
