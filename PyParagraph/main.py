#Challenge 4: PyPargraph

#In this challenge, playing as a role of chief linguist at a local
#learning academy. This script assess the complexity of various passages of writing,
#ranging from the sophmoric Twilight novel to the nauseatingly high-minded
#research article. The following are simple set of metrics for assessing complexity:
#       a. Approximate word count
#       b. Approximate sentence count
#       c. Approximate letter count (per word)
#       d. Average sentence length (in words)

#------------------------------------------------------------

#import the operating system module
import os




#prompt user for folder and file name
fileFolder = input("Which folder is the dataset text file located? ")
print("")
fileName = input("What is the name of the dataset text file (include the extension)? ")
print("")


#prompt user for folder and file name to write paragraph analysis
output_fileName = input("Name of text file to write paragraph analysis(include the extension): ")
print("")
output_folderName = input("Output text file's folder location: ")




#create new lists for sentences and words 
sentence_list = []
word_list = []


#open text file containing text passage for analysis
input_text = os.path.join("..", fileFolder, fileName)

with open(input_text, 'r') as text:

    read_text = text.read()

    #calculate the sentence count
    sentence_count = len(read_text.split("."))


    #loop through text to create list of sentences for the passage
    for sentence in read_text.split('.'):

        sentence_list.append(sentence)

    #calculate the number of sentences in text
    num_of_sentences = len(sentence_list) 


    #loop through list of sentences to create a list of words in each sentence. 
    for i in range(num_of_sentences):

        sentence = sentence_list[i]

   
        for word in sentence.split(" "):

            word_list.append(word)


    #approximate word count 
    num_of_words = len(word_list)

    
    #average sentence length
    avg_sent_len = num_of_words / num_of_sentences


    #code below calculates the average letter count
    letter_count_list = [len(x) for x in word_list]

    count =0
    
    for letter in letter_count_list:

        count += letter

    avg_letter_count = count / num_of_words



#write paragraph analysis onto output text file
output_path = os.path.join("..", output_folderName, output_fileName)

with open(output_path, 'w') as output_text: 

    output_text.write("Paragraph Analysis")
    output_text.write("\n")
    output_text.write("-------------------")
    output_text.write("\n")
    output_text.write("Approximate Word Count: " + str(num_of_words))
    output_text.write("\n")
    output_text.write("Approximate Sentence Count: " + str(sentence_count))
    output_text.write("\n")
    output_text.write("Average Letter Count: " + str(avg_letter_count))
    output_text.write("\n")
    output_text.write("Average Sentence Length: " + str(avg_sent_len))
 
    output_text.close()
