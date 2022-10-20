import wikipedia
import webbrowser

topic = input("Enter the topic : ")
sentences = int(input("Enter the number of lines do you want : "))

try:
   pass
except:
   print("Invalid Number of lines, PLease Enter valid number & Run the program Again!")
   exit()

try:
   result = wikipedia.summary(topic, sentences)
   print(result)
   open_res = input("Do you want to open full wikipedia page in the browser (y/n): ")

   if open_res == "Y" or open_res == "y":
      webbrowser.open(f"https://en.wikipedia.org/wiki/{topic}")
   else:
      print(f"You can press n or any key to close!")

except:
   print(f"Sorry, '{topic}' Wikipedia Article not found!")
