import bcrypt
import nltk
import time

class User:
    def __init__(self, name, salt, hash) -> None:
        self.name = name
        self.salt = salt
        self.hash = hash

def main():
    wordList = []
    for x in nltk.corpus.words.words():
        if len(x) < 10 and len(x) >= 6:
            wordList.append(x.encode())

    users = [User("Bilbo", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"),
                User("Gandalf", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC"),
                User("Thorin", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.", "$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q"),
                User("Fili", "$2b$09$M9xNRFBDn0pUkPKIVCSBzu", "$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm"),
                User("Kili", "$2b$09$M9xNRFBDn0pUkPKIVCSBzu", "$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im"),
                User("Balin", "$2b$10$xGKjb94iwmlth954hEaw3O", "$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom"),
                User("Dwalin", "$2b$10$xGKjb94iwmlth954hEaw3O", "$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be"),
                User("Oin", "$2b$10$xGKjb94iwmlth954hEaw3O", "$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK"),
                User("Gloin", "$2b$11$/8UByex2ktrWATZOBLZ0Du", "$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q"),
                User("Dori", "$2b$11$/8UByex2ktrWATZOBLZ0Du", "$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq"),
                User("Nori", "$2b$11$/8UByex2ktrWATZOBLZ0Du", "$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12"),
                User("Ori", "$2b$12$rMeWZtAVcGHLEiDNeKCz8O", "$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O"),
                User("Bifur", "$2b$12$rMeWZtAVcGHLEiDNeKCz8O", "$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK"),
                User("Bofur", "$2b$12$rMeWZtAVcGHLEiDNeKCz8O", "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O"),
                User("Durin", "$2b$13$6ypcazOOkUT/a7EwMuIjH.", "$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay")]

    passwords = []

    for u in [users[0]]:
        
        start_time = time.time()
        for choice in wordList:
            
            if bcrypt.hashpw(choice, u.salt.encode()) == u.hash.encode():
                end_time = time.time() - start_time
                passwords.append([u.name, choice, end_time])


    print(passwords)







if __name__ == "__main__":
    main()