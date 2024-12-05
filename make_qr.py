import segno
from os import name as os_name


def make_qr(data_to_qr, filename, path_to_save, qr_type=".png"):

    if len(data_to_qr) == 0 or len(filename) < 1 or len(path_to_save) < 1:
        return ".\\qr_icon.png"
    else:

        if "-" in data_to_qr:
            data_seq = data_to_qr.split("-")
            if path_to_save[-1] != "\\":
                if os_name == "nt":
                    path_to_save += "\\"
                elif os_name == "posix":
                    path_to_save += "/"


            if int(data_seq[0]) > int(data_seq[1]):
                return ".\\sequence_input_error.png"

            for i in range(int(data_seq[0]), int(data_seq[1]) + 1):
                qr_url = path_to_save + str(i) + qr_type
                qrcode = segno.make_qr(data_to_qr)
                qrcode.save(qr_url, border=2, scale=5)

                if i == int(data_seq[1]):
                    return qr_url
        else:
            if path_to_save[-1] != "\\":
                path_to_save += "\\"

            qr_url = path_to_save + filename + qr_type
            qr_code = segno.make_qr(data_to_qr)
            qr_code.save(qr_url, border=2, scale=5)

            return qr_url