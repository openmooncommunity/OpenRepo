# OpenMoon by SpaceHub - Random Pieces Generator

# Copyright (c) 2023 SpaceHub. All rights reserved.
#
# Licensed under the MIT License. See LICENSE file
# in the project repository for full license information.

import os
import random
import string


def generate_random_id(length):
    """
    Generate a unique ID of specified length.

    Parameters:
        length (int): Length of the ID to generate.

    Returns:
        str: Generated unique ID.
    """
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def generate_pieces(num_pieces):
    """
    Generate a list of pieces, where each piece is a list of random numbers.

    Parameters:
        num_pieces (int): Number of pieces to generate.

    Returns:
        list: List of pieces, each represented as a list of numbers.
    """
    pieces = []
    for _ in range(num_pieces):
        num_numbers = random.randint(1, 10)
        piece = [str(random.randint(1000, 100000)) for _ in range(num_numbers)]
        pieces.append(piece)
    return pieces


def write_pieces_to_file(pieces, output_dir):
    """
    Write the pieces to the output file in the specified directory.

    Parameters:
        pieces (list): List of pieces to write to the file.
        output_dir (str): Path of the output directory.

    Returns:
        str: Complete path of the created output file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(
        output_dir, f"pieces_{generate_random_id(6)}.txt")
    with open(output_file, 'w') as file:
        for piece in pieces:
            file.write('\n'.join(piece))
            file.write('\n\n')
    return output_file


# Number of pieces to generate
num_pieces = 100

# Output directory
output_dir = 'Outputs'

# Generate the pieces
pieces = generate_pieces(num_pieces)

# Write the pieces to the output file
output_file = write_pieces_to_file(pieces, output_dir)

# Print the path of the created output file
print(f"File '{output_file}' generated successfully!")
