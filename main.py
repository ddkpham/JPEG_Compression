
import argparse
from PIL import Image
import numpy as np
#To grab arguments from input

def file_inputs():
    import argparse
    #Calls an instance of the argument Parser
    parser = argparse.ArgumentParser(description='Process input file path and export file path')
    #add arguments for input file and output file
    #Positional Arguments 
    parser.add_argument('input_file', type=str, help='relative path to the input image from current directory')
    parser.add_argument('output_file', type=str, help='relative path to the input image from current directory')
    #parse through arguments and put into arg
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    return input_file, output_file

#Takes an image in file_path and retuns image with rgb->yuv pixel value conversion
def rgb_to_yuv(file_path):
    from PIL import Image
    img = Image.open(file_path)
    pixels = img.load() #Create Pixel map

    width = img.size[0]
    height = img.size[1]

    #RGB -> YUV conversion 
    for i in range(width):
        for j in range(height):
            r = pixels[i,j][0]
            g = pixels[i,j][1]
            b = pixels[i,j][2]
            y = 0.299*r + 0.587*g + 0.114*b
            u = 0.492* (b-y)
            v = 0.877 * (r-y)
            pixels[i,j] = (int(y),int(u),int(v))
    return img

#applys a 4:2:0 chroma subsampling to image
def chroma_ss_process(img):
    width = img.size[0]
    height = img.size[1]
    pixels = img.load()
    #find chroma block size 
    #chroma_blocksize = (width * height) / 8 
    #Try resizing image N x N -> M x M where M < N

    for i in range(width):
        for j in range(height):
            if(i%2==0):
                pixels[i,j] = pixels[i,j][0]
            else:
                if(j%2==0):
                    pass
                else:
                    #EMPTY value 
                    pixels[i,j] = 0
    
    return img

def main():
    input , output = file_inputs()
    print("input file name = " + str(input))
    print("output file name = " + str(output))

    
    image = rgb_to_yuv(input)
    ss_image = chroma_ss_process(image)
    
    npmat = np.array(ss_image, dtype=np.uint8)

    rows, cols = npmat.shape[0], npmat.shape[1]
    print("rows = " + str(rows))
    print("cols = " + str(cols))
    
    #Create block sizes 
    if(rows%8 ==0 and cols%8==0):
        block_seg = (rows * cols) /64
    else:
        raise ValueError(("the width and height of the image "
                          "should both be mutiples of 8"))
    
    #Iterate through array in an 8x8 block 
    for i in range(0, rows, 8):
        for j in range(0, cols, 8):
            for k in range(3):
                if(len(npmat[i,j]==1)):
                    pass
                else:
                    #scale data to center around 0
                    block = npmat[i:i+8, j:j+8, k] - 128
        
        
    ###CHROMOSUBSAMPLING
    ## How do to the 4:2:0 subsampling 

    #img = Image.fromarray(block, 'RGB')
    print(block_seg)
    #img.show()
    ss_image.show()





    
    
#Checks to see if this is the main module being run
if __name__ == '__main__':
    main()


    