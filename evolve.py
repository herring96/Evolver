import re, ast,time;
from random import choice, randrange, randint;
from extras import read_file, write_to_file, gibberish_check, contraction_split, check_noun, correct_noun, ask_q;
#extras are mine - they can be found in the same folder as this program
#all others are built-in modules

def start ():

    #grabs the replies from the lists stored responses file
    #stored outside this file for extra readability
    to_reply = read_file('responses.txt');
    
    stay = True;
    
    #prints intro and instructions to user
    print ('-'*25 + 'DotUghh 1.0' + '-'*25 + '\n');
    print ('Try to hold a conversation with the computer.');
    print ('Instructions:\n\t-you can ask questions (i.e. who, what, where, why, etc.) or make statements\n\t-to correct the program: type "Correction: a *noun* is defined: ***"\n\t-type \'quit\' to quit');
    print('     -------------------------------------   ');
    print('     |  -------               --------   | '   );
    print('     |  |  -   |             |   -    |  |  ');
    print('     |  --------             ----------  |    ');
    print('     |             |------|              |      ');
    print('     |             |------|              |      ');
    print('     |                                   | ');
    print('     |       |------------------|        |    ');
    print('     |______________------_______________|   ');
    print(' ');

    name = input('Hello. What is your name?: ');

    users = read_file('users.txt');

    current_user = False;

    for user_info in users:

        if name == user_info[0]:
            current_user = user_info;
            break;

    if not current_user:
        
        print ('Ok hi '+name);
        time.sleep(1);
        #new_user = [name, age, [favorites], last mentioned]
        age = eval(input('What is your age? '));
        new_user = [name, age, {}, 'na'];
        print ('Welcome,', name + '.');
        

     

    else:

        print ('Welcome back,', name + '.');
    
    while (stay):

        statement = input('');

        after_split = statement.split('.');
        n=0;
        while n < len(after_split):

            if len(after_split) == 1:
                statement_sp = after_split[n-1];
            else:
                statement_sp = after_split[n];
            
            if statement_sp == '':
                try:
                    n+=1;
                    statement_sp = after_split[n];
                except IndexError:
                    break;
                
            n+=1;

            statement_sp = statement_sp.lstrip();

            statement_e = contraction_split(statement_sp);#splits contractions for easier interpretation
        
            raw_txt = statement_e.capitalize();

            to_brk = False;

            if raw_txt == 'Quit':

                to_brk = True;
                break;

            #removes unnecessary words from beginning to make finding reply easier
            if (len(raw_txt.split()) != 1):

                if re.match('(Ok|And|Because|Or|Well|So|But|Then|Yes|No|Fine|Sure|Oh)(.*)', raw_txt):

                    txt_list = raw_txt.split(' ');
                    del txt_list[0];
                    usr_txt = ' '.join(txt_list);

                else:
    
                    usr_txt = raw_txt;

                usr_txt = usr_txt.capitalize();

            else:

                usr_txt = raw_txt.capitalize();

            articles = [' the ', ' a ', ' an ', ' these ', ' those ', ' them ', ' some '];

            while (1):

                apart = usr_txt.split(' ');
                
                art_check = False;

                for article in articles:

                    if article in usr_txt:
                        art_check = True;
                        break;

                if re.match('Correction(.*)', usr_txt):

                    correct_noun(usr_txt);
                
                elif (apart[0] =='You' and apart[1] =='are'):
                    ask_q(usr_txt);
                    
                elif (apart[0] == "I" and apart[1] == 'am'):#sends it to question part
                    ask_q(usr_txt);

                elif (apart[0] == 'Do' and apart[1] =='you'):#sends it to response part
                    check_noun(usr_txt);

                elif 'my favorite' in usr_txt.lower():

                    split = usr_txt.split();
                    
                    to_find1 = split.index('favorite');
                    subject = split[to_find1+1];
                    to_find2 = split.index('is');
                    fav = split[to_find2+1];

                    if current_user:
                        current_user[2][subject] = fav;

                    else:
                        new_user[2][subject] = fav;
                    
                elif art_check:
                    check_noun(usr_txt);

                else:
                    
                    for comment in to_reply:
    
                        if re.match(comment[0], usr_txt):
                            picked = choice(comment[1]);
                            
                            if picked == 'not found':
                                picked = gibberish_check(usr_txt, picked);
                            print (picked);
                            break;
            
                break;
            
        if to_brk:
            break;

    if current_user:
        
        i = 0;
        while (i<len(users)):
            if users[i][0] == name:
                break;
            i+=1;

        users[i] = current_user;

    else:

        users.append(new_user);
        
    write_to_file(users, 'users.txt');

start ();
