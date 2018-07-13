#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/11/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   This program will encrypt and decrypt a message with a known key.
#	It will also brute force attack a message with an unknown decryption
#	key. As a method of checking the program solutions the debugging 
#	path will take the initial message and key and pass it through all
#	three methods. There is no error checking for 32>char>126 this will
#	give untested results.
#   
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#              	|  	|  
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

instruct = 'Encrypting a message use: " e "\nDecrypting a message use: " d "\nBrute Forcing a message use: " b "\nError Check use: " f "\n'
get_msg = "What is the message for decryption?"
get_clr = "What is the message for encryption?"
get_dkey = "What is your key for decryption?\nEnter a value between 0 and 100"
get_ekey = "What is the key for encryption?\nEnter a value between 0 and 100"

#*  Set initial conditions  *#

selected_run = str()
clear_msg = str()
clear_msg_char = str()
clear_msg_int = int(0)
encrypted_msg = str()
encrypted_msg_char = str()
encrypted_msg_int = int(0)
decrypted_msg = str()
decrypted_msg_char = str()
decrypted_msg_int = int()
encryption_key = int(0)
decryption_key = int(0)
brute_key = int(0)
brute_char = str()
brute_msg = str()


#*  Define functions  *#

def parse_string(in_str, str_step): #this will get each char in sequence#
    out_char = in_str[str_step] #this returns a character by its position in the string#
    return out_char

def char_to_ASCII(in_char): #this will convert a char to the ASCII integer value#
    out_num = ord(in_char) #convert a character to the ASCII integer#
    return out_num

def ASCII_to_char(in_num): #this will convert a ASCII integer value to the char#
    out_char = chr(in_num) #convert an ASCII integer value to a alphanumeric character#
    return out_char

def encrypt_method (clr_char, en_key): #clear_msg_char, encryption_key#
    if ((clr_char + en_key) > int(126)): #encrypted_msg_char + encryption_key#
        en_char = ((clr_char + en_key) - 95) #math formula A#
    else:
        en_char = (clr_char + en_key) #math formula B#
    return en_char #encrypted_char#

def decrypt_method (en_char, de_key): #encrypted_msg_char, decryption_key#
    if (en_char - de_key ) < 32: #encrypted_msg_char + decryption_key#
        de_char = ((en_char - de_key) + 95) #math formula C#
    else:
        de_char = (en_char - de_key) #math formula D#
    return de_char #decrypted_char#

def run_e_method(): #run the encryption method#
    encrypted_msg = str() #declare local variable needed#
    clear_msg = input(print(get_clr)) #get clear message for encryption#
    clear_msg_ln = len(clear_msg) #assign string length of message#
    encryption_key = int(input(print(get_ekey))) #get encryption key#
    for i in range(clear_msg_ln):#scan string with parse_string and hand each char to encryption_method#
        clear_msg_char = parse_string(clear_msg, i) #call function to split out char by position#
        clear_msg_int = char_to_ASCII(clear_msg_char) #this will convert a char to the ASCII integer value#
        encrypted_msg_int = encrypt_method(clear_msg_int, encryption_key) #this is to run the encryption on the clear char#
        encrypted_msg_char = ASCII_to_char(encrypted_msg_int) #this will convert a ASCII integer value to the char#
        encrypted_msg = encrypted_msg + encrypted_msg_char #build encrypted string with string = string + char#

    print('\nYour encrypted message is: ', encrypted_msg,'\nProtect the key\n')#print encrypted message#
    bug_e_msg = encrypted_msg #debugging data#
    bug_e_key = encryption_key #debugging data#
    return bug_e_msg, bug_e_key

def run_d_method(pass_msg, pass_key): #run the decryption method#
    decrypted_msg = str() #declare local variable needed#
    if pass_msg != (0) and pass_key != (0): #used for debug path#
        encrypted_msg = pass_msg #encrypted message passed from run_e_method for decryption#
        decryption_key = int(pass_key) #decryption key passed from run_e_method#
        
    else:
        encrypted_msg = input(print(get_msg)) #get encrypted message for decryption#
        decryption_key = int(input(print(get_dkey))) #get decryption key#
        
    encrypted_msg_len = len(encrypted_msg) #assign string length of message#   
    for i in range(encrypted_msg_len):#scan string with parse_string and hand each char to decryption_method#
        encrypted_msg_char = parse_string(encrypted_msg, i) #call function to split out char by position#
        encrypted_msg_int = char_to_ASCII(encrypted_msg_char) #this will convert a char to the ASCII integer value#
        decrypted_msg_int = decrypt_method(encrypted_msg_int, decryption_key) #this is to run the decryption on the encrypted char#
        decrypted_msg_char = ASCII_to_char(decrypted_msg_int) #this will convert a ASCII integer value to the char#
        decrypted_msg = decrypted_msg + decrypted_msg_char #build decrypted string with string = string + char#

    print('\nYour decrypted message is: ', decrypted_msg, '\nProtect your secrets')#print decrypted message#

def run_b_method(pass_msg): #run the brute force method#
    if pass_msg != (0):
        encrypted_msg = pass_msg #encrypted message passed from run_d_method for decryption#
        
    else:
        encrypted_msg = input(print(get_msg)) #get encrypted message for decryption#

    encrypted_msg_len = len(encrypted_msg) #assign string length of message#
    print("\nRunning Brute Force Cracking Attack")
    print("\nThe following are the decoded messages for keys 1 to 100:")
    brute_key = int(1) #set key to 1 ready for increment#
    while brute_key <= 100: #keep going till you are at the upper limit#
        decrypted_msg = str() #declare local variable needed, will over write after each loop after printing the results#
        for i in range(encrypted_msg_len):#scan string with parse_string and hand each char to decryption_method#
            encrypted_msg_char = parse_string(encrypted_msg, i) #scan string with parse_string and hand each char to decryption_method#
            encrypted_msg_int = char_to_ASCII(encrypted_msg_char) #this will convert a char to the ASCII integer value#
            decrypted_msg_int = decrypt_method(encrypted_msg_int, brute_key)#this is to run the decryption on the encrypted char#
            decrypted_msg_char = ASCII_to_char(decrypted_msg_int) #this will convert a ASCII integer value to the char#
            decrypted_msg = decrypted_msg + decrypted_msg_char #build decrypted string with string = string + char#

        print('Brute Key: ',brute_key, ' --> ',decrypted_msg) #print brute message
        brute_key = brute_key + 1 #increment brute_key by 1

    print("\nThe Brute Force has completed it's message attack.")
    print('\nYour answer is listed above')#this is to run the decryption on the encrypted char#
 
#*  Run program  *#

selected_run = input(print('Are you\n', instruct)) #opening introduction#
selected_run = selected_run.lower(); #selected_run.lower() is to allow both upper and lower case but then converts to lower case to save on logic and lines of code#
while (selected_run != 'e' and selected_run != 'd' and selected_run != 'b' and selected_run != 'f'): #this is checking for valid selection#
    print (instruct) #re run the intro#
    selected_run = input( print( "Please enter a correct selection.") ) #reassigns reselection#
    selected_run = selected_run.lower(); #selected_run.lower() is to allow both upper and lower case but then converts to lower case to save on logic and lines of code#

#* Run Debug math check all series *#

if selected_run == 'f':
    data_msg_e, data_key_e = run_e_method()#run the encryption method#
    print('\nPassing message, ',data_msg_e,' and key, ',data_key_e,' to d_method\n')
    run_d_method(data_msg_e, data_key_e) #run the decryption method#
    print('\nPassing message, ',data_msg_e,' to b_method\n')
    run_b_method(data_msg_e) #run the brute force method#
    print('\nDebug path has complete.')

#*  Run request for clear message and encryption key  *#

if selected_run == 'e':
    run_e_method() #run the encryption method#

#*  Run request for encrypted message and decryption key  *#

if selected_run == 'd':
    run_d_method(0,0) #run the decryption method, nothing to pass#
    
#*  Run request for encrypted message and start brute force *#

if selected_run == 'b':
    run_b_method(0) #run the brute force method, nothing to pass#
    
##* END OF MAIN PROGRAM *##

print('\n\nend of program')

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
