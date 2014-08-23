import re, ast, webbrowser, time;
from random import choice, randrange, randint;
#all others are built-in

def read_file (file_to_read):
    """reads the specified file

    converts string in file to list, dictionary, etc.
    returns converted text
    """

    file = open(file_to_read);
    str_txt = file.read();
    converted = ast.literal_eval(str_txt);
    file.close();

    return (converted);


def write_to_file (text, file_to_edit):
    """opens specified file to write to

    converts list,dictionary, or other text to string
    """

    output_file = open(file_to_edit, 'w');
    output_file.write(str(text));
    output_file.close();

def gibberish_check (to_check, initial):
    """checks to see if user input is gibberish

    returns initial reply if no gibberish found
    looks at number of consonents in a row
    """

    consonents = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'];

    c_count = 0;
    c_check = 0;
    g_check = 0;

    for letter in to_check.upper():

        for c in consonents:
            if c == letter:
                c_count += 1;
                c_check = 1;
                break;

        if c_count >= 4:
            g_check = 1;
            break;

        if c_check == 0:
            c_count = 0;

        c_check = 0;

    if g_check == 1:
        return ('This will eventually be a quote from Finnegan\'s Wake.');
    else:
        return (initial);


def contraction_split (text):
    """takes contractions and splits them up into their individual words

    allows me to account for less user comments in my responses function
    """

    contractions = ["i'm", "you're", "they're", "we're", "she's", "he's", "don't", "can't", "won't", "shouldn't", "wouldn't", "couldn't", "didn't", "that's", "aren't", "isn't"];
    split = ["I am", "you are", "they are", "we are", "she is", "he is", "do not", "cannot", "will not", "should not", "would not", "could not", "did not", "that is", "are not", "is not"];

    to_check_str = text.lower();
    to_check = to_check_str.split();
    to_return = text;

    for word in to_check:

        if word in contractions:

            pos = contractions.index(word);
            replace_with = split[pos];

            to_return = to_check_str.replace(word, replace_with);

    return to_return;


def ask_q (text):#used to prompt questions
    feelings = ['happy', 'sad', 'angry', 'exicted', 'confused'];
    computers = ['computer', 'robot'];

    for computer in computers:
        if computer in text:
            print('You are a'+' '+computer);
            time.sleep(1);
    
    for feeling in feelings:
        if feeling in text:
            print('why are you feeling'+ ' '+feeling+" " );
            break;


def check_noun (text):
    
    articles = ['the', 'a', 'an', 'these', 'those', 'them', 'some'];
    punctuation = ['.', '?', '!', ',', ')'];
    listed = text.split(' ');
    tosrch = False

    if (not tosrch and listed[0] =='Do' and listed[1] =='you'):
        noun = listed[3];
        
        
    for article in articles:
        if article in listed:
            tosrch = True
            to_search = article;
            break;
        
    if tosrch:
        art_index = listed.index(to_search);
        noun = listed[art_index+1];


    for item in punctuation:

        if item in noun:

            temp = list(noun);
            del temp[temp.index(item)];
            noun = ''.join(temp);
            break;
        
    dict_defs = read_file('defs.txt');
         
              
    res = ['Wow Cool',
                     'Thanks for letting me know',
                     'That\'s awesome',
                     'DEFINITION ADDED BEEP BOOP. No just kidding I understand',
                     'My knowledge has been furthered and for that I am thankful',
                     'Ok cool',
                     'Hmmm very interesting' ,
                     'Wow the world is a magical place',
                     'Very interesting',
                     'Wow that\'s really fascinating',
                     'Pretentious, much?'];
    
    if noun in dict_defs.keys():#we should add if/and question="what"
        print (dict_defs[noun]);
        time.sleep(2);
        pic = input('Would you like more information on ' +noun+'s? ');
        info = pic.capitalize();
        
        if (info =='Yes'):
            new = 2;
            Url = 'http://en.wikipedia.org/wiki/';
            webbrowser.open(Url+noun,new=new);
            
        else:
            print('ok');
            
    else:
        if noun[-1] =='s':
            noun = noun[0:-1];
            
        if (noun[0] in ['a','e','i','o','u']):
            art = 'an';
        
        else:
            art = 'a';
            definition_to_add = input('What is ' + art + ' ' + noun + '?\n');
            print (choice(res));
            dict_defs[noun] = definition_to_add;
            write_to_file(dict_defs, 'defs.txt');
                
def check_art (word): 
    art_icle = False;
    articles = ['a', 'an', 'the', 'these', 'those', 'them', 'some'];
    if word in articles:
        art_icle = True;
    return art_icle;


def correct_noun (text):

    articles = ['the', 'a', 'an', 'these', 'those', 'them', 'some'];
    punctuation = ['.', '?', '!', ',', ')'];

    listed = text.split(' ');
	
    a_index = listed.index('a');
    noun = listed[a_index+1];

    split = text.split('defined:');

    to_add = split[1].lstrip();

    for item in punctuation:

        if item in to_add:

            temp = list(to_add);
            del temp[temp.index(item)];
            to_add = ''.join(temp);
            break;

    dict_defs = read_file('defs.txt');

    if noun in dict_defs.keys():
        dict_defs[noun] = to_add.capitalize();
        print ('Hey, you learn something new every day!');

    else:
        'I don\'t even know what that is...';
        
    write_to_file(dict_defs, 'defs.txt');
