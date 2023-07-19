def email_slicer():
    print("Welcome to my email slicer")
    print("")

    while True:
        email_input = input("Input your email address: " "\n")

        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")

        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: .", extension, "\n")


email_slicer()
