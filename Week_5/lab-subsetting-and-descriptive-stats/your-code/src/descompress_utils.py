import os

def descompress_data(zip):
    '''
    This function descompress a .csv file. And drop de .zip
    '''
    csv_file = zip.split(".")[0]
    descompress_zip = f"unzip {zip}"
    print("Descompressing files")
    remove_zip = f"rm -rf {zip}"
    print ("removing .zip")

    for i in [descompress_zip, remove_zip]:
        os.system(i)
    
    move_csv = f"mv {csv_file}.csv yourcode/{csv_file}.csv"
    os.system(move_csv)
    return f"Your file is descompressed. Great!!"