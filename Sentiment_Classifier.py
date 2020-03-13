"""
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(lst):
    list1=""
    for i in lst:
        if i in punctuation_chars:
            continue
        else:
            list1+=i
    return list1

"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(lst):
    list1=""
    for i in lst:
        if i in punctuation_chars:
            continue
        else:
            list1+=i
    return list1

def get_pos(st):
    st_list=st.split()
    pos=0
    for i in st_list:
        y=strip_punctuation(i)
        if y.lower() in positive_words:
            pos+=1
    return pos

"""
Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(lst):
    list1=""
    for i in lst:
        if i in punctuation_chars:
            continue
        else:
            list1+=i
    return list1

def get_neg(st):
    st_list=st.split()
    pos=0
    for i in st_list:
        y=strip_punctuation(i)
        if y.lower() in negative_words:
            pos+=1
    return pos

"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(lst):
    list1=""
    for i in lst:
        if i in punctuation_chars:
            continue
        else:
            list1+=i
    return list1
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())









with open("project_twitter_data.csv") as pos_f:
    tweet_text=[]
    retweet_count=[]
    reply_count=[]
    for line in pos_f:
        tweet_info=line.split(",")
        tweet_text.append(tweet_info[0])
        retweet_count.append(tweet_info[1])
        reply_count.append(tweet_info[2])
    tweet_text=tweet_text[1:]
    retweet_count=retweet_count[1:]
    reply_count=reply_count[1:]
reply_count_m=[]
for i in reply_count:
    reply_count_m.append(i[0])



def get_pos(st):
    st_list=st.split()
    pos=0
    for i in st_list:
        y=strip_punctuation(i)
        if y.lower() in positive_words:
            pos+=1
    return pos
def get_neg(st):
    st_list=st.split()
    neg=0
    for i in st_list:
        y=strip_punctuation(i)
        if y.lower() in negative_words:
            neg+=1
    return neg

def results():
    count=0
    list_result=[]
    for i in tweet_text:
        pos=get_pos(i)
        neg=get_neg(i)
        noret=retweet_count[count]
        norep=reply_count_m[count]
        net=pos-neg
        list_result.append((noret,norep,pos,neg,net))

    return   list_result
y=results()

result_file=open("resulting_data.csv","w")
result_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
for line in y:
    str_line="{},{},{},{},{} \n".format(line[0],line[1],line[2],line[3],line[4])
    result_file.write(str_line)
result_file.close()
