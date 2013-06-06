Text Analysis with Python Redux
========================

*Please note:* This repo is in response to [An introduction to text analysis with Python](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-1/) by Neal Caren. I found a slight error in his code, which skewed the results. 

Problem
--------------

**First, run the results using the original code:**

1. Download sentiment_before.py
2. Run the file. This will create a CSV with the results of the analysis. 

**Next, take a look at the modified code, highlighting the error:**

1. Download sentiment_error.py
2. Run the file. You will see these results:

        [('Obama has called the GOP budget social Darwinism. Nice try, but they believe in social creationism.', 0.05263157894736842, 0.0)]
        ['']  
        []
        
3. The first array is the normal output, indicating that the percent positive is .05263157894736842. This means that there is 1 word in the tweet that is positive. The second and third arrays show the positive and negative words in that specific tweet, respectively. In other words, the blank word, '', within the is being counted as a positive word.

**Where does this word even come from?**

1. Simple. In this for loop--


        for p in list(punctuation):
            tweet_processed=tweet_processed.replace(p,'')
            
  --the original script replaces all the punctuation marks with ''.
  
  Thus, if the next for loop is updated to the code below, this problem will be eliminated:

    for word in words:
        if word in positive_words and word != '':
            pos_words.append(word)
            positive_counter=positive_counter+1
        elif word in negative_words and word != '':
            neg_words.append(word)
            negative_counter=negative_counter+1

Correction
---------

**Let's look at the correct results:**

1. Download sentiment_after.py
2. Run the file. This will create a CSV with the *correct* results of the analysis.
3. You can also look at the analysis to see which tweets changed (highlighted).

Cheers!
