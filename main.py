from fizzbuzz_checker import fizzbuzzChecker

def main():
    print ("Le nombre d'Alice pour Bob: ")
    numAlice = input()
    print(fizzbuzzChecker.is_bob(int(numAlice)))



if __name__ == "__main__":
    # execute only if run as a script
    main()