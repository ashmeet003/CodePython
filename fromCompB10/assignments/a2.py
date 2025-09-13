# The program demonstrates use of f string method
# The following input functions would ask user for input using the description
# The inputs are stored in respective namedVariables used in madlibstext
adj1 = input("Adjective: ").strip().lower()
invention1 = input("An invention: ").strip().lower()
noun1 = input("Noun (a food): ").strip().lower()
adj2 = input("Adjective: ").strip().lower()
bodypart1 = input("Body part (Plural): ").strip().lower()
adj3 = input("Adjective: ").strip().lower()
noun2 = input("Noun (Plural): ").strip().lower()
noun3 = input("Noun (Plural): ").strip().lower()

# This first line is Bill's text. Don't delete it, unless you are making up your own mad libs.
# added f to use f-string for variable inputs
madlibstext = f"""I would like to say a few {adj1} words about the
most important invention of the twentieth century. I am not
referring to {invention1} or even the discovery of {noun1}.
The most {adj2} invention, in my opinion, is the sneaker.
If it were not for sneakers, our {bodypart1} would be dirty, cold,
and {adj3}. Sneakers keep me from skidding if the {noun2} are slippery,
and when I run, they keep me from stubbing my {noun3}."""

#prints formatted madlibstext using f string
print(madlibstext)