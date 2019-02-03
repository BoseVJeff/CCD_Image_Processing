#Start of Code
#var getout is a Boolean variable, allows printing of output to FITS files if its True, else not
#var getout is required because the function used (*.writeto(<pathname>);) will fail if the file already exists at <pathname>
#All functions, regardless of the state of var getout will return the data as an array of the appropriate dimensions

from astropy.io import fits
import numpy

#Evaluate the Bias correction factor, is obtained as an additive error
#Is done here for 8 bias observations, may be adapted to other numbers with minimal difficulty
def bias(getout):
    img_obj=[0]*8;
    img_data=[0]*8;
    #Importing all images
    #TODO: Make this process work either as loop or over all files in the folder
    img_location="<path_to_file_1>";
    img_obj[0]=fits.open(img_location);
    img_data[0]=img_obj[0][0].data;
    img_location="<path_to_file_2>";
    img_obj[1]=fits.open(img_location);
    img_data[1]=img_obj[1][0].data;
    img_location="<path_to_file_3>";
    img_obj[2]=fits.open(img_location);
    img_data[2]=img_obj[2][0].data;
    img_location="<path_to_file_4>";
    img_obj[3]=fits.open(img_location);
    img_data[3]=img_obj[3][0].data;
    img_location="<path_to_file_5>";
    img_obj[4]=fits.open(img_location);
    img_data[4]=img_obj[4][0].data;
    img_location="<path_to_file_6";
    img_obj[5]=fits.open(img_location);
    img_data[5]=img_obj[5][0].data;
    img_location="<path_to_file_7>";
    img_obj[6]=fits.open(img_location);
    img_data[6]=img_obj[6][0].data;
    img_location="<path_to_file_8>";
    img_obj[7]=fits.open(img_location);
    img_data[7]=img_obj[7][0].data;
    #Using median here because data is prone to having irregular values at end, inner n-tile averages may also work
    bias_data=numpy.median(img_data,axis=0)
    #Print the output file if asked for
    if(getout):
        w2file(bias_data,'Bias/netBias.fits');       #TODO Underscores donot work
    #Close all Data Streams
    for img in img_obj:
        img.close();
    return bias_data;

#Evaluate the flat correction factor, is a multiplicative error
#Requires the Bias data to be evaluated first since it also appears here due to experimental procedure and therefore must be eliminated to get the correct trends
#Is implemented for 5 Flat observations, may be adapted to other cases with minimmal difficulty
def flat(bias_data,getout):
    img_obj=[0]*5
    img_data=[0]*5
    #Import all the files
    
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Flat/flat_R.4565.0.fits";
    img_obj[0]=fits.open(img_location)
    img_data[0]=img_obj[0][0].data;
    img_data[0]=numpy.subtract(img_data[0],bias_data)
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Flat/flat_R.4565.0.fits";
    img_obj[1]=fits.open(img_location)
    img_data[1]=img_obj[1][0].data;
    img_data[1]=numpy.subtract(img_data[1],bias_data)
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Flat/flat_R.4565.0.fits";
    img_obj[2]=fits.open(img_location)
    img_data[2]=img_obj[2][0].data;
    img_data[2]=numpy.subtract(img_data[2],bias_data)
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Flat/flat_R.4565.0.fits";
    img_obj[3]=fits.open(img_location)
    img_data[3]=img_obj[3][0].data;
    img_data[3]=numpy.subtract(img_data[3],bias_data)
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Flat/flat_R.4565.0.fits";
    img_obj[4]=fits.open(img_location)
    img_data[4]=img_obj[4][0].data;
    img_data[4]=numpy.subtract(img_data[4],bias_data)

    flat_data=numpy.mean(img_data,axis=0);
    flat_avg=numpy.mean(flat_data)
    norm_flat_data=numpy.divide(flat_data,flat_avg);
    if(getout):
        w2file(norm_flat_data,'Flat/netFlat.fits')
    return norm_flat_data

def obs(bias_data,flat_data,getout):
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Obj/J0901p3846_R.4577.0.fits";
    img_obj=fits.open(img_location);
    img_data=img_obj[0].data;
    unbias_data=numpy.subtract(img_data,bias_data);
    unbf_data=numpy.divide(unbias_data,flat_data);
    if(getout):
        w2file(unbf_data,"/Obj/final.fits");
    return unbf_data;


def w2file(data,name):
    obj=fits.PrimaryHDU(data);
    obj.writeto('/home/ibac/Downloads/IBAC Research Group/Data/Sample/'+name);
