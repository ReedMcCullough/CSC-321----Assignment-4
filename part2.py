import bcrypt
import nltk
import time


# [['Bilbo', b'welcome', 1557.7713930606842]]
# [['Gandalf', b'wizard', 1565.0937330722809], ['Thorin', b'diamond', 376.1382632255554], ['Fili', b'desire', 739.19926404953]
# ['Kili', b'ossify', 1823.756455898285], ['Balin', b'hangout', 2378.744528055191], ['Dwalin', b'drossy', 1635.815267086029], 
# ['Oin', b'ispaghul', 2719.505171060562], ['Gloin', b'oversave', 7447.325847148895], ['Dori', b'indoxylic', 5256.7023832798],
# ['Nori', b'swagsman', 10544.385281801224], ['Ori', b'airway', 497.6584358215332], 
# 'Bifur', b'corrosible', 9117.48
# ['Bofur', b'libellate', 11817.507262945175],
# ['Durin', b'purrone', 33996.96827483177]]



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

    for u in users[1:]:
        
        start_time = time.time()
        for choice in wordList:
            
            if bcrypt.hashpw(choice, u.salt.encode()) == u.hash.encode():
                end_time = time.time() - start_time
                print("The password for", u.name, "was cracked in", end_time, "seconds")
                passwords.append([u.name, choice, end_time])
                break


    print(passwords)







if __name__ == "__main__":
    main()