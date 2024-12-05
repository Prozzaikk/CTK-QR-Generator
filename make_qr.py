import segno
from os import name as os_name


def make_qr(data_to_qr, filename, path_to_save, qr_type=".png"):

    #logo display return
    if len(data_to_qr) == 0 or len(filename) < 1 or len(path_to_save) < 1:
        return ".\\qr_icon.png"
    else:
        #sequence creation
        if "-" in data_to_qr:
            data_seq = data_to_qr.split("-")

            #check for an error in the sequence input for generation
            if int(data_seq[0]) > int(data_seq[1]):
                return ".\\sequence_input_error.png"

            #checking the path entered by the user for proper operation of the application
            if path_to_save[-1] != "\\" or path_to_save[-1] != "/":
                if os_name == "nt":
                    path_to_save += "\\"
                elif os_name == "posix":
                    path_to_save += "/"

            #Sequence generation
            for i in range(int(data_seq[0]), int(data_seq[1]) + 1):
                qr_url = path_to_save + str(i) + qr_type
                qrcode = segno.make_qr(data_to_qr)
                qrcode.save(qr_url, border=2, scale=5)

                if i == int(data_seq[1]):
                    return qr_url
        else:
            #Single code generation
            # checking the path entered by the user for proper operation of the application
            if path_to_save[-1] != "\\" or path_to_save[-1] != "/":
                if os_name == "nt":
                    path_to_save += "\\"
                elif os_name == "posix":
                    path_to_save += "/"

            qr_url = path_to_save + filename + qr_type
            qr_code = segno.make_qr(data_to_qr)
            qr_code.save(qr_url, border=2, scale=5)

            return qr_url