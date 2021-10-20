import time as t
import matplotlib.pyplot as plt

times=[]
mistakes=0

print("Typing test, type 'programming' 5 times, this will be timed.")

input("Press enter to continue.")

while len(times)<5:
    startTime = t.time()
    word=input("Type the word: ")
    endTime = t.time()
    time_elapsed = endTime - startTime

    times.append(time_elapsed)

    if (word.lower() !="programming"):
        mistakes +=1
print("You made " + str(mistakes) + " mistake(s).")
print("Now let's see your evolution.")
t.sleep(3) # give user time to read this

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.show()