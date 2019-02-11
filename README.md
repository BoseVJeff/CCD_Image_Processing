# CCD_Image_Processing
Code to process image obtained from CCDs

This code aims to process the image obatined from telescopes observing the nightsky, made esp for the CCD based obervatories.
The code relies on two pieces of pre-observation data - 1. Dark Bias Observation 2. Flat Observation

<b>Dependencies</b>
1. Numpy - For manipulation of data matrices
2. Astropy (Specifically astropy.io.fits flies) - For accessing FITS files and to output the results as FITS files

<b>Using the Code</b>
Invoke the main() function to run the program. Optionally, provide arguments to not get output FITS files
For ganular control,
Invoke the test1.bias(out) function and store the result in var b(say)
Then invoke test1.flat(b,out) and store the result in var f(say)
Then invoke test1.obs(b,f,out) for the final result
The optional argument 'out' in each of the functions is boolean and allows the function to print the output as a FITS file.
