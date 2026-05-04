password = "112233"
attempt = 3
while True:
        enter = input("Enter Your Password: ")
        if (enter == password):
                print("Password Is Correct")
                break
        else:
                print("Password Is Wrong")
                attempt -= 1
                if (attempt == 0):
                        print("All Attempt Used")
                        break