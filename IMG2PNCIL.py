# code by carlos salazar
# made with python 3.9.5 using cv2 4.5.2
# just for fun and learning purposes
import cv2

def convertImage(location,file):
    imageLocation = location
    filename = file

    img = cv2.imread(imageLocation + filename)

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    invertedGrayImg = 255 - grayImg

    blurImg = cv2.GaussianBlur(invertedGrayImg, (21,21), 0)

    invertedBlurImg = 255 - blurImg

    pencilImg = cv2.divide(grayImg,invertedBlurImg, scale = 256.0)

    cv2.imshow("Original",img)
    cv2.imshow("Pencil", pencilImg)
    cv2.waitKey(0)

    cv2.imwrite(filename[:-4] + "_pencil.png",pencilImg)

    print(filename,'converted successfully')
    option()

def option():
    print('¿Do you want to convert another image? \n')
    option = input('Write an "S" for YES, or a "N" for NO: \n>> ').strip().lower()

    attempts = 0

    while option != 's' and option != 'n':

        if attempts == 3:
            print('\nNo more attempts remaining.')
            exit()
        print('\nInvalid option, enter "S" or "N"')
        option = input('>> ').strip().lower()
        attempts += 1

    if option == 's':
        main()

    if option == 'n':
        print("Exiting...")
        exit()

def main():
    print("\nWelcome to IMG2PNCIL: \n")
    print('1) Enter the image location with the format: "/Users/username/Desktop/ImageFolder/"\n')
    print('2) Enter the image filename: "filetopencil.jpg"\n')
    print('IMPORTANT NOTE: supported extentions (.bmp, .dib, .jpeg, .jpg, .jpe, .jp2, .png, .pbm, .pgm, .ppm, .sr, .ras, .tiff, .tif) .ico is not supported :( \n')
    location = str(input("Enter the image location: \n>>"))
    file = str(input("Enter the file name: \n>>"))
    convertImage(location,file)

main()