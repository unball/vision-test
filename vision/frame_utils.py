def crop(frame, rect_p0, rect_p1):
    x, xf = (rect_p0[0], rect_p1[0])
    y, yf = (rect_p0[1], rect_p1[1])
    return frame[y:yf, x:xf]
