import segno
from os_path_checker import path_checker


def make_qr(data_to_qr, filename, path_to_save, qr_type=".png"):
    os_path_to_save = path_checker(path_to_save)
    #logo display return
    if len(data_to_qr) == 0 or len(filename) == 0 or len(path_to_save) == 0 or data_to_qr is None or filename is None or path_to_save is None:
        return ".\\input_data_error.png"
    else:
        #sequence creation
        if "-" in data_to_qr:
            data_seq = data_to_qr.split("-")

            #check for an error in the sequence input for generation
            if int(data_seq[0]) > int(data_seq[1]):
                return ".\\sequence_input_error.png"


            #Sequence generation
            for i in range(int(data_seq[0]), int(data_seq[1]) + 1):
                qr_url = os_path_to_save + filename + str(i) + qr_type
                qrcode = segno.make_qr(data_to_qr)
                qrcode.save(qr_url, border=2, scale=5)

                if i == int(data_seq[1]):
                    return qr_url
        else:
            #Single code generation
            qr_url = os_path_to_save + filename + qr_type
            qr_code = segno.make_qr(data_to_qr)
            qr_code.save(qr_url, border=2, scale=5)

            return qr_url