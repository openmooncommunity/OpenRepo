# OpenMoon by SpaceHub - Calculating Piece Sums

# Copyright (c) 2023 SpaceHub. All rights reserved.
#
# Licensed under the MIT License. See LICENSE file
# in the project repository for full license information.

# Input file path
input_path = "./Inputs/input.txt"

# Read the contents of the input file as a string
content = File.read(input_path)

# Divides the content into chunks using one blank line as a delimiter
pieces = content.split("\n\n")

# Converts each piece to an array of integers
pieces = pieces.map do |piece|
  lines = piece.split("\n")
  integers = lines.map(&:to_i)
  integers
end

# Calculates the sum of each piece
sums = pieces.map do |piece|
  sum = piece.sum
  sum
end

# Sort sums in descending order
sorted_sums = sums.sort.reverse

# Select first three sums
top_sums = sorted_sums[0..2]

# Calculate the sum of the three highest sums
total_sum = top_sums.sum

# Print result
puts total_sum
