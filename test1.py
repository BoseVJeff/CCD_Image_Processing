from astropy.io import fits
import os.path
import numpy

def w2file(data,name):
    obj=fits.PrimaryHDU(data);
    path_name='/home/ibac/Downloads/IBAC Research Group/Data/Sample/'+name;
    if(os.path.isfile(path_name)):
        i=1;
        split_path=path_name.split('.')
        while(os.path.isfile(split_path[0]+str(i)+split_path[1])):
            i=i+1;
        obj.writeto(split_path[0]+str(i)+split_path[1]);
    else:
        obj.writeto('/home/ibac/Downloads/IBAC Research Group/Data/Sample/'+name);

def bias(getout=True):
    img_obj=[0]*8;
    img_data=[0]*8;
    #Importing all images
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4560.0.fits";
    img_obj[0]=fits.open(img_location);
    img_data[0]=img_obj[0][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4560.1.fits";
    img_obj[1]=fits.open(img_location);
    img_data[1]=img_obj[1][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4560.2.fits";
    img_obj[2]=fits.open(img_location);
    img_data[2]=img_obj[2][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4561.0.fits";
    img_obj[3]=fits.open(img_location);
    img_data[3]=img_obj[3][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4561.1.fits";
    img_obj[4]=fits.open(img_location);
    img_data[4]=img_obj[4][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4626.0.fits";
    img_obj[5]=fits.open(img_location);
    img_data[5]=img_obj[5][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4626.1.fits";
    img_obj[6]=fits.open(img_location);
    img_data[6]=img_obj[6][0].data;
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias.4626.2.fits";
    img_obj[7]=fits.open(img_location);
    img_data[7]=img_obj[7][0].data;
    
    bias_data=numpy.median(img_data,axis=0);
    if(getout):
        w2file(bias_data,'Bias/net_bias.fits');
    #bias_obj=fits.PrimaryHDU(bias_data);
    #bias_obj.writeto('/home/ibac/Downloads/IBAC Research Group/Data/Sample/Bias/bias_net.fits');
    #Close all Data Streams
    for img in img_obj:
        img.close()
    
    return bias_data;

def flat(bias_data,getout=True):
    img_obj=[0]*5
    img_data=[0]*5
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
        w2file(norm_flat_data,'Flat/net_flat.fits')
    return norm_flat_data

def obs(bias_data,flat_data,getout=True):
    img_location="/home/ibac/Downloads/IBAC Research Group/Data/Sample/Obj/J0901p3846_R.4577.0.fits";
    img_obj=fits.open(img_location);
    img_data=img_obj[0].data;
    unbias_data=numpy.subtract(img_data,bias_data);
    unbf_data=numpy.divide(unbias_data,flat_data);
    if(getout):
        w2file(unbf_data,"/Obj/final.fits");
    return unbf_data;

def main(get_bias=True,get_flat=True,get_obs=True):
    bias=bias(get_bias);
    flat=flat(bias,get_flat);
    final=obs(bias,flat,get_obs);
    return final;
