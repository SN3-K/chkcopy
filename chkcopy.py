import sys, os, hashlib


class chkcopy:


    def __init__(self,file_name=None,out_name=None,Mb=64):
        arg_check = self.check_arguments()
        if arg_check["argument_bool"] is True:
            self.file_name = arg_check["argument_list"][0]
            self.out_name = arg_check["argument_list"][1]
            self.Mb_name = arg_check["argument_list"][2]
            self.file_name = arg_check["argument_list"][3]
            self.file_name = arg_check["argument_list"][4]
        else:
           self.file_name = file_name
           self.out_name = out_name
           self.Mb = Mb
           self.buff_size = self.Mb * (1024 ** 2)
        # none check
        try:
            self.file_name
            self.out_name
            self.Mb
            self.buff_size
        except NameError as NE:
            print('file_name, out_name, mb, file_name can not be none!')
            exit()



    def read_write(self,md5_name):
        def check_md5():
            pass

        pass


    def check_arguments(self):
        if len sys.argv >1:
            arguments = True
            return {'argument_bool':arguments,'argument_list':sys.argv}

        return
