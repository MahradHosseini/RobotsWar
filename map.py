import re
import matplotlib.pyplot as plt


def read_map(file_path):
    # Map config data structure
    config = {
        "map_size": None,
        "white_blocks": {},
        "node_coordinates": {}
    }

    # Reading map detail from the file
    with open(file_path, 'r') as file:
        section = None  # Can be map_size, white_blocks, node_coordinates

        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):  # Skip empty lines and comments
                continue

            # Finding the sections
            if line.endswith(':'):
                section = line[:-1]
            elif section == "map_size":
                config["map_size"] = line
            elif section == "white_blocks":
                row, blocks = line.split(':')
                config["white_blocks"][row] = blocks
            elif section == "node_coordinates":
                node, coordinates = line.split(':')
                config["node_coordinates"][node] = coordinates
    white_block_coords = map_config_check(config)
    draw_map(config)
    return white_block_coords


# Checks for possible error like missing a section, coordinates out of ranges, nodes not in white blocks, etc
def map_config_check(config):
    # Checking all sections' existence
    if not ('white_blocks' in config and 'node_coordinates' in config and 'map_size' in config):
        raise ValueError("Configuration must include white_blocks, map_size, and node_coordinates.")

    # Checking map_size format:
    pattern = re.compile(r"^(\d+)x(\d+)$")  # Regular expression for matching the format 'XxY'

    if not pattern.match(config['map_size']):
        raise ValueError("Invalid format for map_size. It should be in 'XxY' format.")

    # Extract map dimensions
    max_x, max_y = map(int, pattern.match(config['map_size']).groups())
    config['map_size'] = (max_x, max_y)

    # Check white blocks coordinates
    for row, blocks in config.get('white_blocks', {}).items():
        row_number = int(row)
        if row_number >= max_y:
            raise ValueError(f"Row number {row_number} in white_blocks exceeds map height.")

        block_groups = blocks.split()  # Split by spaces to get groups of block ranges
        for block_range in block_groups:
            start, end = map(int, block_range.split('-'))
            if start < 0 or end >= max_x:
                raise ValueError(f"Block coordinate {block_range} in row {row} is out of bounds.")

    # Check node coordinates
    for node, coords in config.get('node_coordinates', {}).items():
        x, y = map(int, coords.split(','))
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            raise ValueError(f"Node coordinate ({x},{y}) is out of bounds.")

    # Convert white blocks into a set of coordinates
    white_block_coords = set()
    for row, blocks in config['white_blocks'].items():
        y = int(row)
        block_groups = blocks.split()  # Split by spaces to get groups of block ranges
        for group in block_groups:
            block_ranges = group.split(',')  # Split each group by commas to get individual block ranges
            for block_range in block_ranges:
                start, end = map(int, block_range.split('-'))
                for x in range(start, end + 1):
                    white_block_coords.add((x, y))

    config['white_blocks'] = white_block_coords

    nodes = set()
    # Check each node's coordinates
    for node, coords in config['node_coordinates'].items():
        x, y = map(int, coords.split(','))
        if (x, y) not in white_block_coords:
            raise ValueError(f"Node coordinate ({x},{y}) is not within the white blocks.")
        else:
            nodes.add((node, (x, y)))

    config['node_coordinates'] = {node: (x, y) for node, (x, y) in nodes}

    return config


def draw_map(config):
    x_size, y_size = config['map_size']
    # Create a black map with the given size
    map_grid = [[0 for _ in range(x_size)] for _ in range(y_size)]

    # Fill in the white blocks
    for (x, y) in config['white_blocks']:
        map_grid[y][x] = 1  # Set white block

    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, x_size)
    ax.set_ylim(0, y_size)
    ax.set_xticks(range(x_size + 1))
    ax.set_yticks(range(y_size + 1))
    plt.grid(which='both', color='black', linestyle='-', linewidth=1)

    # Plot the nodes
    for node, coordinates in config['node_coordinates'].items():
        x, y = map(int, coordinates)
        ax.text(x + 0.5, y + 0.5, node, va='center', ha='center')

    # Color the blocks
    for y in range(y_size):
        for x in range(x_size):
            color = 'white' if map_grid[y][x] == 1 else 'black'
            rect = plt.Rectangle((x, y), 1, 1, color=color)
            ax.add_patch(rect)

    # Show the map
    plt.savefig('map.jpg')
    plt.show()
