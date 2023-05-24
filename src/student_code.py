import common
import math #note, for this lab only, you are allowed to import math

def detect_slope_intercept(image):
    # PUT YOUR CODE HERE
    # access the image using "image[y][x]"
    # where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
    # set line.m and line.b
    # to create an auxiliar bidimentional structure 
    # you can use "space=common.init_space(heigh, width)"
    voting_space = common.init_space(2000,2000)  # index by voting_space[m][b]
    for y in range(common.constants.HEIGHT):
        for x in range(common.constants.WIDTH):
            if image[y][x] == 0:  # only check edge pixels, which are black
                for m_index in range(2000):
                    m = -10 + (m_index * 0.01)
                    b = -(x * m) + y
                    #print(f"calculated b to be {b}")
                    if b >= -1000 and b <= 999:
                        b_index = round(b + 1000)
                        #print(f"and b index is {b_index}")
                        voting_space[m_index][b_index] = voting_space[m_index][b_index] + 1

    # find max now
    max_votes = -1
    mmax_idx = 0
    bmax_idx = 0

    for m_index in range(2000):
        for b_index in range(2000):
            if voting_space[m_index][b_index] > max_votes:
                max_votes = voting_space[m_index][b_index]
                mmax_idx = m_index
                bmax_idx = b_index

    mmax = -10 + (mmax_idx * 0.01)
    bmax = -1000 + bmax_idx

    line=common.Line()
    line.m = mmax
    line.b = bmax
    return line

def detect_circles(image):
    # PUT YOUR CODE HERE
    # access the image using "image[y][x]"
    # where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
    # to create an auxiliar bidimentional structure 
    # you can use "space=common.init_space(heigh, width)"
    num_circles = 0
    r = 30
    voting_space = common.init_space(200,200)
    
    for y in range(common.constants.HEIGHT):
        for x in range(common.constants.WIDTH):
            if image[y][x] == 0:  # only check edge pixels, which are black
                for a in range(x-r, x+r):
                    if a >= 0 and a < 200:
                        b1 = round(y + math.sqrt(r**2 - (x-a)**2))
                        if b1 >= 0 and b1 < 200:
                            voting_space[a][b1] = voting_space[a][b1] + 1
                        b2 = round(y - math.sqrt(r**2 - (x-a)**2))
                        if b2 >= 0 and b2 < 200:
                            voting_space[a][b2] = voting_space[a][b2] + 1
    
    threshold = 68
    for a in range(200):
        for b in range(200):
            if voting_space[a][b] >= threshold:
                num_circles += 1

                # to avoid double-counting a circle, clear out the nearby centers
                for da in range(-5, 5):
                    for db in range(-5, 5):
                        voting_space[a+da][b+db] = 0
    
    return num_circles
				
