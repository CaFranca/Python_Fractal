def draw_triangle(center, side_length, degrees_rotate, thickness, colour, 
                  pixels, shrink_side_by, iteration, max_depth):

    # The height of an equilateral triangle is, h = ½(√3a) 
    # where 'a' is the side length
    triangle_height = side_length * math.sqrt(3)/2

    # The top corner
    top = [center[0] - triangle_height/2, center[1]]

    # Bottom left corner
    bottom_left = [center[0] + triangle_height/2, center[1] - side_length/2]

    # Bottom right corner
    bottom_right = [center[0] + triangle_height/2, center[1] + side_length/2]

    if (degrees_rotate != 0):
        top = rotate(top, center, degrees_rotate)
        bottom_left = rotate(bottom_left, center, degrees_rotate)
        bottom_right = rotate(bottom_right, center, degrees_rotate)

    # Coordinates between each edge of the triangle
    lines = [[top, bottom_left],[top, bottom_right],[bottom_left, bottom_right]]

    line_number = 0

    # Draw a line between each corner to complete the triangle
    for line in lines:
        line_number += 1

        plot_line(line[0], line[1], thickness, colour, pixels)

        # If we haven't reached max_depth, draw some new triangles
        if (iteration < max_depth and (iteration < 1 or line_number < 3)):
            gradient = (line[1][0] - line[0][0]) / (line[1][1] - line[0][1])

            new_side_length = side_length*shrink_side_by

            # Center of the line of the traingle we are drawing
            center_of_line = [(line[0][0] + line[1][0]) / 2, 
                              (line[0][1] + line[1][1]) / 2]

            new_center = []
            new_rotation = degrees_rotate

            # Amount we need to rotate the traingle by
            if (line_number == 1):
                new_rotation += 60
            elif (line_number == 2):
                new_rotation -= 60
            else:
                new_rotation += 180

            # In an ideal world this would be gradient == 0,
            # but due to floating point division we cannot
            # ensure that this will always be the case
            if (gradient < 0.0001 and gradient > -0.0001):
                if (center_of_line[0] - center[0] > 0):
                    new_center = [center_of_line[0] + triangle_height * 
                                 (shrink_side_by/2), center_of_line[1]]
                else:
                    new_center = [center_of_line[0] - triangle_height * 
                                  (shrink_side_by/2), center_of_line[1]]

            else:

                # Calculate the normal to the gradient of the line
                difference_from_center = -1/gradient

                # Calculate the distance from the center of the line
                # to the center of our new traingle
                distance_from_center = triangle_height * (shrink_side_by/2)

                # Calculate the length in the x direction, 
                # from the center of our line to the center of our new triangle
                x_length = math.sqrt((distance_from_center**2)/ 
                                     (1 + difference_from_center**2))

                # Figure out which way around the x direction needs to go
                if (center_of_line[1] < center[1] and x_length > 0):
                    x_length *= -1

                # Now calculate the length in the y direction
                y_length = x_length * difference_from_center

                # Offset the center of the line with our new x and y values
                new_center = [center_of_line[0] + y_length, 
                              center_of_line[1] + x_length]

            draw_triangle(new_center, new_side_length, new_rotation, 
                          thickness, colour, pixels, shrink_side_by, 
                          iteration+1, max_depth)