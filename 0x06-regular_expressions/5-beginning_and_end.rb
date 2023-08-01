#!/usr/bin/env ruby
regex = /h.{0,1}n/
puts ARGV[0].scan(regex).join
