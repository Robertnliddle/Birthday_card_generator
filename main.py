#Birthday card generator

input_value = input("What is the recipient's name? ")
input_number = input("What year is the recipient's born? ")
input_number = int(input_number)
interger_number = 2023
input_personalized_message = input("What do you want to write in the birthday card? ")
input_senders_name = input("Who is sending the birthday card? ")


print("----------------------------")

print(
    f"Happy birthday {input_value}, you are now turning {interger_number - input_number} years old! "
)

print(input_personalized_message)

print("With love and wishes")
print(input_senders_name)

print("----------------------------")

