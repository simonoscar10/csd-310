


while True:
  try:
    userIn = int(input(' Enter a number from 1-4: '))
    if userIn > 0 and userIn < 5:
        break
    print("\n  Invalid number please enter a number between 1 and 4\n")
  except Exception as e:
    print(e)
userInput = userIn
print(userInput)