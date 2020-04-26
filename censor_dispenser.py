# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms =  ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",  "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# censorsaccounts for punctuation, preserves length,
def censor_bar(text, character='#'):
  for i in [',', '.', '!', '?']:
    if i in text:
      bar = character* (len(text) -1) + i
      return bar
  bar = character* len(text)   
  return bar

# identifies target word, uses censor_bar to censor them
def cfilter(text, target):
  if target in text:
    text = text.replace(target, censor_bar(target))
  return text

# uses cfilter to go through whole list of words, checks for variants 
def excfilter(text, targets):
  for target in targets:
    varients = [target, target.title(), target.upper()]
    for v in varients:
      text = cfilter(text, v)
  return text
 
# Takes two lists; censors words form one list, and multuple uses of one words from the other
def negexcfilter(text, targets, negs):
  ltext = text.split()
  nindex = 0
  for i in ltext:
    neg_count = 0
    for neg in negs:
      if neg in i:
        if neg_count > 0:
          ltext[nindex] = censor_bar(neg)
        neg_count += 1
    nindex += 1
  ntext = ' '.join(ltext)
  ntext = excfilter(ntext, targets)
  return ntext

# Takes an already censored document, improves coverage censors imediately surrounding words
def totald(text):
  ltext = text.split()
  nindex = 0
  for i in ltext:   
    if '##' in i:
      ltext[nindex] = censor_bar(ltext[nindex])
      if nindex == len(ltext)-1:
        pass
      else:
        ltext[nindex+1] = censor_bar(ltext[nindex + 1], '@')
      if nindex == 0: 
        pass
      ltext[nindex -1] = censor_bar(ltext[nindex - 1], '@')
    nindex += 1
  ntext = ' '.join(ltext)
  ntext = excfilter(ntext, '@')
  return ntext

# preserves document formatting, uses excfilter and totald censorrs everything required
def trufilter(text, targets, negs):
  text = excfilter(text, targets)
  text = excfilter(text, negs)
  ptext = text.split('\n')
  loutput = []
  for p in ptext:
    ntext = totald(p)
    loutput.append(ntext)
  output = '\n'.join(loutput)
  
  return output
    
    
 
    
    
    
    
    
#print(cfilter(email_one, 'learning algorithms'))
#print(excfilter(email_two, proprietary_terms))
#print(negexcfilter(email_three, proprietary_terms, negative_words))
print(trufilter(email_four, proprietary_terms, negative_words))
#print(email_four)
