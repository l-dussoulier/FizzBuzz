class fizzbuzzChecker:

    @staticmethod
    def is_bob(num):
        if (num == 0 or num < 0):
            raise NameError('Exeption')
            return True
        num_div_three = num % 3 == 0
        num_div_five = num % 5 == 0
        if ( num_div_three or num_div_five):
            return True
        if (num_div_three and num_div_five):
            return True
        else:
            print (num)
            return False