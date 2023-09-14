class utils:
    def reversed(self, input_number):
        if type(input_number) != int:
            return None
        else:
            if (input_number < 10):
                return(input_number)
            else:
                new_val = str(input_number)[::-1]
                return(int(new_val))
    
    def formatter(self, input_number):
        if type(input_number) != int:
            return None
        else:
            return(bin(input_number), oct(input_number))
