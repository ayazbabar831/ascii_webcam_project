import numpy as np
def frame_to_ascii(gray):
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    chars = ascii_chars
    bins = np.linspace(0, 256, len(chars) + 1)
    idx = np.digitize(gray, bins) - 1
    return "\n".join("".join(chars[i] for i in row) for row in idx)
