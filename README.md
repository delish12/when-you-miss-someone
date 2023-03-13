# when-you-miss-someone

## how the code works-
run the code with chrome driver in the folder and open any whats app or any other 
social midea user chat which is compatible with clip board and place the cursor in the
typing dialouge box let the code do the work


### code uses selenium to webscrape from a given link
### the link i used was 'https://www.google.com/search?q=want+to+talk+with+you+pics+cute&rlz=1C1GCEB_enIN978IN978&hl=en&sxsrf=AJOqlzUbARKVRw9fnyO7ScfvRDX5FVKXlA:1678438865941&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjcvoaDgNH9AhUn9DgGHeFmCycQ_AUoAXoECAIQAw'

### whomever familier with selenium with the basics can under this code pretty easily

## libs used -
selenium
time
keyboard
BytesIO
win32clipboard
PIL
os


## Line 17 -
checks if sample_data folder exsists else create it

## Line 40 -
getting the link to the driver
### note that chrome driver is important to work. also it must be compatible with the system chrome os

## Line 45 -
gets the class container by xpath

then two for loops for appending the images to the src list
and saving it in the sample_data folder


other for loop in the keyboard pic section is for coping the pic in the clip board
and pasting it in the chat using send_to_clipboard function

if program is terminated in the middle remove section will not initiate

remove section is for removing all the pics after sending the pics
in line 29 the no_of_pics vairable is responsible for saving the given no.of pics in the folder
and sending it to the person


## Note-
if user wishes to end the program in the middle of sending it
make sure to manually remove all the pics in the sample_data folder