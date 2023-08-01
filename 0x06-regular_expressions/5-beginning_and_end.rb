#!/usr/bin/env ruby
regex = /h\wn/
puts ARGV[0].scan(regex).join
