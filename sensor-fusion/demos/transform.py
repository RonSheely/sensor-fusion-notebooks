    p1 = ax.transLimits.transform((w1_min, v1_min))
    p2 = ax.transLimits.transform((w1_max, v1_max))    

    rect_im = [p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1]]
    im_ax = fig.add_axes(rect_im)
        
