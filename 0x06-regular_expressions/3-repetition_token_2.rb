#!/usr/bin/env ruby
regex = /hbt{1,}n/
puts ARGV[0].scan(regex).join
