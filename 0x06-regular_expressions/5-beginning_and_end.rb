#!/usr/bin/env ruby
regex = /h.{0,}n/
puts ARGV[0].scan(regex).join
