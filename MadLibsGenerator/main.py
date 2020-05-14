def go_mad(inp):
    print("Be kind to your {0}-footed {1} For a duck may be somebody`s {2}, Be kind to your {1} in {3}. Where the weather is always {4}. You may think that this is the {5}, Well it is.".format(
        inp[0], inp[1], inp[2], inp[1], inp[3], inp[4], inp[5]))


def get_input():
    print("Noun, Noun(Plural), Noun, Place, Adjective, Noun")
    print("Enter a list of comma seprated strings in the above order:")
    inp = input()
    inp = inp.split(",")
    go_mad(inp)


if __name__ == "__main__":
    get_input()
