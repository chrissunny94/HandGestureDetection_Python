
import cv2
import os
import scipy
import scipy.misc
import Image

import numpy as np
import numpy.linalg as lin



# list file directories
basedir = 'gallery/'
flist = os.listdir(basedir)
print(np.size(flist))


# Count of faces in the database
L = np.size(flist)

# create zero array
arr = np.zeros((L, 24576))
avg = np.zeros((150,125))
conc = np.zeros((150,125))
temp = np.zeros((150,125))
avg1 = np.zeros((150*125,L))
avg2 = np.zeros((150*125,L))
num = 0

# load data matrix out of PGM files
# convert it into a column matrix
# Join all the columns

count =0
for f in flist:
     # construct target
     tfile = basedir + str(f)
     
     try:
        print "Opening:", tfile
        im = Image.open( tfile )
        print( np.shape(im) )




        avg = avg + im
        
        print "Storing image in memory matrix"
        for i in xrange(im.size[0]):
           for j in xrange(im.size[1]):
              pix = im.getpixel((i,j))
              arr[num,i+j*im.size[0]] = (pix[0] + pix[1] + pix[2])/3
        num += 1
     except:
        pass

#Finding the avg face
avg = avg/L

base='eigenvectors/'


temp = np.zeros((150,125))

for f in flist:
     # construct target
     tfile = basedir + str(f)
     
     try:
        print "eigenvectors:", tfile

        im = Image.open( tfile )
        
        temp = im - avg 
        avg1[:,count] = np.reshape( temp  , (150*125, 1) )
        count= count + 1 
        cv2.imwrite("eigenvectors/" + f,temp)
        cov=np.cov(temp)
        cv2.imwrite("cov/" + f,cov)

        conc = conc + temp*(np.transpose(temp))


        
        
     except:
        pass

a = np.array( avg1 )
b = np.array(np.transpose( avg1 ))
cv2.imwrite("god/" + f, a.dot(b) )
conc =  conc/17


#cv2.imshow("Cov",np.transpose(avg))
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite("cov/avg_cov.png",conc)




arr = arr / 256

print(np.shape(avg))
#cv2.imshow("hello",avg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite("avg/avg.png",avg)
# subtract the mean image from each image sample
for i in xrange(arr.shape[0]):
    arr[i,:] = arr[i,:] - arr.mean(0)


# compute SVD of the data matrix
print "Computing sparse SVD of data matrix"
U, V, T = lin.svd(arr.transpose(), full_matrices=False)

# print eigenfaces to files
#print "Writing eigenvectors to disk..."
#for i in xrange(L):
#   scipy.misc.imsave('eigenface_' + str(i) + '.png', U[:,i].reshape(192,128))

