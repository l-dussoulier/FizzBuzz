class fizzbuzzChecker:

    @staticmethod
    def is_bob(num):
        if (num == 0):
            raise NameError('valeur égal zéro')
            return True
        if (num < 0):
            raise NameError('valeur négative')
            return True
        return False