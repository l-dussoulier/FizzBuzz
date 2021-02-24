class fizzbuzzChecker:

    @staticmethod
    def is_bob(num):
        if (num == 0 or num < 0):
            raise NameError('Exeption')
            return True
        if (num % 3 == 0 or num % 5 == 0):
            return True
        if (num % 3 == 0 and num % 5 == 0):
            return True
        return False